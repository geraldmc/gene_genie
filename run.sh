#!/usr/bin/env bash

source ./venv/bin/activate
export FLASK_APP=gene_genie.py 
export FLASK_ENV=development
flask run -h localhost -p 8000
