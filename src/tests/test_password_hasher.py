import unittest

from src.utils.password_hasher import PasswordHash


class TestPasswordHasher(unittest.TestCase):
    def testcheck_hash_password(self):

        # Password got from the user
        password = "12345678"

        # Password got from the database that is related to the username
        hashed_password = PasswordHash().hash_password(password)

        # The hashed_password comes from the database as a string
        hashed_password = hashed_password.decode("utf-8")

        self.assertTrue(PasswordHash().check_password(password, hashed_password))
