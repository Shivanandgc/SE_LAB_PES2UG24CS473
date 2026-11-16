"""Validated highway toll input utilities for Lab 7 fuzz testing."""


def parse_plate(plate):
    """Parse a plate like KA-05-AB-1234.

    Returns (state, district, number). Raises ValueError for malformed plates.
    """
    if not isinstance(plate, str):
        raise ValueError("plate must be a string")
    parts = plate.strip().upper().split("-")
    if len(parts) != 4:
        raise ValueError("plate must have four hyphen-separated parts")
    state, district_text, series, number_text = parts
    if len(state) != 2 or not state.isalpha():
        raise ValueError("state must contain exactly two letters")
    if not district_text.isdigit() or not 1 <= int(district_text) <= 99:
        raise ValueError("district must be a number from 1 to 99")
    if not series.isalpha() or not 1 <= len(series) <= 3:
        raise ValueError("series must contain 1 to 3 letters")
    if not number_text.isdigit() or not 1 <= int(number_text) <= 9999:
        raise ValueError("vehicle number must be from 1 to 9999")
    return state, int(district_text), int(number_text)


def trip_cost(text):
    """Calculate count x rate, rejecting malformed or negative values."""
    if not isinstance(text, str):
        raise ValueError("trip cost must be supplied as text such as '3x150'")
    parts = text.lower().split("x")
    if len(parts) != 2:
        raise ValueError("trip cost must contain exactly one 'x'")
    count_text, rate_text = (part.strip() for part in parts)
    if not count_text.isdigit() or not rate_text.isdigit():
        raise ValueError("trip count and rate must be non-negative integers")
    return int(count_text) * int(rate_text)


def axle_class(axles):
    """Classify valid axle counts: 2 = car, 3-4 = truck, 5+ = heavy."""
    if isinstance(axles, bool):
        raise ValueError("axle count must be an integer")
    if isinstance(axles, int):
        n = axles
    elif isinstance(axles, str) and axles.strip().isdigit():
        n = int(axles.strip())
    else:
        raise ValueError("axle count must be a positive whole number")
    if n < 2:
        raise ValueError("axle count must be at least 2")
    if n == 2:
        return "car"
    if n <= 4:
        return "truck"
    return "heavy"


def main():
    print("==== Running parse_plate ====")
    try:
        user_input = input("Enter a plate (e.g. KA-05-AB-1234): ")
        print("State, District and Number:", parse_plate(user_input))
    except ValueError as exc:
        print("Invalid plate:", exc)

    print("\n==== Running trip_cost ====")
    try:
        user_input = input("Enter trips x rate (e.g. 3x150): ")
        print("Trip Cost:", trip_cost(user_input))
    except ValueError as exc:
        print("Invalid trip cost:", exc)

    print("\n==== Running axle_class ====")
    try:
        user_input = input("Enter an axle count (e.g. 3): ")
        print("Vehicle Class:", axle_class(user_input))
    except ValueError as exc:
        print("Invalid axle count:", exc)


if __name__ == "__main__":
    main()
