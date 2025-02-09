from app import db
from datetime import datetime

class PostExpiry(db.Model):
    __tablename__ = 'post_expiry'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    expiration_date = db.Column(db.DateTime)
    expired = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)

