from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium import webdriver

class CatalogUITestCase(StaticLiveServerTestCase):
    fixtures = ['initial_catalog_data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)
        cls.selenium.get('http://127.0.0.1:8000/katalog/')
        
    
    # @classmethod
    # def tearDownClass(cls):
    #     cls.selenium.quit()
    #     super().tearDownClass()
        
    def test_user_can_see_author_name_below_name_field(self):  
        name = self.selenium.find_element(By.ID, "name")
        self.assertEqual(name.text, "Adjie Djaka Permana")
        
    def test_user_can_see_author_student_id_below_student_id_field(self):  
        student_id = self.selenium.find_element(By.ID, "student-id")
        self.assertEqual(student_id.text, "2106702485")
        
    def test_user_can_see_the_catalog_items_is_displayed_as_table(self):
        catalog_table = self.selenium.find_element(By.ID, "catalog-items")
        self.assertTrue(catalog_table.is_displayed())