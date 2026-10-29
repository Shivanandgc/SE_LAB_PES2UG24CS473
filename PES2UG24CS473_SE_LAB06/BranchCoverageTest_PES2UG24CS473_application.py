import pytest

from highway_toll import toll_for, toll_charge, pass_advice


@pytest.mark.parametrize("axles", [1, 0, -1])
def test_axles_below_minimum_raise(axles):
    with pytest.raises(ValueError, match="invalid axle count"):
        toll_for(axles, False, False)


@pytest.mark.parametrize(
    "axles, expected",
    [(2, 100), (3, 150), (4, 250), (5, 400)],
)
def test_known_and_unknown_axles(axles, expected):
    assert toll_for(axles, False, False) == expected


@pytest.mark.parametrize(
    "is_peak, expected",
    [(False, 100), (True, 125)],
)
def test_peak_and_non_peak_branches(is_peak, expected):
    assert toll_for(2, is_peak, False) == expected


@pytest.mark.parametrize(
    "has_fastag, expected",
    [(False, 100), (True, 90)],
)
def test_two_axle_fastag_branches(has_fastag, expected):
    assert toll_for(2, False, has_fastag) == expected


@pytest.mark.parametrize(
    "axles, expected",
    [(3, 150), (3, 142.5), (5, 400), (5, 380)],
)
def test_other_axles_fastag_paths(axles, expected):
    has_fastag = expected in (142.5, 380)
    assert toll_for(axles, False, has_fastag) == expected


@pytest.mark.parametrize(
    "vehicle, expected",
    [("ambulance", 0), ("fire_engine", 0), ("car", 100)],
)
def test_exempt_and_non_exempt_vehicles(vehicle, expected):
    assert toll_charge(vehicle, 2, False, False) == expected


@pytest.mark.parametrize(
    "trips, pass_price, expected",
    [
        ([(False, False), (False, False)], 150, "buy_pass"),
        ([(False, False)], 100, "either"),
        ([(False, False)], 101, "pay_per_trip"),
        ([], 0, "either"),
    ],
)
def test_all_pass_advice_outcomes(trips, pass_price, expected):
    assert pass_advice(trips, 2, pass_price) == expected
