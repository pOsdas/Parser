import bs4
import requests
from bs4 import BeautifulSoup


def get_url() -> None:
    url: str = input("Enter the url: ")
    domain: str = input("Enter the domain to filter (leave empty for all links): ")
    get_soup(url, domain)


def get_soup(url: str, domain: str) -> None:
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    links = get_links(soup, domain)
    for link in links:
        print(link)
    # check_links(links)


def get_links(soup, domain) -> list:
    links = soup.find_all('a', href=True)
    filtered_links = []
    for link in links:
        href = link['href']
        if domain in href or not domain:
            filtered_links.append(href)
    return filtered_links


def check_links(links: list) -> None:
    for link in links:
        try:
            response = requests.get(link)
            if response.status_code == 200:
                print(f"Available link: {link}")
            else:
                print(f"Unavailable link: {link} (Status code: {response.status_code})")

        except requests.RequestException as e:
            print(f"Error with {link}: {e}")


if __name__ == "__main__":
    get_url()
