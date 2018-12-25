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
    '''
    def __init__(self, original_url, short_url, create_ts, expiration_ts, user_id):
        self.original_url = original_url
        self.short_url = short_url
        self.create_ts = create_ts
        self.expiration_ts = expiration_ts
        self.user_id = user_id '''
    def __repr__(self):
        return 'Original URL: {0}, Short URL: {1}, User: {2}, Expires: {3}'.format(self.original_url, self.short_url, self.user_id, self.expiration_ts)
