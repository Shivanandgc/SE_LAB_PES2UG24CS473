# SE Lab 7 - Hypothesis Fuzz Testing (Highway Toll)

This Lab 7 folder is based on the assigned starter repository:
[SETAPESU26/L6_L7_36_highway_toll - lab7](https://github.com/SETAPESU26/L6_L7_36_highway_toll/tree/main/lab7).

> Handout alignment note: the supplied handout uses generic names `processor.py` and `test_processor.py`. The assigned repository uses `highway_toll.py` and `test_highway_toll.py`; the same six-step fuzzing workflow is applied to the repository's three functions.

## Functions tested

- `toll_for(axles, is_peak, has_fastag)`
- `toll_charge(vehicle, axles, is_peak, has_fastag)`
- `pass_advice(trips, axles, pass_price)`

## Files

- `highway_toll.py` - hardened application with defensive input validation.
- `test_highway_toll.py` - Hypothesis property-based tests and malformed-input regression tests.
- `evidence/` - location for the four required terminal screenshots.

## Setup

```powershell
python -m pip install hypothesis pytest
```

## Run

Run in this directory:

```powershell
python highway_toll.py
python -m pytest -q test_highway_toll.py
```

The Hypothesis tests generate valid and malformed values for all three functions. They check rate calculations, non-negative finite results, emergency vehicle exemptions, pass recommendations, invalid axle values, invalid boolean flags, invalid pass prices, and malformed trip structures.

## Evidence to capture locally

1. Initial run of the original buggy program.
2. Failing Hypothesis test output against the buggy starter.
3. Run of the fixed application.
4. Passing Hypothesis test output against the fixed application.

Capture actual output in your terminal and save the images as `evidence/01_initial_application.png`, `evidence/02_failing_fuzz_tests.png`, `evidence/03_fixed_application.png`, and `evidence/04_passing_fuzz_tests.png`. Screenshots are not fabricated or included until captured from a real run.

## Source

The calculation rates and function behavior originate from the assigned starter source. The defensive validation and property tests are the Lab 7 changes.
