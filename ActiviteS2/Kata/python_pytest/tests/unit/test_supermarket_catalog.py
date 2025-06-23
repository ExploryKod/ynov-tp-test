import pytest
from catalog import SupermarketCatalog
from model_objects import Product, ProductUnit

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