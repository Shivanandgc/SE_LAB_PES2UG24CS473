"""Highway toll utilities used in the SE Lab 7 fuzz-testing exercise."""

BASE_TOLL = {2: 100, 3: 150, 4: 250}
EXEMPT = ("ambulance", "fire_engine")


def _validate_axles(axles):
    """Validate axle count as a positive whole number."""
    if isinstance(axles, bool):
        raise ValueError("axles must be a positive integer")
    try:
        value = int(axles)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError("axles must be a positive integer") from exc
    if isinstance(axles, float) and not axles.is_integer():
        raise ValueError("axles must be a whole number")
    if isinstance(axles, str) and str(value) != axles.strip():
        raise ValueError("axles must be a whole number")
    if value < 1:
        raise ValueError("axles must be a positive integer")
    return value


def _validate_boolean(value, name):
    if not isinstance(value, bool):
        raise ValueError(f"{name} must be a boolean")
    return value


def toll_for(axles, is_peak, has_fastag):
    """Calculate toll from axle count, peak status, and FASTag status."""
    axles = _validate_axles(axles)
    is_peak = _validate_boolean(is_peak, "is_peak")
    has_fastag = _validate_boolean(has_fastag, "has_fastag")

    base = BASE_TOLL.get(axles, 400)
    if is_peak:
        base *= 1.25
    if has_fastag:
        base *= 0.9 if axles == 2 else 0.95
    return round(base, 2)


def toll_charge(vehicle, axles, is_peak, has_fastag):
    """Return zero for emergency vehicles; otherwise calculate the toll."""
    if not isinstance(vehicle, str) or not vehicle.strip():
        raise ValueError("vehicle must be a non-empty string")
    if vehicle.strip().lower() in EXEMPT:
        return 0
    return toll_for(axles, is_peak, has_fastag)


def pass_advice(trips, axles, pass_price):
    """Recommend a pass when its price is below the sum of trip tolls."""
    axles = _validate_axles(axles)
    if isinstance(pass_price, (bool, str, bytes)):
        raise ValueError("pass_price must be a finite non-negative number")
    try:
        pass_price = float(pass_price)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError("pass_price must be a finite non-negative number") from exc
    if not (pass_price >= 0 and pass_price < float("inf")):
        raise ValueError("pass_price must be a finite non-negative number")

    if trips is None or isinstance(trips, (str, bytes)):
        raise ValueError("trips must be an iterable of trip pairs")
    try:
        iterator = iter(trips)
    except TypeError as exc:
        raise ValueError("trips must be iterable") from exc

    total_cost = 0.0
    for trip in iterator:
        if isinstance(trip, (str, bytes)):
            raise ValueError("each trip must be a pair of booleans")
        try:
            is_peak, has_fastag = trip
        except (TypeError, ValueError) as exc:
            raise ValueError("each trip must contain exactly two values") from exc
        total_cost += toll_for(axles, is_peak, has_fastag)

    if total_cost > pass_price:
        return "buy_pass"
    if total_cost == pass_price:
        return "either"
    return "pay_per_trip"


def main():
    """Small deterministic demonstration for the lab's initial/final run."""
    print("==== Highway Toll Calculator ====")
    examples = [
        ("Car, regular, FASTag", toll_for(2, False, True)),
        ("3-axle truck, peak, FASTag", toll_for(3, True, True)),
        ("Ambulance exemption", toll_charge("ambulance", 2, False, False)),
        ("Pass advice", pass_advice([(False, False), (True, True)], 2, 250)),
    ]
    for label, result in examples:
        print(f"{label}: {result}")


if __name__ == "__main__":
    main()
