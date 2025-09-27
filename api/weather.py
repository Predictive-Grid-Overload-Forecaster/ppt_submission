import requests


api_key = "10f64e4346c64f569a2164222252609"
city = "Delhi"
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

response = requests.get(url)

data = response.json()
print(f"Location: {data['location']['name']}, {data['location']['country']}")
print(f"Temperature: {data['current']['temp_c']}°C")
print(f"Condition: {data['current']['condition']['text']}")
print(f"Wind: {data['current']['wind_kph']} kph")
