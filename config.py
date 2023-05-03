import os
from selenium.webdriver.common.by import By


class Config:
    address = ''
    timeout = 10

    path_root_folder = os.path.abspath(os.curdir)
    path_chrome_driver = os.path.join(path_root_folder, 'support\\chromedriver.exe')
    path_list_product = os.path.join(path_root_folder, 'template\\data.txt')
    path_list_price = os.path.join(path_root_folder, 'template\\price.txt')


class SberConfig:
    sort_cheaper = 'Сначала дешевые'


class SelectorSberMarket:
    LENTA_SHOP = (By.XPATH, '//*[@id="__next"]/div[1]/div/div[2]/div/div[2]/div/div[3]/a')

    # Input selector
    INPUT_ADDRESS = (By.XPATH, '//*[@id="by_courier"]/div[1]/div/div[1]/div/div/input')
    INPUT_FIND = (By.XPATH, '//*[@id="__next"]/div[1]/header/div/div[3]/div/div/div[3]/div/div/div/form/input')
    INPUT_SEARCH = (By.XPATH, '//*[@id="__next"]/div[1]/header/div/div[3]/div/div/div[3]/div/div/div/form/input')


    # Select Field
    SELECT_SORT = (By.XPATH, '//*[@id="__next"]/div[1]/section[2]/div/div/aside/div/div[1]/select')
