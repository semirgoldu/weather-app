"""A simple weather function."""


def get_weather(location: str) -> dict:
    """
    Returns the current weather for a given location.

    Args:
        location: A city or country name e.g. "Turkey"

    Returns:
        A dictionary with temperature and condition.
    """
    return {
        "location": location,
        "temperature_c": 20,
        "condition": "Sunny",
    }


def get_forecast(location: str) -> list:
    """
    Returns a 3-day forecast for a given location.

    Args:
        location: A city or country name e.g. "Turkey"

    Returns:
        A list of daily forecasts.
    """
    return [
        {"day": "Monday",    "temperature_c": 20, "condition": "Sunny"},
        {"day": "Tuesday",   "temperature_c": 18, "condition": "Cloudy"},
        {"day": "Wednesday", "temperature_c": 15, "condition": "Rainy"},
    ]


if __name__ == "__main__":
    weather = get_weather("Turkey")
    print(f"Weather in {weather['location']}:")
    print(f"  Temperature : {weather['temperature_c']}°C")
    print(f"  Condition   : {weather['condition']}")
