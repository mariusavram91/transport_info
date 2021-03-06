#!/usr/bin/python3
"""Lists total passenger capacities by type of transport and count of transport
type distinct models given a path to a txt file with data."""

import ijson
import os

from typing import Generator, List, Tuple


def main(data_file_path: str) -> None:
    """Requires the full path of the file with JSON data. Then outputs the
    sorted values in the console."""

    if not os.path.isabs(data_file_path):
        print("Please enter the full path of the file!")
        exit(1)
    elif not os.path.exists(data_file_path):
        print("File does not exist!")
        exit(1)

    with open(data_file_path) as f:
        transports = ijson.items(f, 'transports.item')

        capacities, distinct_transports = \
            get_capacities_and_distinct_transports(transports)

        output(sort_values(capacities))
        print()
        output(sort_values(distinct_transports))


def get_capacities_and_distinct_transports(transports_data: Generator[dict, None, None]) -> Tuple[dict, dict]:
    """
    Returns two dicts with total capacities for each type of transport and
    counts of each distinct models for each type of transport.

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


def sort_values(values_dict: dict) -> List[tuple]:
    """Returns a list of tuples that is sorted by the values of a given dict."""

    return sorted(((value, key) for key, value in values_dict.items()),
                  reverse=True)


def output(sorted_items: List[tuple]) -> None:
    """Prints the sorted list with type of transport and its value."""

    for value, type in sorted_items:
        print(f'"{type}": {value}')


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Lists total passenger \
            capacities by type of transport and count of transport \
            type distinct models given a path to a txt file with data.")
    parser.add_argument("path", help="full path of the data file")
    parser.add_argument("-v", action="version", version="0.1")

    args = parser.parse_args()

    main(args.path)
