import bcrypt


class PasswordHash():

    @staticmethod
    def hash_password(password: str) -> bytes:
        bytes_pw = bytes(password, "utf-8")
        password_hash = bcrypt.hashpw(bytes_pw, bcrypt.gensalt())
        return password_hash

    @staticmethod
    def check_password(password: str, hashed_password: str) -> bool:
        """
        the hashed_password comes from the database as a string
        """

        password = bytes(password, "utf-8")
        hashed_password = bytes(hashed_password, "utf-8")

        return bcrypt.checkpw(password, hashed_password)
