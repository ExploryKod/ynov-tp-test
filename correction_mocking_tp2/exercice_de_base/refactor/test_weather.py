class TestWeather(unittest.TestCase):

 def setUp(self):
    """Fixture : prépare les données avant chaque test"""
    # TODO: Créez self.sample_weather_data avec des données météo types
    # TODO: Créez self.test_city avec une ville de test
    pass

    @patch('weather_service.requests.get')
    def test_get_temperature_success(self, mock_get):
        """Test avec données de la fixture"""
        fake_response = Mock()
        fake_response.status_code = 200
        # TODO: Utilisez self.sample_weather_data ici
        fake_response.json.return_value = self.sample_weather_data

        mock_get.return_value = fake_response

        # TODO: Utilisez self.test_city
        result = get_temperature(self.test_city)

        # TODO: Complétez les assertions