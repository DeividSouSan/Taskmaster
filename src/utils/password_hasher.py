import bcrypt


class PassowordHash():

    @staticmethod
    def hash_password(password):
        bytes_pw = bytes(password, "utf-8")
        password_hash = bcrypt.hashpw(bytes_pw, bcrypt.gensalt())
        return password_hash

    @staticmethod
    def check_password(password, hashed_password):
        password = bytes(password, "utf-8")
        hashed_password = bytes(hashed_password, "utf-8")
        
        return bcrypt.checkpw(password, hashed_password)
