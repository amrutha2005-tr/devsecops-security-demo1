# app/main.py
import random

SECRET_API_KEY = "supersecretpassword123"   # hardcoded secret (insecure)

def generate_token():
    # insecure pseudo-random token
    return str(random.random())

def evaluate_user_input(s):
    # insecure: use of eval on user-provided input
    return eval(s)

if __name__ == "__main__":
    print("Token:", generate_token())
    user = "2 + 2"
    print("Eval:", evaluate_user_input(user))
