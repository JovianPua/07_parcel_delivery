from parcel_fee import delivery_fee
import pytest



@pytest.mark.parametrize(
    "weight_grams, expected",
    [
        (1, 500),     # lowest weight
        (999, 500),   # just below the band edge
        (1000, 500),  # upper edge of the first band
    ],
)
def test_weight_in_first_band_costs_500(weight_grams, expected):
    # Act
    result = delivery_fee(weight_grams)

    # Assert
    assert result == expected



@pytest.mark.parametrize(
    "weight_grams, expected",
    [
        (1001, 1000),   # lower edge of the second band
        (10000, 1000),  # typical weight
        (20000, 1000),  # highest weight
    ],
)
def test_weight_in_second_band_costs_1000(weight_grams, expected):
    # Act
    result = delivery_fee(weight_grams)

    # Assert
    assert result == expected



@pytest.mark.parametrize(
    "weight_grams",
    [
        0,      # below the lowest weight
        -1,     # negative weight
        20001,  # above the highest weight
    ],
)
def test_weight_out_of_range_raises_value_error(weight_grams):
    # Act / Assert
    with pytest.raises(ValueError):
        delivery_fee(weight_grams)



@pytest.mark.parametrize(
    "weight_grams",
    [
        "500",   # string
        500.5,   # float
        True,    # bool is not a valid int
        None,    # None
    ],
)
def test_invalid_type_raises_type_error(weight_grams):
    # Act / Assert
    with pytest.raises(TypeError):
        delivery_fee(weight_grams)
