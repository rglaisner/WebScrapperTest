// feature/initial-project-setup
import requests
from bs4 import BeautifulSoup
import datetime
import json
import csv
from urllib.parse import urlparse

def fetch_page(url):
    """Fetches the content of a web page.

    Args:
        url: The URL of the web page to fetch.

    Returns:
        The content of the web page as a string, or None if the request fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_books(html_content):
    """Parses the HTML of books.toscrape.com to extract book information.

    Args:
        html_content: The HTML content of the web page.

    Returns:
        A list of dictionaries, where each dictionary represents a book.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    books = []
    for article in soup.find_all('article', class_='product_pod'):
        title = article.h3.a['title']
        price = article.find('p', class_='price_color').text
        rating = article.p['class'][1]  # The rating is in the second class name
        books.append({'title': title, 'price': price, 'rating': rating})
    return books

def save_to_json(data, url):
    """Saves data to a JSON file.

    Args:
        data: The data to save (a list of dictionaries).
        url: The URL that was scraped, used for generating the filename.
    """
    if not data:
        return

    domain = urlparse(url).netloc.replace('.', '-')
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = f"{domain}-{date_str}.json"

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")

def save_to_csv(data, url):
    """Saves data to a CSV file.

    Args:
        data: The data to save (a list of dictionaries).
        url: The URL that was scraped, used for generating the filename.
    """
    if not data:
        return

    domain = urlparse(url).netloc.replace('.', '-')
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = f"{domain}-{date_str}.csv"

    with open(filename, 'w', newline='') as f:
        if data:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    print(f"Data saved to {filename}")

def main():
    """Main function to run the web scraper."""
    target_url = "http://books.toscrape.com/"
    print(f"Scraping {target_url}...")
    html_content = fetch_page(target_url)
    if html_content:
        books = parse_books(html_content)
        if books:
            print(f"Successfully scraped {len(books)} books.")
            save_to_json(books, target_url)
            save_to_csv(books, target_url)
        else:
            print("Could not parse any books.")
        print("Scraping successful.")
    else:
        print("Scraping failed.")

if __name__ == "__main__":
    main()
# Main application file for the web scraper.
