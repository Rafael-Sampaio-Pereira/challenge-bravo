from flask import Flask, request, make_response, jsonify
from flask_login import LoginManager, login_user, logout_user, current_user
from models.user import User




class AuthController(object):

    def selectOneById(self, user_id):
        return User.query.filter_by(id=user_id).first()

    def selectOneByEmail(self, email):
        return User.query.filter_by(email=email).first()

    def validateUserAndStartSession(self, request, _user):
        email = request.json['email']
        password = request.json['password']
        if email == _user.email and password == _user.password:
            login_user(_user, remember=False)
            return make_response(jsonify({"message": "Login successfull"}), 200)
        else:
            return make_response(jsonify({"message": "Login failed! Please verify your credentials and try again."}), 401)

    def closeSession(self):
        if current_user.is_authenticated:
            logout_user()
            return make_response(jsonify({"message": "User logged out"}), 200)
        else:
            return make_response(jsonify({"message": "User is not logged"}), 403)

