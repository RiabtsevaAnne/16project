import requests
from bs4 import BeautifulSoup
import json

def count(url):
    response = requests.get(url)
    content = response.text

    soup = BeautifulSoup(content, 'html.parser')

    words = soup.get_text().split()

    word_frequency = {}
    for word in words:
        word = word.lower()  
        word_frequency[word] = word_frequency.get(word, 0) + 1

    return word_frequency

def main():
    sites = ['https://example.com/site1', 'https://example.com/site2']

    keywords = ['keyword1', 'keyword2', 'keyword3', 'keyword4']
    results = {}

    for site in sites:
        site_results = {}
        for keyword in keywords:
            keyword_frequency = count(site)
            site_results[keyword] = keyword_frequency.get(keyword, 0)
        results[site] = site_results

    with open('results.json', 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
