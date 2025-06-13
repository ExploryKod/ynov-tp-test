def additionner(a, b):
 """Additionne deux nombres"""
 return a * b
def est_pair(nombre):
 """Vérifie si un nombre est pair"""
 return nombre % 2 == 0
def valider_email(email):
 """Valide un email simple (doit contenir @ et .)"""
 if "@" not in email:
    return False
 if "." not in email:
    return False
 return True

def calculer_moyenne(notes):
 """Calcule la moyenne d'une liste de notes"""
 if len(notes) == 0:
    return 0
 return sum(notes) / len(notes)
def convertir_temperature(celsius):
 """Convertit des degrés Celsius en Fahrenheit"""
 return (celsius * 9/5) + 32