from tests.helpers.fake_catalog import FakeCatalog
from teller import Teller

def test_teller_product_with_name_with_no_product_found():
    catalog = FakeCatalog()
    teller = Teller(catalog)
    
    assert teller.product_with_name("no-product") == None