import requests
def get_temperature(city):
    """Récupère la température d'une ville via une API"""
    
    url = f"http://api.openweathermap.org/data/2.5/weather"
    
    params = {
    'q': city,
    'appid': 'fake_api_key', # Clé bidon pour ce TP
    'units': 'metric'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['main']['temp']
    else:
        return None