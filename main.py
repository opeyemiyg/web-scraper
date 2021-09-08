from urllib.error import URLError

from bs4 import BeautifulSoup
from urllib import request
import json
from exceptions import PageNotFoundError

PAGE_URL="https://videx.comesconnected.com"

def get_page_html(url:str) -> str:
    '''requests url and raises Error if page is unaccessible'''
    try:
        return request.urlopen(url).read()
    except URLError:
        raise PageNotFoundError()


def get_page_options(page_object:BeautifulSoup):
    '''returns all page options requested as a list'''
    all_options_wrapper=page_object.find('div', class_='sections_wrapper')
    # returns list of page options if it exists, or none
    return all_options_wrapper and all_options_wrapper.find_all('div', class_=['col-xs-4','col-cs-4'])

def get_option_description(page_object:BeautifulSoup) -> str:
    '''returns individual option (description) with element div and class name'''
    return page_object.find('div', class_='package-name').get_text()

def get_option_discount(page_object:BeautifulSoup):
    '''returns individual option (discount) with element div and class name'''
    discount_object=page_object.find('div', class_='package-price').find('p')
    #return discount_object if it exists, or none
    return discount_object and discount_object.get_text().split()[1]

def get_option_title(page_object:BeautifulSoup) -> str:
    '''returns individual option (title) with element div and class name'''
    return page_object.find('h3').get_text()

def get_option_price(page_object:BeautifulSoup) -> str:
    '''returns ndividual option (price) with element div and class name'''
    return page_object.find('span', class_='price-big').get_text()

def extract_options(url:str) -> list:
    ''''extract all attributes of all options'''
    html_text = get_page_html(url)
    page_object = BeautifulSoup(html_text,features="html.parser")
    page_options=get_page_options(page_object)
    return [
        {
            'description': get_option_description(page_option),
            'title': get_option_title(page_option),
            'price': get_option_price(page_option),
            'discount': get_option_discount(page_option)
        }   for page_option in page_options
    ]

def main():
    ''''extract all attributes of all options'''
    html_text = get_page_html(PAGE_URL)
    page_object = BeautifulSoup(html_text, features="html.parser")
    page_options = get_page_options(page_object)
    options= [
        {
            'description': get_option_description(page_option),
            'title': get_option_title(page_option),
            'price': get_option_price(page_option),
            'discount': get_option_discount(page_option)
        } for page_option in page_options
    ]
    #Note: prints out options as a json string; currencies are encoded
    print(json.dumps(options, indent=4))

if __name__ == '__main__':
    main()