import pytest
from receipt_printer import ReceiptPrinter
from receipt import Receipt
from model_objects import Product, ProductUnit, Discount
from tests.fixtures.receipts_fixtures import receipt_with_discount, receipt_with_each_product, receipt_with_kilo_product, product_kilo, product_each, receipt_with_apples_two_for_one

class TestReceiptPrinter:
    "Teste tous ce qui va engendrer une apparition sur le ticket de caisse avec les réductions, totaux, quantités..."
    
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

    def test_print_quantity_kilo(self, mocker):
        """
        GIVEN une quantité de 2.5 kilo pour un produit calculé par kilo
        WHEN on imprime la quantité du produit sur le ticket
        THEN le résultat est un chiffre 2.500 imprimé sur le ticket
        """
        printer = ReceiptPrinter()
        item = mocker.Mock()
        item.quantity = 2.5
        item.product.unit = ProductUnit.KILO
        
        result = printer.print_quantity(item)
        assert result == "2.500"

    def test_print_receipt_item_each(self,receipt_with_each_product):
        """
        GIVEN une quantité de 2.5 kilo pour un produit calculé par kilo
        WHEN on imprime la quantité du produit sur le ticket
        THEN le résultat est un chiffre 2.500 imprimé sur le ticket
        """
        printer = ReceiptPrinter()
        output = printer.print_receipt(receipt_with_each_product)
    
        assert "toothbrush" in output
        assert "0.99" in output
        assert "Total:" in output
        assert "0.99" in output.splitlines()[-1]


    def test_print_receipt_item_kilo(self,receipt_with_kilo_product):
        printer = ReceiptPrinter()
        output = printer.print_receipt(receipt_with_kilo_product)
        
        assert "apples" in output
        assert "3.98" in output
        assert "1.99 * 2.000" in output
        assert "Total:" in output
        assert "3.98" in output.splitlines()[-1]


    def test_print_receipt_with_discount(self, receipt_with_discount):
        printer = ReceiptPrinter()
        output = printer.print_receipt(receipt_with_discount)
        
        assert "apples" in output
        assert "3.98" in output
        assert "2 for 1 (apples)" in output
        assert "-1.99" in output
        assert "Total:" in output
        assert "1.99" in output.splitlines()[-1]

    def test_receipt_add_discount_2for1_on_apples(self, receipt_with_apples_two_for_one):
        receipt = receipt_with_apples_two_for_one
        assert len(receipt.items) == 1

    def test_receipt_total_price(self, receipt_with_apples_two_for_one):
        receipt = receipt_with_apples_two_for_one
        assert receipt.items[0].total_price == 2.0
        assert len(receipt.discounts) == 1
        assert receipt.discounts[0].description == "2 for 1"
        assert receipt.discounts[0].discount_amount == -1.0
        assert receipt.total_price() == 1.0
