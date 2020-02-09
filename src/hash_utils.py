"""
Hashing password module
"""
import hashlib 


class HashUtils:
    """
    Class to implement Hashing

    """

    def get_hash_passord(self, password):
        """
        Convert plain password to hash password using sha256
        """

        encode_pwd = str.encode(password)
        hash_object = hashlib.sha256(encode_pwd)
        hashed_pwd = hash_object.hexdigest()

        return hashed_pwd

    def check_pw_hash(self, password, hashed_pwd):

        """"
        Compareing two password
        """
        
        response = True if password == hashed_pwd else False

        return response
