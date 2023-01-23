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
from bs4 import BeautifulSoup

# Make a request

page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Extract first <h1>(...)</h1> text
first_h1 = soup.select('h1')[0].text

