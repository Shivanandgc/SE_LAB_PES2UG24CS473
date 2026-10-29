# SE Lab 06 — Code and Branch Coverage

This folder contains the Lab 6 highway toll calculator and tests.

## Files

- `highway_toll.py`: application under test.
- `CodeCoverageTest_PES2UG24CS473_application.py`: tests used for code/statement coverage.
- `BranchCoverageTest_PES2UG24CS473_application.py`: tests used for branch coverage.
- `screenshots/code_coverage.png`: terminal evidence for code coverage.
- `screenshots/branch_coverage.png`: terminal evidence for branch coverage.

## Run tests

Run these commands from this folder with Python, pytest and coverage installed.

### Code coverage

```powershell
python -m coverage erase
python -m coverage run --source=highway_toll -m pytest -q CodeCoverageTest_PES2UG24CS473_application.py
python -m coverage report -m
```

### Branch coverage

```powershell
python -m coverage erase
python -m coverage run --branch --source=highway_toll -m pytest -q BranchCoverageTest_PES2UG24CS473_application.py
python -m coverage report -m
```

Coverage screenshots must be taken from the actual local run and saved under `screenshots/`. Screenshots are intentionally not fabricated in this repository.
