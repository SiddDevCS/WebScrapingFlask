from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# function to scrape quotes from a specific page
def scrape_quotes(page=1):
    url = f"https://quotes.toscrape.com/page/{page}/"
    # where to fetch the quotes from

    # check if the page number is valid
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise error for HTTP errors (e.g., 404, 500)
    except requests.RequestException as e:
        return {"error": f"Failed to fetch data: {str(e)}"}

    # parsing HTML content using bs4
    soup = BeautifulSoup(response.text, 'html.parser')
    
    quotes = []
    for quote_div in soup.find_all("div", class_="quote"):
        text = quote_div.find("span", class_="text").text
        author = quote_div.find("small", class_="author").text
        tags = [tag.text for tag in quote_div.find_all("a", class_="tag")]
        
        quotes.append({
            "text": text,
            "author": author,
            "tags": tags
        })

    # check if there are no quotes (end of pages)
    if not quotes:
        return {"message": "No more quotes available."}

    return quotes

# root route to welcome users
@app.route('/')
def home():
    return "Welcome to the Quote Scraper API! Visit /quotes to get the scraped quotes."

# API route to get quotes
@app.route('/quotes', methods=['GET'])
def get_quotes():
    page = request.args.get('page', 1, type=int)  # Get 'page' from URL query, default = 1
    data = scrape_quotes(page)
    return jsonify(data)

# run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
