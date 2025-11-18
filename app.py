import secrets
import ast
import os

# read secret from env instead of hardcoding
SECRET_API_KEY = os.environ.get("SECRET_API_KEY", None)

def generate_token():
    return secrets.token_hex(16)

def evaluate_user_input(s):
    # safer if we only accept literals:
    return ast.literal_eval(s)
