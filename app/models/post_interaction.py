from app import db
from datetime import datetime

class PostInteraction(db.Model):
    __tablename__ = 'post_interaction'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_from_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_to_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comment = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.now)

