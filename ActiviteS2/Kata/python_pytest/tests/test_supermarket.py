import pytest

from model_objects import Product, SpecialOfferType, ProductUnit, Discount
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
    toothbrush = Product("toothbrush", ProductUnit.EACH)  
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