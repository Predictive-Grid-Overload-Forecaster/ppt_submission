# 🚀 Delhi Data APIs: Quick Usage Guide

Easily fetch **holidays**, **weather**, and **carbon intensity** for Delhi using these APIs. Each section includes a sample Python `requests` snippet.

---

## 1️⃣ Calendarific API – Holidays & Observances

**Endpoint:**  
`https://calendarific.com/api/v2/holidays?api_key=YOUR_API_KEY&country=IN&location=Delhi&year=2025`

**Returns:**  
- 🗓️ Public, bank, and regional holidays  
- 🛑 Observances (weekends, festivals, special days)

**Sample Fetch (Python):**
```python
import requests

calendarific_key = "YOUR_API_KEY"
url = f"https://calendarific.com/api/v2/holidays?api_key={calendarific_key}&country=IN&location=Delhi&year=2025"
response = requests.get(url)
print(response.json())
```

---

## 2️⃣ WeatherAPI – Delhi Weather

**Endpoint:**  
`https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=Delhi`

**Returns:**  
- 🌡️ Temperature (°C/°F)  
- 🌬️ Wind speed & direction  
- ☁️ Cloud cover  
- 🌧️ Precipitation  
- 🌅 Sunrise & sunset times

**Sample Fetch (Python):**
```python
import requests

weather_key = "YOUR_API_KEY"
url = f"https://api.weatherapi.com/v1/current.json?key={weather_key}&q=Delhi"
response = requests.get(url)
print(response.json())
```

---

## 3️⃣ Electricity Maps – Carbon Intensity

**Endpoint:**  
`https://api.electricitymaps.com/v3/carbon-intensity/past?datetime=YYYY-MM-DD+HH%3AMM`

**Returns:**  
- ⚡ Carbon intensity (gCO₂/kWh)  
- 🔄 Historical, real-time, and forecast data

**Sample Fetch (Python):**
```python
import requests

electricity_maps_key = "YOUR_API_KEY"
headers = {"auth-token": electricity_maps_key}
url = "https://api.electricitymaps.com/v3/carbon-intensity/past?datetime=2025-09-25+17%3A06"
response = requests.get(url, headers=headers)
print(response.json())
```

---

## 📝 Notes

- Replace `"YOUR_API_KEY"` with your actual API keys.
- All endpoints are for **Delhi, India** and **year 2025** (where applicable).
- For more details, see each API’s official documentation.

---

## 📦 Quick Reference

| API                | Data Type         | Auth Required | Docs Link                                      |
|--------------------|------------------|--------------|------------------------------------------------|
| Calendarific       | Holidays         | Yes          | [calendarific.com](https://calendarific.com/)  |
| WeatherAPI         | Weather          | Yes          | [weatherapi.com](https://weatherapi.com/)      |
| Electricity Maps   | Carbon Intensity | Yes          | [electricitymaps.com](https://electricitymaps.com/) |

---

Happy coding! 🎉