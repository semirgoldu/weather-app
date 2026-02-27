# Weather App

A simple Python function that returns the weather for a given location.

## Usage

```python
from weather import get_weather

weather = get_weather("Turkey")
print(weather)
# {'location': 'Turkey', 'temperature_c': 20, 'condition': 'Sunny'}
```

## Run locally

```bash
python weather.py
pytest test_weather.py
```
