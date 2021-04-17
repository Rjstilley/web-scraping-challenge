from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape_info():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    scrape_site = "https://redplanetscience.com/"

    browser.visit(scrape_site)

    html = browser.html
    soup = bs(html, 'html.parser')
    find_title = soup.find_all("div", class_="content_title")
    find_title = find_title[6].text
    find_para = soup.find_all("div", class_="article_teaser_body")
    find_para = find_para[6].text

    mars_dict = {
        "title": find_title,
        "para": find_para,
        "image": img_url,
        
    }

    return mars_dict


# x = scrape_info()
# print(x)
