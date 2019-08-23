# -*- coding: utf-8 -*-

import json, random, sys
from flask import render_template
from flask import request, make_response
from flask import jsonify, abort  

from app import app
from app.api.stringdb_api import StringDB_API
from app.api.uniprot_api import UniProt_API
from app.utils import *

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Gerald'}
    title='Home'
    #return user['username']
    return render_template('template_index.html', 
                            user=user['username'], 
                            title=title)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)