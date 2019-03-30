#!/usr/bin/python3

import json
import os
import sys


def main():
    if not os.path.isabs(sys.argv[1]):
        print("Please enter the full path of the file!")
        exit(1)
    elif os.path.exists(sys.argv[1]):
        data_file_path = sys.argv[1]
    else:
        print("File does not exist!")
        exit(1)

    with open(data_file_path) as f:
        data = json.load(f)

        capacities, distinct_transports = \
            get_capacities_and_distinct_transports(data['transports'])

        output(sort_values(capacities))
        print()
        output(sort_values(distinct_transports))


def get_capacities_and_distinct_transports(transports_data):
    unique_car_models = set()
    unique_train_models = set()
    unique_plane_models = set()

    cars_total_capacity = 0
    trains_total_capacity = 0
    planes_total_capacity = 0

    for transport in transports_data:
        transport = dict((k.lower(), v) for k, v in transport.items())

        is_car = 'manufacturer' and 'passenger-capacity' in transport.keys()
        is_train = 'number-wagons' and 'w-passenger-capacity' in \
            transport.keys()
        is_plane = 'b-passenger-capacity' and 'e-passenger-capacity' in \
            transport.keys()

        if is_car:
            unique_car_models.add(transport['model'])
            cars_total_capacity += transport['passenger-capacity']
        elif is_train:
            unique_train_models.add(transport['model'])
            trains_total_capacity += transport['number-wagons'] * \
                transport['w-passenger-capacity']
        elif is_plane:
            unique_plane_models.add(transport['model'])
            planes_total_capacity += transport['b-passenger-capacity'] + \
                transport['e-passenger-capacity']

    capacities = {
        'cars': cars_total_capacity,
        'trains': trains_total_capacity,
        'planes': planes_total_capacity
    }

    distinct_transports = {
        'distinct-cars': len(unique_car_models),
        'distinct-trains': len(unique_train_models),
        'distinct-planes': len(unique_plane_models)
    }

    return capacities, distinct_transports


def sort_values(values_dict):
    return sorted(((value, key) for key, value in values_dict.items()),
                  reverse=True)


def output(sorted_items):
    for item in sorted_items:
        print('"{type}": {value}'.format(type=item[1], value=item[0]))


if __name__ == '__main__':
    main()
