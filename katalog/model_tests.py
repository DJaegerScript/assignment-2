from django.test import TestCase
from django.forms.models import model_to_dict
from katalog.models import CatalogItem

# Create your tests here.
class CatalogTestCase(TestCase):
    fixtures = ['initial_catalog_data.json']
    
    def test_data_contains_specified_key(self):
        data = model_to_dict(CatalogItem.objects.first())
        self.assertTrue("item_name" in  data)
        self.assertTrue("item_price" in  data)
        self.assertTrue("description" in  data)
        self.assertTrue("item_stock" in  data)
        self.assertTrue("rating" in  data)
        self.assertTrue("item_url" in  data)
        
    def test_data_has_correct_data_type(self):
        data = CatalogItem.objects.all()
        for single_data in data:
             self.assertTrue(isinstance(single_data.item_name, str))
             self.assertTrue(isinstance(single_data.item_price, int))
             self.assertTrue(isinstance(single_data.description, str))
             self.assertTrue(isinstance(single_data.item_stock, int))
             self.assertTrue(isinstance(single_data.rating, int))
             self.assertTrue(isinstance(single_data.item_url, str))
