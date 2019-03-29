#!/usr/bin/python3

import transport
import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.empty_data = []
        self.test_data = [
                {
                    "model": "Boeing 777",
                    "B-passenger-capacity": 14,
                    "E-passenger-capacity": 300
                },
                {
                    "manufacturer": "BMW",
                    "model": "M3",
                    "passenger-capacity": 4
                },
                {
                    "model": "ICE",
                    "Number-wagons": 5,
                    "w-passenger-capacity": 30
                },
                {
                    "manufacturer": "Mercedes Benz",
                    "model": "C Klasse",
                    "Passenger-capacity": 4
                },
                {
                    "model": "Boeing 777S",
                    "B-passenger-capacity": 10,
                    "E-passenger-capacity": 200
                },
                {
                    "manufacturer": "Audi",
                    "model": "Q3",
                    "passenger-capacity": 6
                }
            ]
        self.test_capacities = {
            'cars': 6,
            'trains': 1,
            'planes': 3
        }

    def test_get_capacities_and_distinct_transports_returns_0_for_empty_data(self):
        capacities, distinct_transports = \
            transport.get_capacities_and_distinct_transports(self.empty_data)

        expected_capacities = {
            'cars': 0,
            'trains': 0,
            'planes': 0
        }

        expected_distinct_transports = {
            'distinct-cars': 0,
            'distinct-trains': 0,
            'distinct-planes': 0
        }

        self.assertDictEqual(capacities, expected_capacities)
        self.assertDictEqual(distinct_transports, expected_distinct_transports)

    def test_get_capacities_and_distinct_transports_returns_totals(self):
        capacities, distinct_transports = \
            transport.get_capacities_and_distinct_transports(self.test_data)

        expected_capacities = {
            'cars': 14,
            'trains': 150,
            'planes': 524
        }

        expected_distinct_transports = {
            'distinct-cars': 3,
            'distinct-trains': 1,
            'distinct-planes': 2
        }

        self.assertDictEqual(capacities, expected_capacities)
        self.assertDictEqual(distinct_transports, expected_distinct_transports)

    def test_sort_values_returns_list_of_set_sorted_by_value(self):
        sorted_capacities = transport.sort_values(self.test_capacities)
        expected_capacities = [
            (6, 'cars'),
            (3, 'planes'),
            (1, 'trains')
        ]

        self.assertListEqual(sorted_capacities, expected_capacities)

if __name__ == '__main__':
    unittest.main()
