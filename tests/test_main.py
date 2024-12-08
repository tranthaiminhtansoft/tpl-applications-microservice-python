"""
This is a test unit for microservice "Hello World".
"""
import unittest
from app.main import app

class TestMain(unittest.TestCase):
    """
    Unit test class
    """
    def setUp(self):
        """
        Function to setup
        """
        self.client = app.test_client()
        self.client.testing = True

    def test_hello_world(self):
        """
        Function to test
        """
        response = self.client.get('/')
        self.assertEqual(response.data, b"Hello, World!")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
