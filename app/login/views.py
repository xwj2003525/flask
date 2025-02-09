from flask import render_template
from . import login_blueprint

@login_blueprint.route('/')
def login():
    return render_template('login/index.html')


