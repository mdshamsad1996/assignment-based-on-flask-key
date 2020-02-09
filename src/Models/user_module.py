
"""
user_module for User table

"""
from flask import json
from src import mysql, hash_utils_obj


class SimpleMethod:
    """
    SimpleMethod contained other method , which is used by some other method
    """
    def get_hashed_pwd_for_existing_use(self, curr, user_email):

        """
        Get hashed_pwd from database for existing user
        """
        curr.execute("select password from user where email=%s", (user_email,))

        return curr.fetchone()[0]


class User(): 
    """
    User class 
    """

    def create_user(self, data):

        """
        creating user with provided info
        """
        curr = mysql.connection.cursor()
        try:

            user_data = json.loads(data)

            hashed_pwd = hash_utils_obj.get_hash_passord(user_data['password'])

            curr.execute("Insert into User (name, email, password) values(%s,%s,%s)", (user_data['name'], user_data['email'], hashed_pwd))
            mysql.connection.commit()

            return "Successfully user has been created"
        finally:
            curr.close()

    def get_user(self):

        """
        Get list of user
        """
        curr = mysql.connection.cursor()
        try:
            users = []
            curr.execute('select * from User')
            records = curr.fetchall()
            for record in records:

                user = {}
                user['name'] = record[0]
                user['email'] = record[1]
                users.append(user)

            return users

        finally:
            curr.close()

    def login_with_proper_credentials(self, data):
        """
        method to check user is login with correct credentials or not
        """
        curr = mysql.connection.cursor()
        try:
            user_data = json.loads(data)

            simpl_method_obj = SimpleMethod()

            hashed_pwd = simpl_method_obj.get_hashed_pwd_for_existing_use(curr, user_data['email'])
             
            password = hash_utils_obj.get_hash_passord(user_data['password'])

            response = hash_utils_obj.check_pw_hash(password, hashed_pwd)

            message = "Login Successfull" if response else "Please provide proper credentials"
            return message
             
        finally:
            curr.close()
