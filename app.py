from flask import Flask, request, jsonify
from models import db, URL
from datetime import datetime
import string, random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db.init_app(app)

with app.app_context():
    db.create_all()

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))