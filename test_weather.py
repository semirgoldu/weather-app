"""Tests for the weather module."""
from weather import get_weather, get_forecast


def test_returns_correct_location():
    result = get_weather("Turkey")
    assert result["location"] == "Turkey"


def test_returns_temperature():
    result = get_weather("Turkey")
    assert result["temperature_c"] == 20


def test_returns_condition():
    result = get_weather("Turkey")
    assert result["condition"] == "Sunny"


def test_works_with_any_location():
    result = get_weather("Germany")
    assert result["location"] == "Germany"


def test_returns_humidity():
    result = get_weather("Turkey")
    assert result["unhumidity_%"] == 65


def test_returns_sun_strength():
    result = get_weather("Turkey")
    assert result["sun_strength"] == "high"


def test_forecast_returns_three_days():
    result = get_forecast("Turkey")
    assert len(result) == 3


def test_forecast_has_required_fields():
    result = get_forecast("Turkey")
    for day in result:
        assert "day" in day
        assert "temperature_c" in day
        assert "condition" in day
