import pytest
from tests.helpers.fake_catalog import FakeCatalog
from model_objects import Product, ProductUnit

@pytest.fixture
def product_in_catalog_by_kilo():
    def _create(name="apples", price=1.99):
        catalog = FakeCatalog()
        product = Product(name, ProductUnit.KILO)
        catalog.add_product(product, price)
        return catalog, product, price
    return _create

@pytest.fixture
def product_in_catalog_by_each():
    def _create(name="toothbrush", price=0.99):
        catalog = FakeCatalog()
        product = Product(name, ProductUnit.EACH)
        catalog.add_product(product, price)
        return catalog, product, price
    return _create
