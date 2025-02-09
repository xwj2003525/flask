from app import db
from datetime import datetime

class Report(db.Model):
    __tablename__ = 'report'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reason = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    status = db.Column(db.String(20), default='pending')

