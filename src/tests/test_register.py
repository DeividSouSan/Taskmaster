import unittest

from ..server.server import create_app
from ..forms.register_form import RegisterForm
from flask_wtf.csrf import generate_csrf


class TestRegisterForm(unittest.TestCase):

    def setUp(self) -> None:
        self.app = create_app()
        self.app.testing = True

        self.client = self.app.test_client()

    def test_register_all_credentials_correct(self):

        with self.app.test_request_context():
            csrf_token = generate_csrf()

            form_data = {
                "username": "test",
                "password": "12345678",
                "fullname": "test",
                "email": "test@gmail.com",
                "submit": True,
                "csrf_token": csrf_token
            }

            form = RegisterForm(data=form_data)
            
            self.assertEqual(form.validate(), True, "Form is not valid")

        self.assertNotEqual(form, None, "Form is None")
        self.assertDictEqual(form.data, form_data, "Form data different from expected")

    def test_register_password_too_short(self):

        with self.app.test_request_context():
            csrf_token = generate_csrf()

            form_data = {
                "username": "test",
                "password": "12345",
                "fullname": "test",
                "email": "test@gmail.com",
                "submit": True,
                "csrf_token": csrf_token
            }

            form = RegisterForm(data=form_data)
            
            self.assertEqual(form.validate(), False, "Form is valid")

        self.assertNotEqual(form, None, "Form is None")
        self.assertEqual(form.data, form_data, "Form data different from expected")
        
    def test_register_email_not_valid(self):

            with self.app.test_request_context():
                csrf_token = generate_csrf()

                form_data = {
                    "username": "test",
                    "password": "12345678",
                    "fullname": "test",
                    "email": "aaaa",
                    "submit": True,
                    "csrf_token": csrf_token
                }

                form = RegisterForm(data=form_data)
                self.assertEqual(form.validate_on_submit(), False, "Form is valid")

            self.assertNotEqual(form, None, "Form is None")
            self.assertEqual(form.data, form_data, "Form data different from expected")
            
    def test_register_csrf_token_invalid(self):

            with self.app.test_request_context():
                csrf_token = generate_csrf()

                form_data = {
                    "username": "test",
                    "password": "12345678",
                    "fullname": "test",
                    "email": "test@gmail.com",
                    "submit": True,
                    "csrf_token": "1234"
                }

                form = RegisterForm(data=form_data)
                
                self.assertEqual(form.validate(), False, "Form is valid")

            self.assertNotEqual(form, None, "Form is None")
            self.assertEqual(form.data, form_data, "Form data different from expected")
            
    def test_register_username_too_long(self):

        with self.app.test_request_context():
            csrf_token = generate_csrf()

            form_data = {
                "username": "mynameistoolongbutiwanttoregister",
                "password": "12345678",
                "fullname": "test",
                "email": "test@gmail.com",
                "submit": True,
                "csrf_token": csrf_token
            }

            form = RegisterForm(data=form_data)
            
            self.assertEqual(form.validate(), False, "Form is valid")

        self.assertNotEqual(form, None, "Form is None")
        self.assertEqual(form.data, form_data, "Form data different from expected")