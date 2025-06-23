Il y avait une doublure custom qui me sert de model réutilisable que j'ai conservé: 
```py
from catalog import SupermarketCatalog

class FakeCatalog(SupermarketCatalog):
    def __init__(self):
        self.products = {}
        self.prices = {}

    def add_product(self, product, price):
        self.products[product.name] = product
        self.prices[product.name] = price

    def unit_price(self, product):
        return self.prices[product.name]
```

J'ai mis en place deux doublures moi-même : 
- Via l'uage de pytest-mock et le paramètre mocker, je peux créer un faux produit avec sa quantité et son unité de mesure (KILO / EACH)

Voici le résultat avec pytest-mock de mon mocking : 
```py
def test_print_quantity_each(self,mocker):
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
