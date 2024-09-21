#!/bin/bash

# a) Install dependencies
pip install -r requirements.txt

# b) Run the application
FLASK_APP=app.py flask run &
