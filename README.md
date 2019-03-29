# transport_info

Command line tool that takes the full path of a file that contains a JSON array
of cars, trains, and planes. It's assumed data is well formatted and contains
between 100 - 1000000000 records.

It will output in the console a sorted list of transport types capacities and a
count of distinct models.

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

## Virtual Env
```
$ python3.7 -m venv env
```

```
$ python -V
Python 3.7.2
```

To activate the env

    source env/bin/activate

To deactivate the env

    deactivate

## Run script
```
$ python transport.py <full_path_to_file>
```

## Run tests
```
$ python transport_tests.py
```
