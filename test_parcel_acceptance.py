from parcel_acceptance import is_parcel_accepted
import pytest



@pytest.mark.parametrize(
    "weight_grams, length_cm",
    [
        (1, 1),        # smallest parcel
        (10000, 100),  # typical parcel
        (20000, 100),  # heaviest allowed weight
        (10000, 200),  # longest allowed length
    ],
)
def test_parcel_within_limits_is_accepted(weight_grams, length_cm):
    # Act
    result = is_parcel_accepted(weight_grams, length_cm)

    # Assert
    assert result is True



@pytest.mark.parametrize(
    "weight_grams, length_cm",
    [
        (0, 100),      # zero weight
        (10000, 0),    # zero length
        (20001, 100),  # too heavy
        (10000, 201),  # too long
    ],
)
def test_parcel_outside_limits_is_rejected(weight_grams, length_cm):
    # Act
    result = is_parcel_accepted(weight_grams, length_cm)

    # Assert
    assert result is False



@pytest.mark.parametrize(
    "weight_grams, length_cm",
    [
        (-1, 100),     # negative weight
        (10000, -1),   # negative length
    ],
)
def test_negative_measurement_raises_value_error(weight_grams, length_cm):
    # Act / Assert
    with pytest.raises(ValueError):
        is_parcel_accepted(weight_grams, length_cm)



@pytest.mark.parametrize(
    "weight_grams, length_cm",
    [
        ("10000", 100),  # weight is a string
        (10000, 100.5),  # length is a float
        (True, 100),     # weight is a bool
        (10000, None),   # length is None
    ],
)
def test_invalid_type_raises_type_error(weight_grams, length_cm):
    # Act / Assert
    with pytest.raises(TypeError):
        is_parcel_accepted(weight_grams, length_cm)
