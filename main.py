import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from config import Config, SelectorSberMarket, SberConfig
from models.product import ProductOrder
from utils.data import get_product, get_price


class SberMarket:
    def setup(self) -> webdriver:
        """
        Настройка хромдрайвера
        :return: Объект хромдрайвера
        """
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
    def fill_field(el, data: str):
        """
        Заполнение поля input с предварительной очисткой
        :param el: Объект input
        :param data: Данные для заполнения
        """
        el.clear()
        el.send_keys(Keys.CONTROL, 'a')
        el.send_keys(data)

    def fill_address(self):
        """
        Заполнение поля аддресс
        """
        address = self.driver.find_element(*SelectorSberMarket.INPUT_ADDRESS)
        self.fill_field(address, self.config.address)
        time.sleep(1)
        address.send_keys(Keys.ENTER)
        time.sleep(3)

    def search_product(self, product: ProductOrder):
        """
        Поиск продукта при помощи поисковой строки
        :param product: Модель продукта заказа
        """
        search_input = self.driver.find_element(*SelectorSberMarket.INPUT_SEARCH)
        self.fill_field(search_input, product.name)
        search_input.send_keys(Keys.ENTER)
        self.driver.set_page_load_timeout(self.config.timeout)

    def sort_product_by_price(self, sort_val: str):
        """
        Сортировка продуктов
        :param sort_val:
        :return:
        """
        search_input = self.driver.find_element(*SelectorSberMarket.SELECT_SORT)
        s = Select(search_input)
        for el in s.options:
            if el.text == sort_val:
                el.click()

    def go_to_shop(self):
        """
        Переход в Ленту и выбор товаров
        :return:
        """
        self.fill_address()
        self.driver.set_page_load_timeout(self.config.timeout)
        time.sleep(3)
        self.driver.find_element(*SelectorSberMarket.LENTA_SHOP).click()
        self.driver.set_page_load_timeout(self.config.timeout)

        for product in self.info_product:
            # Search product by name
            self.search_product(product)

            # Sort by price
            self.sort_product_by_price(self.sber_config.sort_cheaper)

    def start(self):
        """
        Точка входа робота
        """
        self.driver.get(self.url)
        time.sleep(5)
        self.go_to_shop()

    def close(self):
        """
        Закрытие хромедрайвера
        """
        if self.driver:
            self.driver.close()


if __name__ == "__main__":
    SberMarket().start()
    # a = get_product(Config.path_list_product)
    # a = get_price(r'')
    # print(a)
