# PES2UG24CS473 - Software Engineering Lab 7
## Hypothesis Fuzz Testing - Highway Toll

This is the separate Lab 7 submission folder. It is based on the assigned starter repository:
[SETAPESU26/L6_L7_36_highway_toll - lab7](https://github.com/SETAPESU26/L6_L7_36_highway_toll/tree/main/lab7).

The handout describes the workflow using generic `processor.py` and `test_processor.py` names. The assigned starter repository uses `highway_toll.py` and `test_highway_toll.py`, so those names are retained here.

## Functions tested

- `parse_plate(plate)` - validates and parses a vehicle registration plate.
- `trip_cost(text)` - calculates trip cost from a count/rate expression such as `3x150`.
- `axle_class(axles)` - classifies vehicles by axle count.

## Files

- `highway_toll.py` - corrected application with input validation.
- `test_highway_toll.py` - Hypothesis property-based tests.

## Setup

Install the dependencies:

```cmd
python -m pip install hypothesis pytest
```

## Run

Run these commands from this directory:

```cmd
python highway_toll.py
python -m pytest -v test_highway_toll.py
```

## Verification results

The local verification run completed successfully: **10 tests passed** using Python 3.13.15, pytest 8.3.4, and Hypothesis 6.170.15.

During testing of the original starter application, Hypothesis exposed invalid-input handling defects:
- `parse_plate(None)` raised `AttributeError` instead of a controlled `ValueError`.
- `trip_cost(None)` raised `AttributeError` instead of a controlled `ValueError`.
- `axle_class` did not safely reject invalid types such as `None` and infinity.
- `axle_class(0)` was incorrectly accepted and classified.

The corrected application validates these inputs, and the final property-based test run passed all 10 tests.

## Screenshot evidence

Create a local folder named `screenshots` and place the four actual terminal screenshots in it:

1. `01_original_application.png` - original application with valid sample inputs.
2. `02_failing_hypothesis_tests.png` - Hypothesis failures against the original application.
3. `03_fixed_application.png` - corrected application with valid sample inputs.
4. `04_passing_hypothesis_tests.png` - final run showing 10 passing tests.

Screenshots should be captured from the actual terminal run; they are not generated or fabricated by this README.
