import unittest
from unittest.mock import patch, Mock
from weather_service import get_temperature

class TestWeather(unittest.TestCase):

    @patch('weather_service.requests.get')
    def test_get_temperature_success(self, mock_get):
        fake_response = Mock()
        fake_response.status_code = 200
        fake_response.json.return_value = {
            'main': {
                'temp': 25.5
            }
        }

        mock_get.return_value = fake_response

        result = get_temperature("Paris")
        self.assertEqual(result, 25.5)
        mock_get.assert_called_once_with(
            'http://api.openweathermap.org/data/2.5/weather',
            params={'q': 'Paris', 'appid': 'fake_api_key', 'units': 'metric'}
        )

if __name__ == '__main__':
    unittest.main()
