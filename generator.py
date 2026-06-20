import random

def generate_code():
    return random.randint(100000, 999999)

def generate_number(country_code):
    return f"{country_code} XXX XXX {random.randint(1000,9999)}"
