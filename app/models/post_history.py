from app import db
from datetime import datetime

class PostHistory(db.Model):
    __tablename__ = 'post_history'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    old_content = db.Column(db.Text)
    new_content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.now)

