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
    
    @patch('weather_service.requests.get')
    def test_get_temperature_city_not_found(self, mock_get):
        """Test quand la ville n'existe pas"""

        # TODO: Créez un Mock qui retourne status_code = 404

        # TODO: Configurez mock_get.return_value

        # TODO: Testez get_temperature("VilleInexistante")

        # TODO: Vérifiez que le résultat est None

        pass # Remplacez p
        
    @patch('weather_service.requests.get')
    def test_get_temperature_network_error(self, mock_get):
        """Test quand il y a une erreur réseau"""

        # TODO: Configurez le mock pour lever une exception
        # Indice: mock_get.side_effect = requests.exceptions.RequestException()
        mock_get.side_effect = requests.exceptions.RequestException()
        # TODO: Testez que votre fonction gère l'exception
        # Vous devrez peut-être modifier weather_service.py pour gérer ce cas
        result = get_temperature("Paris")
        self.assertIsNone(result)

        pass
    
 
if __name__ == '__main__':
    unittest.main()




