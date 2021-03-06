# transport_info

Command line tool that takes the full path of a file that contains a JSON array
of cars, trains, and planes. It's assumed data is well formatted and contains
between 100 - 1000000000 records.

It will output in the console a sorted list of transport types capacities and a
count of distinct models.

[![Build Status](https://travis-ci.org/mariusavram91/transport_info.svg?branch=master)](https://travis-ci.org/mariusavram91/transport_info)

## Total capacities by type of transport

Cars:

    passenger-capacity

Trains:

    number-wagons * w-passenger-capacity

Planes:

    b-passenger-capacity + e-passenger-capacity

## Example

For instance, in this example file (data.txt):

```
{
  "transports": [
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
}
```

when the script is executed
```
$ python tranport.py /tmp/data.txt
```

the output in the console will be:
```
"planes": 524
"trains": 150
"cars": 14

"distinct-cars": 3
"distinct-planes": 2
"distinct-trains": 1
```

## Run script

**Dependencies**

ijson library is needed, you can install it by:

```
$ pip install -r requirements.txt
```
Then you can execute the script

```
$ python transport.py <full_path_to_file>
```

You can use -h for help and -v for the version:

```
$ python transport.py -h
usage: transport.py [-h] [-v] path

Lists total passenger capacities by type of transport and count of transport
type distinct models given a path to a txt file with data.

positional arguments:
  path        full path of the data file

optional arguments:
  -h, --help  show this help message and exit
  -v          show program's version number and exit
```

```
$ python transport.py -v
0.1
```

## Run tests
```
$ python transport_tests.py
```

## Benchmarking

```
$ /usr/bin/time -p python transport.py /tmp/data.txt
real 0.03
user 0.03
sys 0.00
```

Profiling
```
$ python -m cProfile -s tottime -o profile.stats transport.py /tmp/data.txt
$ snakeviz profile.stats
```

![Graph](profile_output_1.png)

![Table](profile_output_2.png)
