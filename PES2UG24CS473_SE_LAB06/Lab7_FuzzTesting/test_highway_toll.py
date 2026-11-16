"""Hypothesis fuzz tests for highway_toll.py."""
import math

import pytest
from hypothesis import given, strategies as st

from highway_toll import pass_advice, toll_charge, toll_for


@given(
    axles=st.integers(min_value=1, max_value=100),
    is_peak=st.booleans(),
    has_fastag=st.booleans(),
)
def test_toll_for_valid_inputs_is_finite_and_non_negative(axles, is_peak, has_fastag):
    result = toll_for(axles, is_peak, has_fastag)
    assert isinstance(result, float)
    assert math.isfinite(result)
    assert result >= 0


@given(
    axles=st.integers(min_value=1, max_value=100),
    is_peak=st.booleans(),
    has_fastag=st.booleans(),
)
def test_toll_for_follows_rate_and_discount_rules(axles, is_peak, has_fastag):
    expected = {2: 100, 3: 150, 4: 250}.get(axles, 400)
    if is_peak:
        expected *= 1.25
    if has_fastag:
        expected *= 0.9 if axles == 2 else 0.95
    assert toll_for(axles, is_peak, has_fastag) == round(expected, 2)


@given(value=st.one_of(st.none(), st.text(), st.floats(allow_nan=True, allow_infinity=True), st.booleans()))
def test_toll_for_rejects_malformed_axle_values(value):
    if isinstance(value, str):
        try:
            parsed = int(value)
            valid = parsed >= 1 and str(parsed) == value.strip()
        except ValueError:
            valid = False
    else:
        valid = isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value) and value >= 1 and float(value).is_integer()
    if valid:
        assert toll_for(value, False, False) >= 0
    else:
        with pytest.raises(ValueError):
            toll_for(value, False, False)


@given(value=st.one_of(st.none(), st.text(), st.integers(), st.lists(st.booleans(), max_size=3)))
def test_toll_for_rejects_non_boolean_flags(value):
    if isinstance(value, bool):
        return
    with pytest.raises(ValueError):
        toll_for(2, value, False)
    with pytest.raises(ValueError):
        toll_for(2, False, value)


@given(vehicle=st.sampled_from(["ambulance", "fire_engine", " AMBULANCE ", "Fire_Engine"]))
def test_emergency_vehicles_are_exempt(vehicle):
    assert toll_charge(vehicle, None, "invalid", object()) == 0


@given(
    vehicle=st.text(min_size=1).filter(lambda value: value.strip().lower() not in {"ambulance", "fire_engine"}),
    axles=st.integers(min_value=1, max_value=100),
    is_peak=st.booleans(),
    has_fastag=st.booleans(),
)
def test_non_exempt_vehicle_uses_toll_for(vehicle, axles, is_peak, has_fastag):
    assert toll_charge(vehicle, axles, is_peak, has_fastag) == toll_for(axles, is_peak, has_fastag)


@given(
    trips=st.lists(st.tuples(st.booleans(), st.booleans()), max_size=30),
    axles=st.integers(min_value=1, max_value=100),
)
def test_pass_advice_returns_a_valid_recommendation(trips, axles):
    assert pass_advice(trips, axles, 10000) in {"buy_pass", "either", "pay_per_trip"}


@given(
    trips=st.lists(st.tuples(st.booleans(), st.booleans()), max_size=20),
    axles=st.integers(min_value=1, max_value=100),
)
def test_pass_advice_compares_pass_price_with_trip_total(trips, axles):
    total = sum(toll_for(axles, peak, fastag) for peak, fastag in trips)
    assert pass_advice(trips, axles, total) == "either"
    assert pass_advice(trips, axles, total + 1) == "pay_per_trip"
    if total > 0:
        assert pass_advice(trips, axles, total - 1) == "buy_pass"


@given(value=st.one_of(st.none(), st.text(), st.floats(allow_nan=True, allow_infinity=True), st.booleans()))
def test_pass_advice_rejects_invalid_pass_prices(value):
    valid = isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value) and value >= 0
    if valid:
        assert pass_advice([], 2, value) == "either"
    else:
        with pytest.raises(ValueError):
            pass_advice([], 2, value)


@given(trips=st.one_of(st.none(), st.text(), st.integers(), st.dictionaries(st.text(), st.integers())))
def test_pass_advice_rejects_non_iterable_or_string_trips(trips):
    if trips is not None and not isinstance(trips, (str, bytes)) and hasattr(trips, "__iter__"):
        return
    with pytest.raises(ValueError):
        pass_advice(trips, 2, 100)


@given(trip=st.one_of(st.text(), st.integers(), st.lists(st.integers(), max_size=4)))
def test_pass_advice_rejects_malformed_trip_items(trip):
    with pytest.raises(ValueError):
        pass_advice([trip], 2, 100)
