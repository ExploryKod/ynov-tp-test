def additionner(a, b):
 """Additionne deux nombres"""
 return a + b
def est_pair(nombre):
 """Vérifie si un nombre est pair"""
 return nombre % 2 == 0
def valider_email(email):
 """Valide un email simple (doit contenir @ et .)"""
 if "@" not in email:
    raise ValueError("Email: besoin d'un @ dans l'email")
 if "." not in email:
    raise ValueError("Email: besoin d'un point dans l'email")
 return True

def calculer_moyenne(notes):
 """Calcule la moyenne d'une liste de notes"""
 if len(notes) == 0:
    return 0
 return sum(notes) / len(notes)
def convertir_temperature(celsius):
 """Convertit des degrés Celsius en Fahrenheit"""
 return (celsius * 9/5) + 32

def diviser(a, b):
    """Divise a par b, une erreur doit survenir si b vaut 0"""
    if b == 0:
        raise ValueError("Division par zéro interdite")
    return a / b

def valider_mot_de_passe(mot_de_passe):
    """Valide un mot de passe en respectant ces critères:"""
    if len(mot_de_passe) < 8:
        return False
    if not any(c.isupper() for c in mot_de_passe):
        return False
    if not any(c.isdigit() for c in mot_de_passe):
        return False
    if not any(c in "!@#$%^&*()-_+=" for c in mot_de_passe):
        return False
    return True