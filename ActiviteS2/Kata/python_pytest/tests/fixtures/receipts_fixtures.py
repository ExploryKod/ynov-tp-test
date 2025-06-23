import pytest
from model_objects import Product, ProductUnit, Discount
from receipt import Receipt

@pytest.fixture
def receipt_with_apples_two_for_one():
    receipt = Receipt()
    product = Product("apples", ProductUnit.EACH)
    receipt.add_product(product, quantity=2, price=1.0, total_price=2.0)
    discount = Discount(product, "2 for 1", -1.0)
    receipt.add_discount(discount)
    return receipt

@pytest.fixture
def product_each(product_name="toothbrush"):
    return Product(product_name, ProductUnit.EACH)


@pytest.fixture
def product_kilo(product_name="apples"):
    return Product(product_name, ProductUnit.KILO)


@pytest.fixture
def receipt_with_each_product(product_each):
    receipt = Receipt()
    receipt.add_product(product_each, quantity=1, price=0.99, total_price=0.99)
    return receipt

@pytest.fixture
def receipt_with_kilo_product(product_kilo):
    receipt = Receipt()
    receipt.add_product(product_kilo, quantity=2.0, price=1.99, total_price=3.98)
    return receipt


@pytest.fixture
def receipt_with_discount(product_kilo):
    receipt = Receipt()
    receipt.add_product(product_kilo, quantity=2.0, price=1.99, total_price=3.98)
    receipt.add_discount(Discount(product_kilo, "2 for 1", -1.99))
    return receipt
