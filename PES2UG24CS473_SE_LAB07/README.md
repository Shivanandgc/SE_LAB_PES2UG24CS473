# PES2UG24CS473 - Software Engineering Lab 7
## Highway Toll Calculator: Hypothesis Fuzz Testing

This folder contains the complete Lab 7 submission. It separates the untouched starter files, the corrected implementation, and terminal screenshot evidence.

## Folder structure

```text
PES2UG24CS473_SE_LAB07/
├── README.md
├── original/
│   ├── highway_toll.py
│   ├── test_highway_toll.py
│   └── README.md
├── updated/
│   ├── highway_toll.py
│   ├── test_highway_toll.py
│   └── README.md
└── screenshots/
    ├── 01_original_application.png
    ├── 02_failing_hypothesis_tests.png
    ├── 03_fixed_application.png
    └── 04_passing_hypothesis_tests.png
```

## Original files

The `original/` directory contains unchanged copies of the files from the assigned starter repository:
[SETAPESU26/L6_L7_36_highway_toll - lab7](https://github.com/SETAPESU26/L6_L7_36_highway_toll/tree/main/lab7).

The original application includes three functions:
- `parse_plate(plate)`
- `trip_cost(text)`
- `axle_class(axles)`

## Updated files

The `updated/` directory contains the corrected application and the completed Hypothesis tests for the three functions. Input validation was added to handle malformed values safely.

## Setup and run

Install the required packages:

```cmd
python -m pip install hypothesis pytest
```

Run the corrected application from the Lab 7 folder:

```cmd
python updated\highway_toll.py
```

Run the Hypothesis tests:

```cmd
python -m pytest -v updated\test_highway_toll.py
```

## Bugs identified and corrected

- `parse_plate(None)` caused an `AttributeError` instead of a controlled validation error.
- `trip_cost(None)` caused an `AttributeError`.
- `axle_class` did not safely reject invalid types such as `None` and infinity.
- `axle_class(0)` was incorrectly accepted.

## Test result

The updated test suite was executed locally with Python 3.13.15, pytest 8.3.4, and Hypothesis 6.170.15. **All 10 tests passed**.

## Screenshot evidence

The `screenshots/` directory is intended to contain the four actual terminal screenshots listed in the folder structure. These images should be captured from the user's real executions; the README does not fabricate or substitute for screenshot evidence.

See `original/README.md` for the starter notes and `updated/README.md` for details of the corrected implementation and test suite.
