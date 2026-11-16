# PES2UG24CS473 - Software Engineering Lab 7
## Highway Toll Calculator - Hypothesis Fuzz Testing

This folder keeps the untouched starter files separate from the corrected implementation and Hypothesis tests.

### Folder structure

- `original/` - files copied from the assigned starter repository, unchanged.
- `updated/` - corrected application and completed Hypothesis property-based tests.
- `screenshots/` - terminal evidence captured while running the original and updated versions.

### Run the updated version

From this Lab 7 folder:

```cmd
python updated\highway_toll.py
python -m pytest -v updated\test_highway_toll.py
```

Install dependencies first:

```cmd
python -m pip install hypothesis pytest
```

### Verification

The updated test suite was run locally using Python 3.13.15, pytest 8.3.4, and Hypothesis 6.170.15. Result: **10 passed**.

See `original/README.md` for the starter repository's original notes and `updated/README.md` for the completed work and test details.

### Screenshot evidence

Place the four actual terminal screenshots in `screenshots/`:
1. `01_original_application.png`
2. `02_failing_hypothesis_tests.png`
3. `03_fixed_application.png`
4. `04_passing_hypothesis_tests.png`

Screenshots are captured from real terminal executions and should not be fabricated.
