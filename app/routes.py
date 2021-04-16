from flask import render_template, redirect

from app import db
from app import app
from app.forms import Form
# Make sure to import all tables
from app.models import User

@app.route("/", methods=['GET', 'POST'])
def home():
    """
    
    """
    form=Form()
    

