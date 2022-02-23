
import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('/todo',__name__)

@bp.route('/<list_id>', methodes=["GET"])
def list(list_id):
    #check if the Id vaild and exists
    #Query to Select the wunted list from db
    #return the JSON_Object of lists or the codestatus 200/404
    return 'JSON_Object_list(list_id)'


@bp.route('/<list_id>',methods=["DELETE"])
def delete_list(list_id):
    #check if the Id vaild and exists
    #Query to delete the wunted list from db
    #return the JSON_Object of lists or the codestatus 200/404
    return 'JSON_Object_delete_list(list_id)'


@bp.route('/list',methods=["POST"])
def create_list():
    #check the Method and the Parameters
    #Query to Insert the new List
    #return the JSON_Object of the New List or code status 200/500
    return 'JSON_Object_create_list()'


@bp.route('/<list_id>/entry',methods=["POST"])
def add_entry():
    #check the Method and the Parameters
    #Query to Insert the new entry
    #return the JSON_Object of the New entry with id or code status 200/500
    return 'JSON_Object_add_entry()'


@bp.route('/<list_id>/entry/<entry_id>',methods=["POST"])
def update_entry():
    #check the Method and the Parameters
    #Query to Update the existed entry
    #return the JSON_Object of the List with the updated element or code status 200/500
    return 'JSON_Object_update_entry()'

@bp.route('/<list_id>/entry/<entry_id>',methods=["DELETE"])
def delete_entry():
    #check the Method and the Parameters
    #Query to delete the existed entry
    #return the JSON_Object of the List with out the deleted element or code status 200/500
    return 'JSON_Object_update_entry()'