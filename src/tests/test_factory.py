import unittest

from .. import create_app


class TestFactory(unittest.TestCase):

    def setUp(self) -> None:
        self.app = None

    def test_create_app(self):
        self.app = create_app()
        self.app = self.app.test_client()
        self.app.testing = True

        self.assertNotEqual(self.app, None)
