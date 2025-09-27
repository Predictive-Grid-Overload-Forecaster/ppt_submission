## 🔹 Event & Weather Feature Mapping  

| **Feature**        | **Type**     | **Encoding Method**         | **Example Value**       | **Notes** |
|---------------------|--------------|-----------------------------|-------------------------|-----------|
| **Temperature**     | Numeric      | Scaled (0–1)                | 35°C → 0.7              | Directly impacts AC usage |
| **Humidity**        | Numeric      | Scaled (0–1)                | 70% → 0.7               | High humidity = more cooling load |
| **Solar Radiation** | Numeric      | Scaled (0–1)                | 200 W/m² → 0.5          | Impacts solar power generation |
| **Wind Speed**      | Numeric      | Scaled (0–1)                | 5 km/h → 0.2            | Secondary factor, supports renewables |
| **Precipitation**   | Numeric      | Binary (0/1)                | Rain = 1, No Rain = 0   | Heavy rain lowers outdoor activity & solar output |
| **Day of Week**     | Categorical  | One-hot (Mon–Sun)           | Sunday = 1              | Captures weekday vs weekend demand |
| **Hour of Day**     | Categorical  | One-hot (0–23)              | 18:00 = 1               | Captures daily peak cycles |
| **Holiday Flag**    | Categorical  | One-hot (Holiday/Normal)    | Holiday = 1             | Lower industry demand, higher residential |
| **Festival Event**  | Categorical  | One-hot (Festival/Normal)   | Diwali = 1              | Demand spikes due to lighting/celebrations |
| **City Event**      | Categorical  | One-hot (Event/Normal)      | Cricket Match = 1       | Zone-specific unusual spikes |
| **Lag Demand**      | Numeric      | Raw + rolling avg (t-1, t-24, t-168) | Yesterday’s 6PM = 3200 MW | Strong predictor of short-term demand |


## ⚡ Event & Weather Feature Mapping

Our demand forecasting model uses not only past consumption but also **external factors** that shape Delhi’s electricity usage:

### 🗓️ 1. Calendarific (Holidays & Events)
- **Features:** `is_holiday`, `holiday_type`, `festival_flag`  
- **Why:** Demand shifts during holidays & festivals.  
  - Weekends/holidays → lower office load, higher residential use.  
  - Festivals (Diwali, Eid) → sharp evening demand spikes.  

### 🌦️ 2. WeatherAPI (Weather Conditions)
- **Features:** `temperature`, `humidity`, `precipitation`, `cloud_cover`, `wind_speed`  
- **Why:** Weather heavily impacts demand.  
  - High temp & humidity → more AC usage.  
  - Rain/clouds → lower solar output → grid demand ↑.  

### ⚡ 3. Electricity Maps (Carbon Intensity)
- **Feature:** `carbon_intensity (gCO₂/kWh)`  
- **Why:** Shows how clean/polluting current supply is.  
  - Same demand can be low-carbon (solar/wind) or high-carbon (coal).  
