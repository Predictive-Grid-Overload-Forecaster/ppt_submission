# 📚 API Usage Guide with Fetch Examples

This project fetches holidays, weather, and carbon intensity data for Delhi using three APIs.

---

## 1. Calendarific API – Holidays & Observances

**Endpoint:**
https://calendarific.com/api/v2/holidays?&api_key=YOUR_API_KEY&country=IN&location=Delhi&year=2025

p

**Data You Get:**
- 🗓️ Public, bank, and regional holidays
- 🛑 Observances like weekends and special days

**Fetch Example (JS):**
```javascript
const calendarificKey = "3YqlfOm204SMAg5W55cRIQ0gqoxCQcpB";
fetch(`https://calendarific.com/api/v2/holidays?&api_key=${calendarificKey}&country=IN&location=Delhi&year=2025`)
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));

---

## 2. WeatherAPI – Current Weather in Delhi

**Endpoint:**
https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=Delhi


Data You Get:

🌡️ Temperature (°C/°F)
🌬️ Wind speed & direction
☁️ Cloud cover
🌧️ Precipitation info
🌅 Sunrise & sunset times


Fetch Example (JS):

const weatherKey = "10f64e4346c64f569a2164222252609";
fetch(`https://api.weatherapi.com/v1/current.json?key=${weatherKey}&q=Delhi`)
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));


## 3. Electricity Maps – Carbon Intensity Data


** Endpoint: **

https://api.electricitymaps.com/v3/carbon-intensity/past?datetime=2025-09-25+17%3A06

Data You Get:
⚡ Carbon intensity in gCO₂/kWh
🔄 Historical, real-time, and forecast data

Fetch Example (JS):
const electricityMapsKey = "HrPKJcgjOjMZt6yQn3N7";
fetch(`https://api.electricitymaps.com/v3/carbon-intensity/past?datetime=2025-09-25+17%3A06`, {
  headers: {
    "auth-token": electricityMapsKey
  }
})
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));


