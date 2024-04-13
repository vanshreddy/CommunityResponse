from flask import Flask, jsonify
import unittest
from routes.api import app

class TestApiRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_data(self):
        response = self.app.get('/api/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'name': 'John', 'age': 30})

if __name__ == '__main__':
    unittest.main()