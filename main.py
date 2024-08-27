import requests
from bs4 import BeautifulSoup


def get_url():
    url: str = input("Enter the url: ")
    get_soup(url)


def get_soup(url):
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    links = get_links(soup)
    for link in links:
        print(link)


def get_links(soup):
    links = soup.find_all('a', href=True)
    return [link['href'] for link in links]


if __name__ == "__main__":
    get_url()
