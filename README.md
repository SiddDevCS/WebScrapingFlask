# Quote Scraper API

This is a simple **Flask-based web scraping API** that extracts quotes from [Quotes to Scrape](https://quotes.toscrape.com/). The API scrapes quotes, authors, and tags, and returns the data in **JSON format**.

---

## 🚀 Features
- 📡 **Web scraping** using `requests` & `BeautifulSoup`
- 🌍 **REST API** built with Flask
- 📑 **Pagination support** (`/quotes?page=2`)
- ⚠️ **Error handling** for failed requests

---

## 🛠 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/QuoteScraperAPI.git
cd QuoteScraperAPI
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the API
```bash
python main.py
```
You should see:
```
Running on http://127.0.0.1:5000/
```

---

## 🔥 Usage

### 1️⃣ Home Route
- **Endpoint:** `GET /`
- **Response:** Welcome message

Example:
```
http://127.0.0.1:5000/
```
Response:
```json
{"message": "Welcome to the Quote Scraper API! Visit /quotes to get the scraped quotes."}
```

### 2️⃣ Get Quotes
- **Endpoint:** `GET /quotes`
- **Query Params:** `page` (default = 1)
- **Response:** JSON list of quotes

Example:
```
http://127.0.0.1:5000/quotes
```
Response:
```json
[
    {
        "text": "The greatest glory in living lies not in never falling, but in rising every time we fall.",
        "author": "Nelson Mandela",
        "tags": ["inspirational"]
    }
]
```

**Paginated Requests:**
```
http://127.0.0.1:5000/quotes?page=2
```

---

## 📜 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

... (standard MIT license text) ...
```

---

## 💡 Contributions
Pull requests are welcome! If you find a bug or have suggestions, feel free to open an issue.

---

## 🌟 Acknowledgments
- [Quotes to Scrape](https://quotes.toscrape.com/) for providing test data
- Flask, Requests, and BeautifulSoup for making this possible
