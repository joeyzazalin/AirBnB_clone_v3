#!/usr/bin/python3
"""
create flask app blueprint
"""
from flask import blueprint
from api.v1.view.index import *

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
