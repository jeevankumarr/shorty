from app import db
from sqlalchemy.dialects.postgresql import JSON


class URL(db.Model):
    __tablename__ = 'url'
    original_url = db.Column(db.String())
    short_url = db.Column(db.String())
    create_ts = db.Column(db.TIMESTAMP)
    expiration_ts = db.Column(db.TIMESTAMP)
    user_id = db.Column(db.Integer)
    hits = db.Column(db.Integer, default=0)
    id = db.Column(db.Integer, primary_key=True)
    
    def __init__(self, *args, **kwargs):
        super(URL, self).__init__(*args, **kwargs)
    
    def __repr__(self):
        return 'Original URL: {0}, Short URL: {1}, User: {2}, Expires: {3}, Hits: {4}'.format(self.original_url, self.short_url, self.user_id, self.expiration_ts, self.hits)


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())
    create_ts = db.Column(db.TIMESTAMP)
    last_login = db.Column(db.TIMESTAMP)
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
    
    def __repr__(self):
        return 'User Id: {0}, Email: {1}, Created TS: {2}, Last Login: {3}'.format(user_id, email, create_ts, last_login)
    
