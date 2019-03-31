#!/usr/bin/python3
"""Lists total passenger capacities by type of transport and count of transport
type distinct models given a path to a txt file with data."""

import json
import os


def main(data_file_path):
    """Requires the full path of the file with JSON data. Then outputs the
    sorted values in the console."""

    if not os.path.isabs(data_file_path):
        print("Please enter the full path of the file!")
        exit(1)
    elif not os.path.exists(data_file_path):
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
    """
    Returns two dicts with total capacities for each type of transport and
    counts of each distinct models for each type of transport. Requires a
    list of dicts with the different transport info.

    Car total capacity: passenger-capacity value
    Train total capacity: number-wagons * w-passenger-capacity
    Plane total capacity: b-passenger-capacity + e-passenger-capacity
    """

    unique_car_models = set()
    unique_train_models = set()
    unique_plane_models = set()

    cars_total_capacity = 0
    trains_total_capacity = 0
    planes_total_capacity = 0

    for transport in transports_data:
        # Lowercase for all the keys in the transport dict
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
    """Returns a list of sets that is sorted by the values of a given dict."""

    return sorted(((value, key) for key, value in values_dict.items()),
                  reverse=True)


def output(sorted_items):
    """Prints the sorted list with type of transport and its value."""

    for item in sorted_items:
        print('"{type}": {value}'.format(type=item[1], value=item[0]))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Lists total passenger \
            capacities by type of transport and count of transport \
            type distinct models given a path to a txt file with data.")
    parser.add_argument("path", help="full path of the data file")
    parser.add_argument("-v", action="version", version="0.1")

    args = parser.parse_args()

    main(args.path)
