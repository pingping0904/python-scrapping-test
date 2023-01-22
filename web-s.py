# from selenium import webdriver
# from BeautifulSoup4 import BeautifulSoup4
# import pandas as pd
#
# driver = webdriver.Chrome("https://www.petcare.se/hund/")
# article_id = []
# product_title = []
# ean_barcode = []
# product_description = []
# weight = []
# main_pic = []
# sub_pic = []
# prices = []
# category = []
import requests
import io

res = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')


with io.open('mydata.html', 'w', encoding="utf-8") as f:
    f.write(res.text)
print(res.text, res.status_code)
