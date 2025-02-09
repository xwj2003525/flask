from app import db

class IdentityVerification(db.Model):
    __tablename__ = 'identity_verification'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    verified = db.Column(db.Boolean, nullable=False)
    verification_date = db.Column(db.DateTime, nullable=False)
    identity_label = db.Column(db.String(50),nullable=False)

