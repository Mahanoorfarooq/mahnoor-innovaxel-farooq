# URL Shortener API

This is a simple RESTful API for shortening URLs using Flask and SQLite.

## Features
- Create short URLs
- Retrieve original URLs
- Update URLs
- Delete URLs
- Track access statistics

## Setup Instructions

```bash
git clone https://github.com/yourusername/mahnoor-innovaxel-farooq.git
cd url-shortener-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Test with Postman or Curl using endpoints:
- POST `/shorten`
- GET `/shorten/<shortCode>`
- PUT `/shorten/<shortCode>`
- DELETE `/shorten/<shortCode>`
- GET `/shorten/<shortCode>/stats`
