from nose.tools import assert_is_not_none
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin
import requests
from unittest.mock import Mock, patch
import ISStask
import json



# def get_ISS_data():
#     response = requests.get(ISS_DATA_URL)
#     if response.ok:
#         return response
#     else:
#         return None
#

# def get_WEATHER_data():
#     response = requests.get(_get_weather_url())
#     if response.ok:
#         return response
#     else:
#         return None
#
#
# def test_ISS_request_response():
#     # Call the service, which will send a request to the server.
#     response = get_ISS_data()
#
#     # If the request is sent successfully, then I expect a response to be returned.
#     assert_is_not_none(response)
#
#
# def test_WEATHER_request_response():
#     # Call the service, which will send a request to the server.
#     response = get_WEATHER_data()
#
#     # If the request is sent successfully, then I expect a response to be returned.
#     assert_is_not_none(response)


@patch('requests.get')
def test_getting_ISS_data(mock_get):
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True
    mock_ISS_location = (1544503409, '46.9037', '123.7170')
    mock_get.return_value.text = '{"timestamp": 1544503409, "iss_position": {"latitude": "46.9037", "longitude": "123.7170"}, "message": "success"}'

    assert ISStask.consume_ISS_api() == mock_ISS_location

@patch('requests.get')
def test_getting_WEATHER_data(mock_get):
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True
    mock_location = '{"coord": {"lon": -160.72, "lat": 40.74}, "weather": [{"id": 804, "main": "Clouds", "description":\
                    "overcast clouds", "icon": "04n"}], "base": "stations", "main": {"temp": 285.123, "pressure": \
                    1040.78, "humidity": 98, "temp_min": 285.123, "temp_max": 285.123, "sea_level": 1040.8, \
                    "grnd_level": 1040.78}, "wind": {"speed": 5.93, "deg": 286.509}, "clouds": {"all": 88}, "dt":\
                     1544503940, "sys": {"message": 0.0058, "sunrise": 1544551032, "sunset": 1544584530}, "id": 0, \
                     "name": "", "cod": 200}'


    mock_get.return_value.text = mock_location
    mock_tuple = (1544504255, '-160.72', '40.74')
    assert ISStask.get_weather_under_ISS(mock_tuple) == json.loads(mock_location)


def _get_weather_url():
    return ('http://api.openweathermap.org/data/2.5/weather?lat=48.2365&lon=-155.6439'
            '&id=524901&APPID=ebb6b0d75ac8039bfcd5db95d399b515')


ISS_BASE_URL = 'http://api.open-notify.org'
ISS_DATA_URL = urljoin(ISS_BASE_URL, 'iss-now.json')

# WEATHER_BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
# WEATHER_DATA_URL = urljoin(WEATHER_BASE_URL, '&id=524901&APPID=ebb6b0d75ac8039bfcd5db95d399b515')


