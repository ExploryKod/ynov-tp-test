import pytest
import math

from shopping_cart import ShoppingCart
from model_objects import Product, SpecialOfferType, ProductUnit, Discount, Offer
from receipt import Receipt
from tests.fixtures.catalog_fixtures import product_in_catalog_by_kilo, product_in_catalog_by_each

class TestShoppingCart:
    """Test adding or updating new items to shopping cart with or without offers"""
    
    def test_shopping_cart_add_item(self):
        cart = ShoppingCart()
        toothbrush = Product("toothbrush", ProductUnit.EACH)
        
        cart.add_item(toothbrush)  
        
        assert len(cart.items) == 1

    # Couvre shopping_cart > add_item_quantity
    def test_shopping_cart_add_item_quantity_with_same_product_already_in_cart(self):
        cart = ShoppingCart()
        apples = Product("apples", ProductUnit.KILO)
        
        # Nous ajoutons une quantité 1 de pommes 
        cart.add_item_quantity(apples, 1.0)
        # Nous ajoutons à nouveau des pommes : quantité de 1
        cart.add_item_quantity(apples, 1.0)
        # Nous devons donc avoir une quantité 2 de pommes dans le panier
        assert cart.product_quantities[apples] == 2.0

    def test_shopping_cart_handle_offers_with_no_offers(self, product_in_catalog_by_kilo):     
        catalog, apples, _ = product_in_catalog_by_kilo("apples", 1.99)
        
        cart = ShoppingCart()
        offers = {}
        cart.add_item_quantity(apples, 3.0)
        receipt = Receipt()
        
        cart.handle_offers(receipt, offers, catalog)
        assert len(receipt.discounts) == 0

    def test_shopping_cart_handle_offers_with_three_for_two_offer(self, product_in_catalog_by_kilo):
        catalog, apples, price = product_in_catalog_by_kilo("apples", 1.99)
        quantity = 3.0
        quantity_as_int = int(quantity)
        catalog.add_product(apples, price)
        cart = ShoppingCart()
        offers = {apples: Offer(SpecialOfferType.THREE_FOR_TWO, apples, None)}
        cart.add_item_quantity(apples, quantity)
        receipt = Receipt()
        
        cart.handle_offers(receipt, offers, catalog)
        assert len(receipt.discounts) == 1
        discount = receipt.discounts[0]
        x = 3
        number_of_x = math.floor(quantity_as_int / x)
        discount_amount = quantity * price - ((number_of_x * 2 * price) + quantity_as_int % 3 * price)
        
        assert discount.product == apples
        assert discount.description == "3 for 2"
        assert pytest.approx(discount.discount_amount, 0.01) == -discount_amount

    def test_shopping_cart_handle_offers_threefortwo_with_two_or_less_item(self, product_in_catalog_by_kilo):
        catalog, apples, price = product_in_catalog_by_kilo("apples", 1.99)
        quantity = 2.0

        catalog.add_product(apples, price)
        cart = ShoppingCart()
        offers = {apples: Offer(SpecialOfferType.THREE_FOR_TWO, apples, None)}
        cart.add_item_quantity(apples, quantity)
        receipt = Receipt()
        
        cart.handle_offers(receipt, offers, catalog)
        assert len(receipt.discounts) == 0

    def test_shopping_cart_handle_offers_with_two_for_amount_offer(self, product_in_catalog_by_kilo):
        catalog, apples, price = product_in_catalog_by_kilo("apples", 1.99)
        quantity = 3.0 # quantité achetée
        price_for_two = 3.0 # paramètre arguments 
        apples = Product("apples", ProductUnit.KILO)
        catalog.add_product(apples, price)
        cart = ShoppingCart()
    
        offers = {apples: Offer(SpecialOfferType.TWO_FOR_AMOUNT, apples, price_for_two)}
        cart.add_item_quantity(apples, quantity)
        receipt = Receipt()
        
        cart.handle_offers(receipt, offers, catalog)
        discount = receipt.discounts[0]

        # Nombre de produits à acheter pour bénéficier de l'offre
        number_to_reach = 2
        quantity_as_int = int(quantity)
        # Calcul de l'offre comme dans la méthode (le code n'utilise pas de division entière donc on le reproduit exactement)
        # Note: on devrait plutôt refactorer cette division dans la méthode mais l'exercice ne l'autorise pas: seulement les tests sont refactorés
        total = price_for_two * (quantity_as_int /  number_to_reach) + quantity_as_int % 2 * price
        two_for_amount_discount = price * quantity - total

        print(two_for_amount_discount)
        assert discount.product == apples
        assert discount.description == f"2 for {price_for_two}"
        assert discount.discount_amount == pytest.approx(-two_for_amount_discount)  
     
    def test_shopping_cart_handle_offers_with_five_for_amount_offer(self, product_in_catalog_by_kilo):
        catalog, apples, price = product_in_catalog_by_kilo("apples", 1.99)
        quantity = 5.0 # quantité achetée
        price_for_five = 5.0 # paramètre arguments : prix non-dépassable si on en achète 5
        catalog.add_product(apples, price)
        cart = ShoppingCart()
    
        offers = {apples: Offer(SpecialOfferType.FIVE_FOR_AMOUNT, apples, price_for_five)}
        cart.add_item_quantity(apples, quantity)
        receipt = Receipt()
        
        cart.handle_offers(receipt, offers, catalog)
        discount = receipt.discounts[0]

        # Nombre de produits à acheter pour bénéficier de l'offre
        number_to_reach = 5 # c'est x = 5 dans la méthode
        quantity_as_int = int(quantity)
        number_of_x = math.floor(quantity_as_int /   number_to_reach)
        # Calcul de l'offre comme dans la méthode (le code n'utilise pas de division entière donc on le reproduit exactement)
        # Note: on devrait plutôt refactorer cette division dans la méthode mais l'exercice ne l'autorise pas: seulement les tests sont refactorés
        total = price_for_five * number_of_x + quantity_as_int % 5 * price
        five_for_amount_discount = price * quantity - total
        
        print(five_for_amount_discount)
        assert discount.product == apples
        assert discount.description == f"{number_to_reach} for {price_for_five}"
        assert discount.discount_amount == pytest.approx(-five_for_amount_discount)
    
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
    

    def test_shopping_cart_handle_offers_with_two_for_amount_offer_with_less_than_two_product(self, product_in_catalog_by_kilo):
        catalog, apples, price = product_in_catalog_by_kilo("apples", 1.99)
        quantity = 1.0 # quantité achetée
        price_for_two = 3.0 # paramètre arguments : prix non-dépassable si on en achète 5
        catalog.add_product(apples, price)
        cart = ShoppingCart()
    
        offers = {apples: Offer(SpecialOfferType.TWO_FOR_AMOUNT, apples, price_for_two)}
        cart.add_item_quantity(apples, quantity)
        receipt = Receipt()
        
        cart.handle_offers(receipt, offers, catalog)    
        assert len(receipt.discounts) == 0

    def test_shopping_cart_handle_offers_with_ten_percent_discount(self, product_in_catalog_by_kilo):
        catalog, apples, price = product_in_catalog_by_kilo("apples", 1.99)
        quantity = 1.0 # quantité achetée
        argument = 10.0 # paramètre arguments : réduction
        cart = ShoppingCart()
    
        offers = {apples: Offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, apples, argument)}
        cart.add_item_quantity(apples, quantity)
        receipt = Receipt()
        
        cart.handle_offers(receipt, offers, catalog) 
        discount_amount = -quantity * price * argument / 100.0
        discount_description = str(argument) + "% off"
        assert len(receipt.discounts) == 1
        discount = receipt.discounts[0]  
        assert discount.product == apples
        assert discount.description == discount_description
        assert discount.discount_amount == pytest.approx(discount_amount)
    
    
    def test_ten_percent_discount_on_product_by_each(self, product_in_catalog_by_each):
        catalog, toothbrush, price = product_in_catalog_by_each("toothbrush", 0.99) 
        discount = Discount(toothbrush, "10% off", -0.10)  

        assert discount.product == toothbrush  
        assert discount.description == "10% off"  
        assert discount.discount_amount == -0.10 
    
    # Class privées réutilisables et seulement liées aux méthodes du shopping cart
    def _apply_cart_offer(self, product, quantity, offer, catalog):
        catalog.add_product(product, catalog.unit_price(product))
        cart = ShoppingCart()
        cart.add_item_quantity(product, quantity)
        receipt = Receipt()
        offers = {product: offer}
        cart.handle_offers(receipt, offers, catalog)
        return receipt

    