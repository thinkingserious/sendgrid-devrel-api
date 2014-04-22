import unittest
from flask import current_app
import requests

class APITestCase(unittest.TestCase):

    def setUp(self):
        self.VERSION = 'v1.0'
        self.BASE_URL = 'http://127.0.0.1:5000'

    def tearDown(self):
         pass

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_404(self):
        r = requests.get(self.BASE_URL + '/does/not/exist')
        self.assertTrue(r.status_code == 404)

    def test_team_get(self):
        r = requests.get(self.BASE_URL + '/api/' + self.VERSION + '/team')
        self.assertTrue(r.status_code == 200)

if __name__ == '__main__':
    unittest.main()