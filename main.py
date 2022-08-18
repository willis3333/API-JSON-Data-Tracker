import requests
import datetime

#set datetime variables
time_now = datetime.datetime.now()
todays_date = time_now.strftime('%Y-%m-%d')
current_hour = time_now.hour
# Set my long, lat variables
MY_LAT = "44.5098735"
MY_LON = "-72.9760819"
# Get iss data from API
iss_api_connection = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_api_connection.raise_for_status()
iss_data = iss_api_connection.json()
print(iss_data)
print(iss_data['iss_position'])
iss_lat = iss_data['iss_position']['latitude']
iss_long = iss_data['iss_position']['longitude']
# Get sunset/ sunrise data
url = "https://sunrise-sunset-times.p.rapidapi.com/getSunriseAndSunset"
querystring = {"date":todays_date,"latitude":MY_LAT,"longitude":MY_LON,"timeZoneId":"America/New_York"}
headers = {
	"X-RapidAPI-Key": "137222575fmsh12e3a03e0483ff0p1d451ejsn1e7a54e95f10",
	"X-RapidAPI-Host": "sunrise-sunset-times.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
sunset_hour = int(response.json()['sunset'][11:13])
sunrise_hour = int(response.json()['sunrise'][11:13])


# Check if sun is down at current hour (for ISS visibility)
def sun_down():
	if current_hour < sunrise_hour or current_hour > sunset_hour:
		return True
	else:
		return False


def iss_visible():
	if float(MY_LAT)-5 <= float(iss_lat) <= float(MY_LAT)+5 and float(MY_LON)-5 <= float(iss_long) >= float(MY_LON)+5:
		return True
	else:
		return False


if iss_visible() and sun_down():
	print(f'You can see the ISS in the night sky')
else:
	if iss_visible():
		print('iss is visible')
	else:
		print('iss not visible')

	if sun_down():
		print('sun is down')
	else:
		print('sun is up')

# TODO: Add SMS message notification