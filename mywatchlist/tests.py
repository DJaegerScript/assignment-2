from django.test import TestCase

# Create your tests here.
class WatchListTest(TestCase):
    def test_response_code_200(self):
        watch_list_resp = self.client.get('/mywatchlist/')
        watch_list_html_resp = self.client.get('/mywatchlist/html')
        watch_list_xml_resp = self.client.get('/mywatchlist/xml')
        watch_list_json_resp = self.client.get('/mywatchlist/json')

        self.assertEqual(watch_list_resp.status_code, 200)
        self.assertEqual(watch_list_html_resp.status_code, 200)
        self.assertEqual(watch_list_xml_resp.status_code, 200)
        self.assertEqual(watch_list_json_resp.status_code, 200)
        
    def test_response_code_200_parameterized_json_endpoint(self):
        response_codes = []
        for i in range(10):
            response = self.client.get('/mywatchlist/json/' + str(i+1))
            response_codes.append(response.status_code)
        self.assertTrue(all(response_code == 200 for response_code in response_codes))
        
    def test_response_code_200_parameterized_xml_endpoint(self):
        response_codes = []
        for i in range(10):
            response = self.client.get('/mywatchlist/xml/' + str(i+1))
            response_codes.append(response.status_code)
        self.assertTrue(all(response_code == 200 for response_code in response_codes))