import json
from datetime import datetime
def save_weather_report(city, filename="weather_log.json"):
    """Récupère la météo et la sauvegarde dans un fichier"""

    # 1. Récupérer la température
    temp = get_temperature(city)
    if temp is None:
        return False

    # 2. Créer le rapport
    report = {
    'city': city,
    'temperature': temp,
    'timestamp': datetime.now().isoformat()
    }

    # 3. Sauvegarder dans le fichier
    try:
    # Lire le fichier existant
        with open(filename, 'r') as f:
            reports = json.load(f)
    except FileNotFoundError:
            reports = []

    reports.append(report)

    with open(filename, 'w') as f:
        json.dump(reports, f)

    return True