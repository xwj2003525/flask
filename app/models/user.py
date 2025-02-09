from app import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    icon_path = db.Column(db.String(255), nullable=False)
    self_info = db.Column(db.Text, nullable=False)
    privacy_settings = db.Column(db.String(20), nullable=False)  
    activity_level = db.Column(db.String(20), nullable=False)    
    identity = db.Column(db.String(20), nullable=False)          




