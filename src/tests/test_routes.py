import unittest

from ..server.server import create_app


class TestRoutes(unittest.TestCase):
    
    def setUp(self) -> None:
        self.app = create_app()
        self.app.testing = True
        
        self.client = self.app.test_client()

    def test_login(self):
        response = self.client.get("/login")

        self.assertEqual(response.status_code, 200)
        
    def test_register(self):
        response = self.client.get("/register")

        self.assertEqual(response.status_code, 200)

