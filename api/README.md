# 🚀 Delhi Data APIs: Quick Usage Guide

Easily fetch **holidays**, **weather**, and **carbon intensity** for Delhi using these APIs. Each section includes a sample JavaScript fetch snippet.

---

## 1️⃣ Calendarific API – Holidays & Observances

**Endpoint:**  
`https://calendarific.com/api/v2/holidays?api_key=YOUR_API_KEY&country=IN&location=Delhi&year=2025`

**Returns:**  
- 🗓️ Public, bank, and regional holidays  
- 🛑 Observances (weekends, festivals, special days)

**Sample Fetch:**
```javascript
const calendarificKey = "3YqlfOm204SMAg5W55cRIQ0gqoxCQcpB
";
fetch(`https://calendarific.com/api/v2/holidays?api_key=${calendarificKey}&country=IN&location=Delhi&year=2025`)
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(console.error);
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

**Sample Fetch:**
```javascript
const weatherKey = "10f64e4346c64f569a2164222252609";
fetch(`https://api.weatherapi.com/v1/current.json?key=${weatherKey}&q=Delhi`)
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(console.error);
```

---

## 3️⃣ Electricity Maps – Carbon Intensity

**Endpoint:**  
`https://api.electricitymaps.com/v3/carbon-intensity/past?datetime=YYYY-MM-DD+HH%3AMM`

**Returns:**  
- ⚡ Carbon intensity (gCO₂/kWh)  
- 🔄 Historical, real-time, and forecast data

**Sample Fetch:**
```javascript
const electricityMapsKey = "HrPKJcgjOjMZt6yQn3N7";
fetch(`https://api.electricitymaps.com/v3/carbon-intensity/past?datetime=2025-09-25+17%3A06`, {
  headers: { "auth-token": electricityMapsKey }
})
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(console.error);
```

---

## 📝 Notes

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
