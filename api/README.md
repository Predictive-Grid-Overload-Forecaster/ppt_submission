# 🚀 Delhi Data APIs: Quick Usage Guide

Easily fetch **holidays**, **weather**, and **carbon intensity** for Delhi using these FastAPI endpoints. Each section includes a sample request and response.

---

## 1️⃣ `/holidays` – Delhi Holidays & Observances

**Endpoint:**  
`GET /holidays?year=2025`

**Returns:**  
- 🗓️ Public, bank, and regional holidays  
- 🛑 Observances (weekends, festivals, special days)

**Sample Request (Python):**
```python
import requests

url = "http://localhost:8000/holidays?year=2025"
response = requests.get(url)
print(response.json())
```

**Sample Response:**
```json
{
  "year": 2025,
  "location": "Delhi",
  "holidays": [
    {"date": "2025-01-26", "name": "Republic Day", "type": "public"},
    {"date": "2025-08-15", "name": "Independence Day", "type": "public"},
    // ...more holidays...
  ]
}
```

---

## 2️⃣ `/weather` – Delhi Weather

**Endpoint:**  
`GET /weather`

**Returns:**  
- 🌡️ Temperature (°C/°F)  
- 🌬️ Wind speed & direction  
- ☁️ Cloud cover  
- 🌧️ Precipitation  
- 🌅 Sunrise & sunset times

**Sample Request (Python):**
```python
import requests

url = "http://localhost:8000/weather"
response = requests.get(url)
print(response.json())
```

**Sample Response:**
```json
{
  "location": "Delhi",
  "temperature_c": 32.5,
  "wind_kph": 12.3,
  "wind_dir": "NW",
  "cloud": 40,
  "precip_mm": 0.0,
  "sunrise": "06:10",
  "sunset": "18:45"
}
```

---

## 3️⃣ `/carbon-intensity` – Carbon Intensity

**Endpoint:**  
`GET /carbon-intensity?datetime=2025-09-25T17:06`

**Returns:**  
- ⚡ Carbon intensity (gCO₂/kWh)  
- 🔄 Historical, real-time, and forecast data

**Sample Request (Python):**
```python
import requests

url = "http://localhost:8000/carbon-intensity?datetime=2025-09-25T17:06"
response = requests.get(url)
print(response.json())
```

**Sample Response:**
```json
{
  "datetime": "2025-09-25T17:06",
  "location": "Delhi",
  "carbon_intensity_gco2_per_kwh": 620
}
```

---

## 📝 Notes

- All endpoints are for **Delhi, India** and **year 2025** (where applicable).
- For more details, see the FastAPI docs or `/docs` endpoint.

---

## 📦 Quick Reference

| Endpoint                | Data Type         | Auth Required | Example URL                                  |
|-------------------------|------------------|--------------|----------------------------------------------|
| `/holidays`             | Holidays         | No           | `/holidays?year=2025`                        |
| `/weather`              | Weather          | No           | `/weather`                                   |
| `/carbon-intensity`     | Carbon Intensity | No           | `/carbon-intensity?datetime=2025-09-25T17:06`|

---

Happy coding! 🎉