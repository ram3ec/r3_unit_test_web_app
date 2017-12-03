from flask import session
#не забывать при создании своего декоратора
from functools import wraps

def check_logged_in(func):
    #для идентификации функции интерпретатором
    @wraps(func)
    def wrapper(*agrs, **kwargs):
        if 'logged_id' in session:
            return func(*agrs, **kwargs)
        return 'You are not logged in.'
    return wrapper