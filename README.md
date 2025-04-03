# Quote Scraper API

This is a simple **Flask-based web scraping API** that extracts quotes from [Quotes to Scrape](https://quotes.toscrape.com/). The API scrapes quotes, authors, and tags, and returns the data in **JSON format**.

---

##  Features
- **Web scraping** using `requests` & `BeautifulSoup`
-  **REST API** built with Flask
-  **Pagination support** (`/quotes?page=2`)
-  **Error handling** for failed requests

---

##  Installation

### Clone the Repository
```bash
git clone https://github.com/your-username/QuoteScraperAPI.git
cd QuoteScraperAPI
```

### Create a Virtual Environment (Optional but Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Running the API
```bash
python main.py
```
You should see:
```
Running on http://127.0.0.1:5000/
```

---

## Usage

### Home Route
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

### Get Quotes
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

## License

This project is licensed under the **MIT License**.


---

## 💡 Contributions
Pull requests are welcome! If you find a bug or have suggestions, feel free to open an issue. Please support this repository, anything helps!

---

## 🌟 Acknowledgments
- [Quotes to Scrape](https://quotes.toscrape.com/) for providing test data
- Flask, Requests, and BeautifulSoup for making this possible
