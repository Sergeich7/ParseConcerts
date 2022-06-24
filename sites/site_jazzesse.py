"""

Класс парсит сайт jazzesse.ru
нужно передать родителю урл

и добавить метод parse где будут получаться данные
self.result = []
self.result.append(("data", "time", "title", "desc", "price"))



"""

from .class_site_parser import SiteParser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

class SiteJazzesseClass(SiteParser):

    def __init__(self):
        super().__init__("https://www.jazzesse.ru/#afisha")

    def parse(self):
        fl_parse_page = True
        while fl_parse_page:
            # находим все артикли на странице
            xpath_pattern = "//div[@class='afishaItemBottom']"
            self.wait_el.until(EC.visibility_of_element_located((By.XPATH, xpath_pattern)))
            el_articles = self.driver.find_elements(By.XPATH, value=xpath_pattern)
            print(f"{self.sitename} {len(el_articles)}")
            # разбираем артикли
            for el_article in el_articles:
                self.result.append((
                    el_article.find_element(By.XPATH, value=".//div[@class='day']").text,
                    el_article.find_element(By.XPATH, value=".//div[@class='houre']").text,
                    el_article.find_element(By.XPATH, value=".//a").text,
                    el_article.find_element(By.XPATH, value=".//div[@class='desc']").text,
                    el_article.find_element(By.XPATH, value=".//div[@class='minprice']").text
                    ))
            try:
                # если есть продолжение в следуещем месяце, то кликаем на следующую страницу
                xpath_pattern = "//div[@class='arrow second_arrow next_month ']"
                self.wait_el.until(EC.visibility_of_element_located((By.XPATH, xpath_pattern)))
                el_next_month = self.driver.find_element(By.XPATH, value=xpath_pattern)
                wbd = webdriver.ActionChains(self.driver).move_to_element(el_next_month)
                time.sleep(1)
                wbd.click(el_next_month).perform()
                time.sleep(2)
            except:
                # если невозможно (кнопка disabled) выбрать следующую страницу - выходим
                fl_parse_page = False

