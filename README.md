# URL Shortener API – Innovaxel Assignment

This is a simple RESTful API built with **Flask** and **SQLite** for shortening long URLs into short, easy-to-share codes.

---

## 🚀 Features

- Create a short URL from a long URL
- Retrieve the original URL from a short code
- Update an existing shortened URL
- Delete a short URL
- Track access statistics (`accessCount`)

---

## 🛠️ Technologies Used

- **Python 3**
- **Flask** 
- **Flask-SQLAlchemy** 
- **SQLite** 

---

## 📂 Project Structure

- app.py # Main functionality
- models.py #URL model using SQLAlchemy
- requirements.txt # Project dependencies
- README.md #setup and usage guide
- .gitignore 
---


### 1. Clone the Repository

```bash
git clone https://github.com/Mahanoorfarooq/mahnoor-innovaxel-farooq.git
cd url-shortener-api
````


### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

### 3. Run the Flask Application

```bash
python app.py
```

You will see:

```
 * Running on http://127.0.0.1:5000/
```

---

## 📬 API Endpoints

| Method | Endpoint                     | Description            |
| ------ | ---------------------------- | ---------------------- |
| POST   | `/shorten`                   | Create a short URL     |
| GET    | `/shorten/<shortCode>`       | Retrieve original URL  |
| PUT    | `/shorten/<shortCode>`       | Update an existing URL |
| DELETE | `/shorten/<shortCode>`       | Delete a short URL     |
| GET    | `/shorten/<shortCode>/stats` | Get usage statistics   |

---

## 📫 Example Requests (JSON)

### 🔹 Create a Short URL

```http
POST /shorten
Content-Type: application/json

{
  "url": "https://example.com/long/url"
}
```

### 🔹 Retrieve Original URL

```http
GET /shorten/abc123
```

### 🔹 Update URL

```http
PUT /shorten/abc123
Content-Type: application/json

{
  "url": "https://example.com/updated"
}
```

### 🔹 Get Stats

```http
GET /shorten/abc123/stats
```

---

## 📈 Notes for Review

* All core API features are implemented and tested in **Postman**
* Code is modular and easy to read
* No external dependencies beyond Flask and SQLite

---



