"""Tests for the weather module."""
from weather import get_weather


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
