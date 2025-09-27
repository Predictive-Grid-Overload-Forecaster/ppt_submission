import requests

url = "https://calendarific.com/api/v2/holidays"
params = {
    "api_key": "3YqlfOm204SMAg5W55cRIQ0gqoxCQcpB",
    "country": "IN",
    "location": "Delhi",
    "year": 2025
}
response = requests.get(url, params=params)
data = response.json()
print(data)
