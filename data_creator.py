from random import randint, choice
import names
import string


def create_name():
    return names.get_full_name()


def create_email():
    symbols = string.ascii_lowercase + string.digits
    email = (f"{''.join(choice(symbols) for i in range(9))}"
             f"_{randint(100, 999)}@ya.ru")
    return email


def create_password():
    symbols = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(choice(symbols) for i in range(6))
    return password


def create_password_from_5_symbols():
    symbols = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(choice(symbols) for i in range(5))
    return password
