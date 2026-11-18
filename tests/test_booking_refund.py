import pytest

from booking_refund import is_refundable


@pytest.mark.parametrize(
    "hours_before_checkin, flexible_rate",
    [
        (48, True),
        (49, True),
        (100, True),
    ]
)
def test_refundable_booking_valid(
    hours_before_checkin,
    flexible_rate
):
    # Arrange

    # Act
    result = is_refundable(
        hours_before_checkin,
        flexible_rate
    )

    # Assert
    assert result is True


@pytest.mark.parametrize(
    "hours_before_checkin, flexible_rate",
    [
        (47, True),
        (0, True),
        (100, False),
        (48, False),
    ]
)
def test_non_refundable_booking_invalid(
    hours_before_checkin,
    flexible_rate
):
    # Arrange

    # Act
    result = is_refundable(
        hours_before_checkin,
        flexible_rate
    )

    # Assert
    assert result is False


def test_negative_hours_before_checkin_invalid():
    # Arrange
    hours_before_checkin = -1
    flexible_rate = True

    # Act & Assert
    with pytest.raises(ValueError):
        is_refundable(
            hours_before_checkin,
            flexible_rate
        )


@pytest.mark.parametrize(
    "hours_before_checkin, flexible_rate",
    [
        ("48", True),
        (48.5, True),
        (None, True),
        (True, True),
        (48, 1),
        (48, "True"),
        (48, None),
    ]
)
def test_invalid_type_invalid(
    hours_before_checkin,
    flexible_rate
):
    # Arrange

    # Act & Assert
    with pytest.raises(TypeError):
        is_refundable(
            hours_before_checkin,
            flexible_rate
        )