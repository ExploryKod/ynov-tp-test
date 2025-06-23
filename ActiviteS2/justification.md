## Justification du refactoring

Je n'ai pas touché au code existant dans src/ ce qui fait que je reste dépendant d'un code qui aurait lui-même gagné à être mieux organisé.

Pour autant, j'ai réorganisé les tests une fois que j'ai obtenu un trés bon coverage :
- Création des fichiers de tests dans des dossier "unit" pour les test unitaire en anticipant d'autres type (ex: intégration)
- Je nomme chaque fichier avec un nom qui reflète directement le fichier ou la class associée dans src/ afin de gagner en lisibilité et maintenabilité.
- Je met les tests dans une class quand il y a beaucoup de fonction (qui deviennent des méthodes) pour favoriser une réusabilité ultérieur si besoin.
- Je suis un pattern de naming assez similaire par méthode ou fonction de tests avec toujours le nom de la class associée puis la méthode testé et des précisions sur les conditions pour les mêmes raisons que ci-dessus. 
- Je sépare en respectant le AAA mis en exergue (Arrange, Act, Assert) dans le bon ordre (1) et utilise pytest qui le met aussi en relief avec ses outils (ex: assert ...)
- Je créer des fixtures afin que la phase "Arrange" du AAA soit facilitée en réutilisant des morceaux de code pour respecter les règle comme le "DRY", faciliter le Single Responsibility Principle (SRP) et favoriser la modularité et réusabilité du code (2).
- La doublure custom que représente FakeCatalog existait déjà avant le refactoring : il est trés bien et je l'ai donc conservé dans mes helpers transversaux
- Je n'ai pas forcément besoin de fausse base de donnée dans mon cas : les doublures et quelques paramètres que je répète dans les tests suffisent car la complexité se trouve plus dans les calculs des réductions. 
- Pour les calculs des réductions et chaque deal/réduction j'ai créé une méthode privée _apply_cart_offer. Elle permet de ne pas répéter la logique utilisé pour créer une réduction sur un produit mais doit rester lié au cart d'où son caractère privée. 
- Les deal/réductions ont à chaque fois un des cas positifs et des cas négatifs ou des cas limites : afin de ne pas écrire trop de tests, j'utilise les tests paramétrés afin de couvrir autant les cas négatifs comme les cas limites et les cas positifs. Pour ces tests, je n'ai cependant pas été assez exhaustif et il manque des cas négatifs. Voir le (3) pour un exemple.

(1) La structure d'un test (exemple): 

```py
    def test_print_quantity_each(mocker):
        """
        GIVEN une quantité de 3 pour un produit calculé par lot
        WHEN on imprime la quantité du produit sur le ticket
        THEN le résultat est un chiffre 3 imprimé sur le ticket
        """
        printer = ReceiptPrinter()
        item = mocker.Mock()
        item.quantity = 3
        item.product.unit = ProductUnit.EACH

        result = printer.print_quantity(item)
        assert result == "3"
```

(2) Mes fixtures, Exemple : 
Ici le code suivant sera sans cesse répété dans chaque test :

```py
    catalog = FakeCatalog()
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    catalog.add_product(toothbrush, 0.99)
```

J'ai donc créer des fixtures en fonction de deux cas spécifiques que je veux mettre en exergue (unités de mesure):
- Pour les produits calculé par kilo
- Pour les produits calculé par unité (each)
Les noms pourront changé ou alors même ne pas être mentionnées. Je les nommes quand même dans mes tests pour la lisibilité sans devoir tout répéter.
- Consultez ces fixtures dans le dossier fixtures > catalog_fixtures.py

Il y a aussi une série de fixtures pour les tickets de caisse (receipts) car il y avait un beau potentiel de réusabilité pour ce code.

J'ai créer des fixtures mais en prenant en compte le fait de ne pas trop regrouper tout afin de laisser la logique et les élèments important bien visible (nom, prix...).


(3) Un exemple de mes tests paramétrés :
```py
   # Test des cas limites et du cas positif avec un parametrized :
    # Test de chaque quantité : Moins de 5, plus de 2 ou le cas positif avec 5 et les réductions allouées
    @pytest.mark.parametrize("quantity,expected_discounts", [
        (5.0, 1),
        (3.0, 0),
        (1.0, 0)
    ])
    def test_shopping_cart_five_for_amount_discount(self, product_in_catalog_by_kilo, quantity, expected_discounts):
        catalog, apples, price = product_in_catalog_by_kilo("apples", 1.99)
        price_for_five = 5.0
        receipt = self._apply_cart_offer(
            apples, quantity,
            Offer(SpecialOfferType.FIVE_FOR_AMOUNT, apples, price_for_five),
            catalog
        )
        assert len(receipt.discounts) == expected_discounts
```