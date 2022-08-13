import requests
import datetime


api_connection = requests.get(url="http://api.open-notify.org/iss-now.json")
api_connection.raise_for_status()

data = api_connection.json()
print(data)
