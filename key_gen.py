import string
import random
from app import db
from app.models import URL

class KeyGenService():
    def __init__(self):
        pass
    def get_code(self):
        chars = string.ascii_letters + string.digits
        length = 5
        code = ''.join(random.choice(chars) for x in range(length))
        print('verifying', code)
        exists = db.session.query(db.exists().where(URL.short_url == code)).scalar()
        if not exists:
            print('New Code is ', code)
        return code
