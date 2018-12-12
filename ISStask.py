import requests
import json


def consume_ISS_api():
    html = requests.get("http://api.open-notify.org/iss-now.json")
    obj = json.loads(html.text)

    return obj['timestamp'], obj['iss_position']['latitude'], obj['iss_position']['longitude']


def get_weather_under_ISS(ISS_location):
    latitude = ISS_location[1]
    longitude = ISS_location[2]
    html = requests.get('http://api.openweathermap.org/data/2.5/weather?lat='+latitude+'&lon='+longitude+'&id=524901&APPID=ebb6b0d75ac8039bfcd5db95d399b515')
    obj = json.loads(html.text)

    return obj
        # obj['weather']['description'], obj['main']['temp'], obj['wind']
#['weather'][0], ['main'][0], ['wind'][0])
ISS_location = consume_ISS_api()
print(ISS_location)
print(get_weather_under_ISS(ISS_location)['weather'][0]['description'])
