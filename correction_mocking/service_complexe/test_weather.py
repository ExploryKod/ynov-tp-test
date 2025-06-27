from unittest.mock import mock_open, patch
from weather_service import save_weather_report
class TestWeatherReport(unittest.TestCase):

 def setUp(self):
 # TODO: Préparez vos données de test
    pass

    @patch('weather_service.datetime')
    @patch('builtins.open', new_callable=mock_open, read_data='[]')
    @patch('weather_service.get_temperature')
    def test_save_weather_report_success(self, mock_get_temp, mock_file,mock_datetime):
        """Test sauvegarde rapport météo - EXERCICE PRINCIPAL"""

        # TODO: Configurez mock_get_temp pour retourner 20.5

        # TODO: Configurez mock_datetime.now().isoformat() pour retourner une date fixe

        # TODO: Appelez save_weather_report("Paris")

        # TODO: Vérifiez que le résultat est True

        # TODO: Vérifiez que get_temperature a été appelé avec "Paris"

        # TODO: Vérifiez que le fichier a été ouvert en lecture puis en écriture

        pass