import unittest
from functions import additionner, est_pair, valider_email, calculer_moyenne, convertir_temperature, diviser, valider_mot_de_passe
class TestFonctions(unittest.TestCase):

 def test_additionner_cas_positif(self):
    """Test addition avec nombres positifs"""
    resultat = additionner(2, 3)
    self.assertEqual(resultat, 5)

 def test_additionner_cas_negatif(self):
    """Test addition avec nombres négatifs"""
    resultat = additionner(-2, -3)
    self.assertEqual(resultat, -5)
    
    
def test_est_pair_nombre_pair(self):
    """Test avec un nombre pair"""
    self.assertTrue(est_pair(4))
def test_est_pair_nombre_impair(self):
    """Test avec un nombre impair"""
    self.assertFalse(est_pair(3))
def test_est_pair_zero(self):
    """Test avec zéro"""
    self.assertTrue(est_pair(0))

# VALIDATION DES EMAILS
def test_valider_email_valide(self):
 """Test avec un email valide"""
 self.assertTrue(valider_email("amaury@example.com"))
 """Test avec un email invalide et levée d'une exception lié à l'absence de @"""
 with self.assertRaises(ValueError) as context1:
        valider_email("amauryexample.com")
 self.assertEqual(str(context1.exception), "Email: besoin d'un @ dans l'email")

 """Test avec un email invalide et levée d'une exception lié à l'absence de ."""
 with self.assertRaises(ValueError) as context2:
    valider_email("amaury@examplecom")
 self.assertEqual(str(context2.exception), "Email: besoin d'un point dans l'email")

def test_valider_email_sans_arobase(self):
 """Test avec un email sans @"""
 self.assertFalse(valider_email("testexample.com"))
def test_valider_email_sans_point(self):
 """Test avec un email sans point"""
 self.assertFalse(valider_email("test@example"))
 
def test_calculer_moyenne_liste_normale(self):
 """Test avec une liste de notes normales"""
 # TODO: Testez avec [10, 15, 20] - résultat attendu : 15
 # Utilisez self.assertEqual(resultat, valeur_attendue)
 self.assertEqual(calculer_moyenne([10, 15, 20]), 15)
 
def test_calculer_moyenne_liste_vide(self):
 """Test avec une liste vide"""
 self.assertEqual(calculer_moyenne([]), 0)
 
def test_calculer_moyenne_une_note(self):
 """Test avec une seule note"""
 # TODO: Testez avec [18] - résultat attendu : 18
 self.assertEqual(calculer_moyenne([18]), 18)
 

def test_convertir_temperature_zero(self):
 """Test conversion 0°C = 32°F"""
 # TODO: Testez la conversion de 0°C
 self.assertEqual(convertir_temperature(0), 32)
 
def test_convertir_temperature_eau_bouillante(self):
 """Test conversion 100°C = 212°F"""
 # TODO: Testez la conversion de 100°C
 self.assertEqual(convertir_temperature(100), 212)

# À COMPLÉTER : Ajoutez vos tests ici

def test_diviser(self):
    self.assertEqual(diviser(10, 2), 5)
    self.assertAlmostEqual(diviser(7, 3), 7/3, places=5)

    with self.assertRaises(ValueError):
        diviser(5, 0)

def test_valider_mot_de_passe(self):
    self.assertTrue(valider_mot_de_passe("anpo1!"))
    self.assertFalse(valider_mot_de_passe("anopo"))        
    self.assertFalse(valider_mot_de_passe("anipo1"))        
    self.assertFalse(valider_mot_de_passe("AnoPo"))        
    self.assertFalse(valider_mot_de_passe("AnoPo1")) 

# Permet d'exécuter les tests
if __name__ == '__main__':
 unittest.main()