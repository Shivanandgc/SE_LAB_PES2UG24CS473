"""Hypothesis tests for all three highway toll input functions."""
import pytest
from hypothesis import given, strategies as st

from highway_toll import axle_class, parse_plate, trip_cost


@given(st.text())
def test_parse_plate_accepts_only_valid_structure_or_reports_validation_error(value):
    try:
        result = parse_plate(value)
    except ValueError:
        return
    assert isinstance(result, tuple) and len(result) == 3
    assert len(result[0]) == 2 and result[0].isalpha()
    assert isinstance(result[1], int) and 1 <= result[1] <= 99
    assert isinstance(result[2], int) and 1 <= result[2] <= 9999


@given(
    state=st.text(alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", min_size=2, max_size=2),
    district=st.integers(min_value=1, max_value=99),
    series=st.text(alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", min_size=1, max_size=3),
    number=st.integers(min_value=1, max_value=9999),
)
def test_parse_plate_valid_plates(state, district, series, number):
    plate = f"{state.lower()}-{district:02d}-{series.lower()}-{number:04d}"
    assert parse_plate(plate) == (state, district, number)


@given(value=st.one_of(st.none(), st.integers(), st.lists(st.text())))
def test_parse_plate_rejects_non_string_inputs(value):
    with pytest.raises(ValueError):
        parse_plate(value)


@given(st.text())
def test_trip_cost_never_returns_negative_for_valid_or_invalid_text(value):
    try:
        result = trip_cost(value)
    except ValueError:
        return
    assert isinstance(result, int) and result >= 0


@given(count=st.integers(min_value=0, max_value=100000), rate=st.integers(min_value=0, max_value=100000))
def test_trip_cost_calculates_valid_values(count, rate):
    assert trip_cost(f"{count}x{rate}") == count * rate


@given(value=st.one_of(st.none(), st.integers(), st.lists(st.integers()), st.booleans()))
def test_trip_cost_rejects_non_string_inputs(value):
    with pytest.raises(ValueError):
        trip_cost(value)


@given(value=st.one_of(st.none(), st.floats(allow_nan=True, allow_infinity=True), st.booleans(), st.lists(st.integers())))
def test_axle_class_rejects_invalid_types(value):
    with pytest.raises(ValueError):
        axle_class(value)


@given(axles=st.integers(min_value=2, max_value=1000))
def test_axle_class_returns_one_of_three_classes(axles):
    result = axle_class(axles)
    assert result in {"car", "truck", "heavy"}


@given(axles=st.integers(min_value=2, max_value=1000))
def test_axle_class_matches_classification_rules(axles):
    expected = "car" if axles == 2 else "truck" if axles <= 4 else "heavy"
    assert axle_class(axles) == expected


@given(axles=st.integers(min_value=-1000, max_value=1))
def test_axle_class_rejects_axle_counts_below_two(axles):
    with pytest.raises(ValueError):
        axle_class(axles)
