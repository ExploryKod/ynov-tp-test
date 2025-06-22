import pytest
import math

from catalog import SupermarketCatalog
from model_objects import Product, SpecialOfferType, ProductUnit, Discount, Offer
from receipt import Receipt
from shopping_cart import ShoppingCart
from teller import Teller
from tests.fake_catalog import FakeCatalog

@pytest.fixture
def receipt_with_apples():
    receipt = Receipt()
    product = Product("apples", ProductUnit.EACH)
    receipt.add_product(product, quantity=2, price=1.0, total_price=2.0)
    discount = Discount(product, "2 for 1", -1.0)
    receipt.add_discount(discount)
    return receipt

def test_ten_percent_discount():
    catalog = FakeCatalog()
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    catalog.add_product(toothbrush, 0.99)
    apples = Product("apples", ProductUnit.KILO)
    catalog.add_product(apples, 1.99)

    teller = Teller(catalog)
    teller.add_special_offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, toothbrush, 10.0)

    cart = ShoppingCart()
    cart.add_item_quantity(apples, 2.5)

    receipt = teller.checks_out_articles_from(cart)

    assert 4.975 == pytest.approx(receipt.total_price(), 0.01)
    assert [] == receipt.discounts
    assert 1 == len(receipt.items)
    receipt_item = receipt.items[0]
    assert apples == receipt_item.product
    assert 1.99 == receipt_item.price
    assert 2.5 * 1.99 == pytest.approx(receipt_item.total_price, 0.01)
    assert 2.5 == receipt_item.quantity

def test_discount_on_toothbrush(): 
    catalog = FakeCatalog()
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    catalog.add_product(toothbrush, 0.99)
    discount = Discount(toothbrush, "10% off", -0.10)  

    assert discount.product == toothbrush  
    assert discount.description == "10% off"  
    assert discount.discount_amount == -0.10 
    
def test_receipt_add_discount_on_apples(receipt_with_apples):
    receipt = receipt_with_apples
    assert len(receipt.items) == 1

def test_receipt_total_price(receipt_with_apples):
    receipt = receipt_with_apples
    assert receipt.items[0].total_price == 2.0
    assert len(receipt.discounts) == 1
    assert receipt.discounts[0].description == "2 for 1"
    assert receipt.discounts[0].discount_amount == -1.0
    assert receipt.total_price() == 1.0
    
def test_shopping_cart_add_item():
    cart = ShoppingCart()
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    
    cart.add_item(toothbrush)  
    
    assert len(cart.items) == 1

# Couvre shopping_cart > add_item_quantity
def test_shopping_cart_add_item_quantity_with_same_product_already_in_cart():
     cart = ShoppingCart()
     apples = Product("apples", ProductUnit.KILO)
     
     # Nous ajoutons une quantité 1 de pommes 
     cart.add_item_quantity(apples, 1.0)
     # Nous ajoutons à nouveau des pommes : quantité de 1
     cart.add_item_quantity(apples, 1.0)
     # Nous devons donc avoir une quantité 2 de pommes dans le panier
     assert cart.product_quantities[apples] == 2.0
     
def test_shopping_cart_handle_offers_with_no_offers():
     catalog = FakeCatalog()
     apples = Product("apples", ProductUnit.KILO)
     catalog.add_product(apples, 1.99)
     cart = ShoppingCart()
     offers = {}
     cart.add_item_quantity(apples, 3.0)
     receipt = Receipt()
     
     cart.handle_offers(receipt, offers, catalog)
     assert len(receipt.discounts) == 0
          
def test_shopping_cart_handle_offers_with_three_for_two_offer():
    catalog = FakeCatalog()
    apples = Product("apples", ProductUnit.KILO)
    price = 1.99
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

def test_shopping_cart_handle_offers_threefortwo_with_two_or_less_item():
    catalog = FakeCatalog()
    apples = Product("apples", ProductUnit.KILO)
    price = 1.99
    quantity = 2.0

    catalog.add_product(apples, price)
    cart = ShoppingCart()
    offers = {apples: Offer(SpecialOfferType.THREE_FOR_TWO, apples, None)}
    cart.add_item_quantity(apples, quantity)
    receipt = Receipt()
     
    cart.handle_offers(receipt, offers, catalog)
    assert len(receipt.discounts) == 0

def test_shopping_cart_handle_offers_with_two_for_amount_offer():
    catalog = FakeCatalog()
    price = 1.99
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
     
def test_shopping_cart_handle_offers_with_five_for_amount_offer():
    catalog = FakeCatalog()
    price = 1.99
    quantity = 5.0 # quantité achetée
    price_for_five = 5.0 # paramètre arguments : prix non-dépassable si on en achète 5
    apples = Product("apples", ProductUnit.KILO)
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
    
def test_shopping_cart_handle_offers_with_five_for_amount_offer_with_less_than_five_product():
    catalog = FakeCatalog()
    price = 1.99
    quantity = 3.0 # quantité achetée
    price_for_five = 5.0 # paramètre arguments : prix non-dépassable si on en achète 5
    apples = Product("apples", ProductUnit.KILO)
    catalog.add_product(apples, price)
    cart = ShoppingCart()
  
    offers = {apples: Offer(SpecialOfferType.FIVE_FOR_AMOUNT, apples, price_for_five)}
    cart.add_item_quantity(apples, quantity)
    receipt = Receipt()
     
    cart.handle_offers(receipt, offers, catalog)    
    assert len(receipt.discounts) == 0

def test_shopping_cart_handle_offers_with_five_for_amount_offer_with_less_than_two_product():
    catalog = FakeCatalog()
    price = 1.99
    quantity = 1.0 # quantité achetée
    price_for_five = 5.0 # paramètre arguments : prix non-dépassable si on en achète 5
    apples = Product("apples", ProductUnit.KILO)
    catalog.add_product(apples, price)
    cart = ShoppingCart()
  
    offers = {apples: Offer(SpecialOfferType.FIVE_FOR_AMOUNT, apples, price_for_five)}
    cart.add_item_quantity(apples, quantity)
    receipt = Receipt()
     
    cart.handle_offers(receipt, offers, catalog)    
    assert len(receipt.discounts) == 0

def test_shopping_cart_handle_offers_with_two_for_amount_offer_with_less_than_two_product():
    catalog = FakeCatalog()
    price = 1.99
    quantity = 1.0 # quantité achetée
    price_for_two = 3.0 # paramètre arguments : prix non-dépassable si on en achète 5
    apples = Product("apples", ProductUnit.KILO)
    catalog.add_product(apples, price)
    cart = ShoppingCart()
  
    offers = {apples: Offer(SpecialOfferType.TWO_FOR_AMOUNT, apples, price_for_two)}
    cart.add_item_quantity(apples, quantity)
    receipt = Receipt()
     
    cart.handle_offers(receipt, offers, catalog)    
    assert len(receipt.discounts) == 0

def test_shopping_cart_handle_offers_with_ten_percent_discount():
    catalog = FakeCatalog()
    price = 1.99
    quantity = 1.0 # quantité achetée
    argument = 10.0 # paramètre arguments : réduction
    apples = Product("apples", ProductUnit.KILO)
    catalog.add_product(apples, price)
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
    
def test_superMarketCatalog_add_product_exception_error():  
    """  
    Test that a ValueError is raised when the add_product is called directly from bdd
    """  
    catalog = SupermarketCatalog()
    apples = Product("apples", ProductUnit.KILO)
    unit_price = 1.99
    with pytest.raises(Exception) as excinfo:  
        catalog.add_product(apples, unit_price)
        
    assert str(excinfo.value) == "cannot be called from a unit test - it accesses the database"

def test_superMarketCatalog_unit_price_exception_error():  
    """  
    Test that a ValueError is raised when the add_product is called directly from bdd
    """  
    catalog = SupermarketCatalog()
    apples = Product("apples", ProductUnit.KILO)
    with pytest.raises(Exception) as excinfo:  
        catalog.unit_price(apples)
            
    assert str(excinfo.value) == "cannot be called from a unit test - it accesses the database"


def test_teller_product_with_name_with_no_product_found():
    catalog = FakeCatalog()
    teller = Teller(catalog)
    
    assert teller.product_with_name("no-product") == None
  
