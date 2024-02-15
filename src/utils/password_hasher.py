import bcrypt


class PassowordHash():

    @staticmethod
    def hash_password(password):
        bytes_pw = bytes(password, "utf-8")
        password_hash = bcrypt.hashpw(bytes_pw, bcrypt.gensalt())
        return password_hash

    @staticmethod
    def check_password(password, hash):
        hashed_password = PassowordHash().hash_password(password)
        return hashed_password == hash
