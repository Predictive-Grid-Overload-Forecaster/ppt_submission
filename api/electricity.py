import requests

url = "https://api.electricitymaps.com/v3/carbon-intensity/latest"
params = {"zone": "IN"} 
headers = {"Authorization": "HrPKJcgjOjMZt6yQn3N7"}
response = requests.get(url, params=params, headers=headers)
data = response.json()
print(data)
