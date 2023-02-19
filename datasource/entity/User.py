from UserManagementApp import db
from datetime import datetime as dt
from datasource.entity.UserType import UserTypeEnum

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    pwd = db.Column(db.String(50), nullable=False)
    user_type = db.Column(db.Integer, db.ForeignKey('user_type.type'), nullable=False)
    created = db.Column(db.String(20), nullable=False)

    @staticmethod
    def createUserFromDto(dto):
        user = User()
        user.name = dto.name
        user.surname = dto.surname
        user.email = dto.email
        user.username = dto.username
        user.pwd = dto.password
        user.created = str(int(dt.now().timestamp()))
        user.user_type = UserTypeEnum.OBSERVER.value
        return user


