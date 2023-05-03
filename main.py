import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from utils.data import get_product, get_price
from config import Config, SelectorSberMarket, SberConfig


class SberMarket:
    def setup(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_experimental_option("detach", True)
        return webdriver.Chrome(
            executable_path=self.config.path_chrome_driver,
            chrome_options=chrome_options
        )

    def __init__(self):
        self.config = Config()
        self.sber_config = SberConfig()
        self.url = r'https://sbermarket.ru/'
        self.info_product = get_product(self.config.path_list_product)
        self.info_price = get_price(self.config.path_list_price)
        self.driver = self.setup()

    def __del__(self):
        if self.driver:
            self.close()

    @staticmethod
    def fill_field(el, data):
        el.clear()
        el.send_keys(Keys.CONTROL, 'a')
        el.send_keys(data)

    def fill_address(self):
        address = self.driver.find_element(*SelectorSberMarket.INPUT_ADDRESS)
        self.fill_field(address, self.config.address)
        time.sleep(1)
        address.send_keys(Keys.ENTER)
        time.sleep(3)

    def search_product(self, product):
        search_input = self.driver.find_element(*SelectorSberMarket.INPUT_SEARCH)
        self.fill_field(search_input, product.name)
        search_input.send_keys(Keys.ENTER)
        self.driver.set_page_load_timeout(self.config.timeout)

    def sort_product_by_price(self, sort_val: str):
        search_input = self.driver.find_element(*SelectorSberMarket.SELECT_SORT)
        s = Select(search_input)
        for el in s.options:
            if el.text == sort_val:
                el.click()

    def go_to_shop(self):
        self.fill_address()
        self.driver.set_page_load_timeout(self.config.timeout)
        time.sleep(3)
        self.driver.find_element(*SelectorSberMarket.LENTA_SHOP).click()
        self.driver.set_page_load_timeout(self.config.timeout)

        for product in self.info_product:
            # try
            # Search product by name
            self.search_product(product)

            # Sort by price
            self.sort_product_by_price(self.sber_config.sort_cheaper)


            print()

    def get_info(self):
        self.driver.get(self.url)
        time.sleep(5)
        self.go_to_shop()

    def close(self):
        if self.driver:
            self.driver.close()


if __name__ == "__main__":
    # SberMarket().get_info()
    # a = get_product(Config.path_list_product)
    a = get_price(r'')
    print(a)
