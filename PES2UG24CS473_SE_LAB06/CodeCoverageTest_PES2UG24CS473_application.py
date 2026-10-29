import pytest

from highway_toll import toll_for, toll_charge, pass_advice


def test_invalid_axle_count():
    with pytest.raises(ValueError, match="invalid axle count"):
        toll_for(1, False, False)


@pytest.mark.parametrize(
    "axles, expected",
    [(2, 100), (3, 150), (4, 250), (5, 400)],
)
def test_base_toll(axles, expected):
    assert toll_for(axles, False, False) == expected


def test_peak_surcharge():
    assert toll_for(2, True, False) == 125


def test_fastag_two_axle_discount():
    assert toll_for(2, False, True) == 90


@pytest.mark.parametrize(
    "axles, expected",
    [(3, 142.5), (4, 237.5), (5, 380)],
)
def test_fastag_other_axles(axles, expected):
    assert toll_for(axles, False, True) == expected


def test_peak_and_fastag_combined():
    assert toll_for(2, True, True) == 112.5


@pytest.mark.parametrize("vehicle", ["ambulance", "fire_engine"])
def test_exempt_vehicles(vehicle):
    assert toll_charge(vehicle, 2, True, False) == 0


def test_regular_vehicle_is_charged():
    assert toll_charge("car", 2, False, False) == 100


def test_buy_pass():
    assert pass_advice(
        [(False, False), (False, False)], 2, 150
    ) == "buy_pass"


def test_either_option():
    assert pass_advice([(False, False)], 2, 100) == "either"


def test_pay_per_trip():
    assert pass_advice([(False, False)], 2, 101) == "pay_per_trip"


def test_empty_trip_list():
    assert pass_advice([], 2, 0) == "either"
