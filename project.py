import requests
from bs4 import BeautifulSoup
import json

def count_word_frequency(url):
    # Отримуємо вміст веб-сторінки
    response = requests.get(url)
    content = response.text

    # Парсимо HTML вміст
    soup = BeautifulSoup(content, 'html.parser')

    # Отримуємо текст сторінки та розбиваємо його на слова
    words = soup.get_text().split()

    # Підраховуємо частоту кожного слова
    word_frequency = {}
    for word in words:
        word = word.lower()  # Перетворюємо слово в нижній регістр
        word_frequency[word] = word_frequency.get(word, 0) + 1

    return word_frequency

def main():
    # Список URL-адрес сайтів, які вам потрібно проаналізувати
    sites = ['https://example.com/site1', 'https://example.com/site2']

    # Список ключових слів
    keywords = ['keyword1', 'keyword2', 'keyword3', 'keyword4']
    results = {}

    for site in sites:
        site_results = {}
        for keyword in keywords:
            keyword_frequency = count_word_frequency(site)
            site_results[keyword] = keyword_frequency.get(keyword, 0)
        results[site] = site_results

    with open('results.json', 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
