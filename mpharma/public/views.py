# -*- coding: utf-8 -*-                                                                                                             [15/600]
"""Public section, including homepage and signup."""
from flask import Blueprint, render_template


blueprint = Blueprint('public', __name__, template_folder='../../templates')


@blueprint.route('/')
def home():
    """Home page."""
    return render_template('index.html')
