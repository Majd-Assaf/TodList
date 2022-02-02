from crypt import methods
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('/users',__name__)

@app.route('/', methods=('GET'))
def get_users():
    #query to select all users from db
    #return JSON_Object of List of users
    return 'JSON_Object_get_users()'

@app.route('/user',methods=('POST',))
def add_user():
    #check the parameters and the metods
    #Query to insert new User in the db
    #return JESON Object of the new user
    return 'JSON_Object_add_user()'


@app.route('/user/<user_id>',methods=('POST',))
def add_user(user_id):
    #check the parameters and the metods
    #Query to delete the User from the db
    #return JESON Object of deleted user or statuscode 200/500
    return 'JSON_Object_add_user()'