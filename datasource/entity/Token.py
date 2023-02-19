from UserManagementApp import db


class Token(db.Model):

    __tablename__ = 'token'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    value = db.Column(db.String(100), unique=True)
    expiresAt = db.Column(db.String(20))