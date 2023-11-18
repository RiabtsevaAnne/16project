import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def image(url, folder_path):
    try:
        response = requests.get(url)
        type = response.headers['content-type']

        if 'image' not in type:
            print(f"URL {url} не містить малюнка.")
            return

        filename = os.path.join(folder_path, os.path.basename(urlparse(url).path))

        with open(filename, 'wb') as img_file:
            img_file.write(response.content)

        print(f"Малюнок {filename} успішно завантажено.")

    except Exception as e:
        print(f"Помилка при завантаженні малюнка з {url}: {e}")

def images(site_url, folder_path):
    try:
        response = requests.get(site_url)
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')

        img_tags = soup.find_all('img')

        for img_tag in img_tags:
            img_url = urljoin(site_url, img_tag['src'])
            image(img_url, folder_path)

    except Exception as e:
        print(f"Помилка при роботі з сайтом {site_url}: {e}")

def main():
    url = input("Введіть URL сайту для пошуку малюнків: ")
    folder = input("Введіть шлях до теки для збереження малюнків: ")

    os.makedirs(folder, exist_ok=True)

    images(url, folder)

if __name__ == "__main__":
    main()
