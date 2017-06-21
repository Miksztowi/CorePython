# -*- coding: utf-8 -*-
from selenium import webdriver
from scrapy import Selector
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def request():
    url = 'https://www.amazon.com/s/ref=nb_sb_noss_2?field-keywords=film'
    driver = webdriver.Firefox()
    driver.get(url)
    res_list = []
    selector = 'partial_link_text'
    locator = 'Next Page'
    for i in xrange(10):
        try:
            res_list.append(Selector(text=driver.page_source))
            if _is_visible(selector, driver, locator, timeout=5):
                driver.find_elements_by_partial_link_text('Next Page')[0].click()
        except:
            break
    driver.quit()
    print res_list
    return res_list


def pipeline():
    res_list = request()
    for res in res_list:
        pro_list = res.xpath('//*[@id="s-results-list-atf"]/li')
        print pro_list.xpath('//*[@class="a-size-base s-inline  s-access-title  a-text-normal"]/text()').extract()
        print pro_list.xpath('//*[@class="sx-price-whole"]/text()').extract()
        print pro_list.xpath('//*[@class="s-access-image cfMarker"]/@src').extract()
        print pro_list.xpath('//*[@class="a-icon-alt"]/text()').extract()


def _is_visible(selector, driver, locator, timeout=5):
    if selector == 'partial_link_text':
        try:
            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, locator)))
            return True
        except TimeoutException:
            return False
    elif selector == 'xpath':
            try:
                WebDriverWait(driver, timeout).until(
                    EC.visibility_of_element_located((By.XPATH, locator)))
                return True
            except TimeoutException:
                return False


if __name__ == '__main__':
    pipeline()