import secrets # we store our secret keys in another file somewhere else.

class Config:
    WTF_CSRF_ENABLED = True
    SECRET_KEY = secrets.forms # WTForms
