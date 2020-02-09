"""
Generate API Keys 
"""

import secrets

api_key = secrets.token_urlsafe(16)

print(secrets.token_urlsafe(16))
