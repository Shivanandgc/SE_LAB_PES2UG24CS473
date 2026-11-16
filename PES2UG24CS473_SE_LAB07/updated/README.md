# Updated Lab 7 - Corrected Highway Toll Calculator

This folder contains the corrected application and completed Hypothesis property-based tests.

## Functions
- `parse_plate(plate)`: validates and parses a vehicle registration plate.
- `trip_cost(text)`: calculates trip cost from an expression such as `3x150`.
- `axle_class(axles)`: classifies vehicles by axle count.

## Files
- `highway_toll.py`: corrected application with defensive input validation.
- `test_highway_toll.py`: Hypothesis property-based tests.

## Setup and execution

```cmd
python -m pip install hypothesis pytest
python highway_toll.py
python -m pytest -v test_highway_toll.py
```

## Bugs found in the original
- `parse_plate(None)` raised an `AttributeError` instead of a controlled validation error.
- `trip_cost(None)` raised an `AttributeError`.
- `axle_class` did not safely reject invalid types such as `None` and infinity.
- `axle_class(0)` was incorrectly accepted and classified.

## Final verification
The corrected version passed all **10 Hypothesis tests** locally with Python 3.13.15, pytest 8.3.4, and Hypothesis 6.170.15.

The actual terminal screenshots are stored in the sibling `../screenshots/` folder.
