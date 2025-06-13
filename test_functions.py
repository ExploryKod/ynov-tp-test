import unittest
from functions import additionner, est_pair, valider_email, calculer_moyenne, convertir_temperature
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

def test_valider_email_valide(self):
 """Test avec un email valide"""
 self.assertTrue(valider_email("test@example.com"))
 
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
 pass
def test_calculer_moyenne_liste_vide(self):
 """Test avec une liste vide"""
 self.assertEqual(calculer_moyenne([]), 0)
 pass
def test_calculer_moyenne_une_note(self):
 """Test avec une seule note"""
 # TODO: Testez avec [18] - résultat attendu : 18
 self.assertEqual(calculer_moyenne([18]), 18)
 pass

# À COMPLÉTER : Ajoutez vos tests ici
# Permet d'exécuter les tests
if __name__ == '__main__':
 unittest.main()