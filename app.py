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

@app.route("/shorten", methods=["POST"])
def create_short_url():
    data = request.get_json()
    url = data.get("url")
    if not url:
        return jsonify({"error": "URL is required"}), 400

    short_code = generate_short_code()
    while URL.query.filter_by(short_code=short_code).first():
        short_code = generate_short_code()

    new_url = URL(url=url, short_code=short_code)
    db.session.add(new_url)
    db.session.commit()

    return jsonify({
        "id": new_url.id,
        "url": new_url.url,
        "shortCode": new_url.short_code,
        "createdAt": new_url.created_at.isoformat(),
        "updatedAt": new_url.updated_at.isoformat()
    }), 201

@app.route("/shorten/<short_code>", methods=["GET"])
def get_original_url(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()
    if not url_entry:
        return jsonify({"error": "Not found"}), 404

    url_entry.access_count += 1
    db.session.commit()

    return jsonify({
        "id": url_entry.id,
        "url": url_entry.url,
        "shortCode": url_entry.short_code,
        "createdAt": url_entry.created_at.isoformat(),
        "updatedAt": url_entry.updated_at.isoformat()
    }), 200