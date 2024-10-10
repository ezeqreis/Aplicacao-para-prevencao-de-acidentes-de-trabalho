"""Patches that are applied at runtime to the virtual environment."""

import os
basedir=os.path.abspath(os.path.dirname(_file_))

class config:
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='segredo-muito-seguro'


