import requests
from bs4 import BeautifulSoup


def print_headlines(response_text):
    soup = BeautifulSoup(response_text, 'lxml')
    headlines = soup.find_all(attrs={"itemprop": "headline"})
    for headline in headlines:
        print(headline.text)


url = 'https://inshorts.com/en/read' # I have used Inshorts for scraping. Any news website can be used
response = requests.get(url)
print_headlines(response.text)
