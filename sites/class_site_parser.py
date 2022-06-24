

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

import csv


class SiteParser:

    def __init__(self, url=""):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.services = Service('chromedriver.exe')

        self.driver = webdriver.Chrome(options=self.options, service=self.services)
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(35)

        # переходим на сайт
        self.driver.get(url)

        self.wait_el = WebDriverWait(self.driver, 10)

        self.sitename = url.split("/")[2].replace("www.", "").split(".")[0]
        
        # сохраняем результат в формате
        self.result = []
        self.result.append(("data", "time", "title", "desc", "price"))


    def save(self):
        # data time title desc price
        with open("Out\\" + self.sitename + ".csv", "w", newline="", encoding="utf8") as f:
            writer = csv.writer(f)
            writer.writerows(self.result)

