import unittest
from bs4 import BeautifulSoup

from exceptions import PageNotFoundError
from main import PAGE_URL, get_page_html, get_page_options, get_option_description, get_option_title, get_option_price, \
    get_option_discount


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        bad_html_text = get_page_html('https://jsonplaceholder.typicode.com/')
        self.bad_page_object = BeautifulSoup(bad_html_text, features="html.parser")
        self.bad_page_options = get_page_options(self.bad_page_object)

        html_text = get_page_html(PAGE_URL)
        self.page_object = BeautifulSoup(html_text, features="html.parser")
        self.page_options = get_page_options(self.page_object)

    def test_get_page_html(self):
        response=get_page_html(PAGE_URL)
        self.assertIsInstance(response,bytes)
        self.assertIn(b'<!doctype html>',response)

    def test_get_page_html_raises_error_with_incorrect_url(self):
        self.assertRaises(PageNotFoundError, get_page_html,'https://videx.comesconnected.com/bad')

    def test_get_page_options(self):
        page_options = get_page_options(self.page_object)
        self.assertIsInstance(page_options,list)
        self.assertEqual(len(page_options),6)

    def test_get_page_options_return_none_with_no_options_in_page(self):
        page_options = get_page_options(self.bad_page_object)
        self.assertIsNone(page_options)


    def test_get_option_description(self):
        description=get_option_description(self.page_options[0])
        self.assertIsInstance(description,str)
        self.assertIn('Up to 40 minutes talk',description)

    def test_get_option_title(self):
        title=get_option_title(self.page_options[0])
        self.assertIsInstance(title,str)
        self.assertIn('Option 40',title)

    def test_get_option_price(self):
        price=get_option_price(self.page_options[0])
        self.assertIsInstance(price,str)
        self.assertEqual('£6.00',price)

    def test_get_option_discount(self):
        discount=get_option_discount(self.page_options[3])
        self.assertIsInstance(discount,str)
        self.assertEqual('£5',discount)

    def test_get_option_discount_with_no_discount(self):
        discount=get_option_discount(self.page_options[0])
        self.assertIsNone(discount)

if __name__ == '__main__':
    unittest.main()
