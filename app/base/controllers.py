# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify

import pprint

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.base.forms import LoginForm

# Import module models (i.e. User)
from app.base.models import RiskField, RiskFieldType, RiskType, RiskTypeSchema, RiskFieldTypeSchema, RiskFieldSchema

# Define the blueprint: 'auth', set its url prefix: app.url/auth
base = Blueprint('base', __name__, url_prefix='/base', static_folder='static')

# Set the route and accepted methods
@base.route('/signin/', methods=['GET', 'POST'])
def signin():

    return render_template("base/signin.html", )

from flask_json import JsonError, json_response, as_json
from sqlalchemy.exc import IntegrityError

@base.route('/risktype/<int:pk>', methods=['GET'])
def api(pk):
    try:
        risktype = RiskType.query.get(pk)
        riskfields = risktype.riskFields.all()
    except IntegrityError:
        return jsonify({"message": "Author could not be found."}, 400)

    properties = []
    for riskfield in riskfields:
        riskfields_schema = RiskFieldSchema()
        properties.append(riskfields_schema.dump(riskfield)[0])
               
    risktype_data = {
        'id': risktype.id,
        'risktype': risktype.riskType,
        'fields':properties
    }    
    
    return jsonify([ risktype_data ])

@base.route('/risktype/all/', methods=['GET'])
def all():
    try:
        risktypes = RiskType.query.all()
    except IntegrityError:
        return jsonify({"message": "Author could not be found."}, 400)
    riskfields_schema = RiskFieldSchema(many=True)
    
    risktypes_data = []
    for risktype in risktypes:
        risktype_data = {}
        risktype_data['id']= risktype.id
        risktype_data['risktype'] = risktype.riskType
        riskfields = risktype.riskFields.all()

        properties = []
        for riskfield in riskfields:
            riskfields_schema = RiskFieldSchema()
            properties.append(riskfields_schema.dump(riskfield)[0])

        
        risktype_data['fields'] = properties
        risktypes_data.append( risktype_data )
        
    return jsonify(risktypes_data)
    
