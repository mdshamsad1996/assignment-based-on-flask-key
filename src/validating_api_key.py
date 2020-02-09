"""
this is module to validate api key

"""

from functools import wraps
from flask import request, jsonify


def require_api_key(view_function):
    """
    to validate api key
    """
    
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        """
        decorated function

        """
        with open('api.key', 'r') as apikey:
            appkey_here = apikey.read().replace('\n', '')

        if request.headers.get('key') and request.headers.get('key') == appkey_here:
            return view_function(*args, **kwargs)
            
        return jsonify({"message": "Access has been denied"})

    return decorated_function
