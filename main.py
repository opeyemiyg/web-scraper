from bs4 import BeautifulSoup
from urllib import request
PAGE_URL="https://videx.comesconnected.com/"


def get_page_html(url:str) -> str:
    return request.urlopen(url).read()

def main():
    html_text = get_page_html(PAGE_URL)
    soup = BeautifulSoup(html_text)
    print(soup.prettify())



if __name__ == '__main__':
    main()