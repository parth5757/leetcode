import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# Function to get grammar content from a URL
def get_grammar_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    content = ' '.join([para.text for para in paragraphs])
    return content

# Function to scrape and save grammar content
def scrape_grammar_content():
    urls = [
        "https://en.wikipedia.org/wiki/Grammar",
        "https://en.wikipedia.org/wiki/English_grammar",
        # Add more URLs as needed
    ]

    data = []
    for url in urls:
        content = get_grammar_content(url)
        data.append({'URL': url, 'Content': content})

    # Load existing data if file exists
    if os.path.exists('grammar_content.csv'):
        existing_data = pd.read_csv('grammar_content.csv')
        data = existing_data.append(data, ignore_index=True)

    df = pd.DataFrame(data)
    df.to_csv('grammar_content.csv', index=False)
    print("Content saved to 'grammar_content.csv'.")

# Function to run the script periodically
def run_periodically(interval=3600):
    while True:
        scrape_grammar_content()
        time.sleep(interval)

# Run the script
if __name__ == "__main__":
    # Run the scraper periodically (e.g., every hour)
    run_periodically(interval=3600)  # 3600 seconds = 1 hour
