import pytest
from receipt_printer import ReceiptPrinter
from receipt import Receipt
from model_objects import Product, ProductUnit, Discount


class FakeItem:
    def __init__(self, quantity, unit):
        self.quantity = quantity
        self.product = Product("test", unit)

def test_print_quantity_each():
    printer = ReceiptPrinter()
    item = FakeItem(quantity=3, unit=ProductUnit.EACH)
    result = printer.print_quantity(item)
    assert result == "3"

def test_print_quantity_kilo():
    printer = ReceiptPrinter()
    item = FakeItem(quantity=2.5, unit=ProductUnit.KILO)
    result = printer.print_quantity(item)
    assert result == "2.500"

@pytest.fixture
def product_each():
    return Product("toothbrush", ProductUnit.EACH)


@pytest.fixture
def product_kilo():
    return Product("apples", ProductUnit.KILO)


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


def test_print_receipt_item_each(receipt_with_each_product):
    printer = ReceiptPrinter()
    output = printer.print_receipt(receipt_with_each_product)
    
    assert "toothbrush" in output
    assert "0.99" in output
    assert "Total:" in output
    assert "0.99" in output.splitlines()[-1]


def test_print_receipt_item_kilo(receipt_with_kilo_product):
    printer = ReceiptPrinter()
    output = printer.print_receipt(receipt_with_kilo_product)
    
    assert "apples" in output
    assert "3.98" in output
    assert "1.99 * 2.000" in output
    assert "Total:" in output
    assert "3.98" in output.splitlines()[-1]


def test_print_receipt_with_discount(receipt_with_discount):
    printer = ReceiptPrinter()
    output = printer.print_receipt(receipt_with_discount)
    
    assert "apples" in output
    assert "3.98" in output
    assert "2 for 1 (apples)" in output
    assert "-1.99" in output
    assert "Total:" in output
    assert "1.99" in output.splitlines()[-1]
