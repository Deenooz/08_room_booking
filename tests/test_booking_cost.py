import pytest

from src.booking_cost import calculate_booking_cost


@pytest.mark.parametrize(
    "nights, nightly_rate_cents, expected_result",
    [
        (1, 1000, 1000),
        (30, 1000, 30000),
        (5, 1000, 5000),
        (5, 0, 0),
        (1, 0, 0),
        (15, 2000, 30000),
        (7, 1000, 7000),
        (8, 1000, 8000),
        (30, 500, 15000),
    ]
)
def test_valid_booking_valid(
    nights,
    nightly_rate_cents,
    expected_result
):
    # Arrange

    # Act
    result = calculate_booking_cost(
        nights,
        nightly_rate_cents
    )

    # Assert
    assert result == expected_result


@pytest.mark.parametrize(
    "nights, nightly_rate_cents",
    [
        (0, 1000),
        (31, 1000),
        (5, -1),
    ]
)
def test_invalid_range_invalid(
    nights,
    nightly_rate_cents
):
    # Arrange

    # Act & Assert
    with pytest.raises(ValueError):
        calculate_booking_cost(
            nights,
            nightly_rate_cents
        )


@pytest.mark.parametrize(
    "nights, nightly_rate_cents",
    [
        ("5", 1000),
        (5.5, 1000),
        (None, 1000),
        (True, 1000),
        (5, "1000"),
        (5, 1000.5),
        (5, None),
        (5, False),
    ]
)
def test_invalid_type_invalid(
    nights,
    nightly_rate_cents
):
    # Arrange

    # Act & Assert
    with pytest.raises(TypeError):
        calculate_booking_cost(
            nights,
            nightly_rate_cents
        )