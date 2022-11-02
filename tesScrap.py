import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import csv 

#link yohaneskosek
main_link = 'https://shopee.co.id/yohaneskosek#product_list'
path = r'C:\Users\IHSAN W\OneDrive\Documents\ITS\SEM 3\Belajar Python\chromedriver.exe'

#customize chrome display 
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--headless')
chrome_options.add_argument('disable-notifications')
chrome_options.add_argument('--disable-infobars')
chrome_service = Service('chromedriver.exe')


driver = webdriver.Chrome(executable_path = path, options = chrome_options, service = chrome_service)
driver.get(main_link)

html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(html, "html.parser")

#product name 
product_name = soup.find_all('div', class_ = '_3Gla5X _2j2K92 _3j20V6')

#product price
product_price = soup.find_all('div', class_ = '_3w3Slt _1NAEoM')

#total terjual
product_sold = soup.find_all('div', class_ = '_2Tc7Qg _2R-Crv')


# #looping
product_name, product_price, product_sold = [], [], []

#product name 
for i in soup.find_all('div', class_ = '_3Gla5X _2j2K92 _3j20V6'):
    product_name.append(i.text)

#product price
for i in soup.find_all('div', class_ = '_3w3Slt _1NAEoM'):
    product_price.append(i.text)

#total terjual
for i in soup.find_all('div', class_ = '_2Tc7Qg _2R-Crv'):
    product_sold.append(i.text)



# #many pages
product_name, product_price, product_sold = [], [], []

for page in range(0, 1):
    main_link = 'https://shopee.co.id/yohaneskosek?page={}&sortBy=pop'.format(page)
    driver.get(main_link)
    

    #product name 
    for i in soup.find_all('div', class_ = '_3Gla5X _2j2K92 _3j20V6'):
        product_name.append(i.text)

    #product price
    for i in soup.find_all('div', class_ = '_3w3Slt _1NAEoM'):
        product_price.append(i.text)

    #total terjual
    for i in soup.find_all('div', class_ = '_2Tc7Qg _2R-Crv'):
        product_sold.append(i.text)


# #save data 
listCols = ['product_name', 'product_price', 'product_sold']
dict_data = dict(zip(
            listCols,
                (product_name, 
                product_price, 
                product_sold)
))

import json
with open('yohaneskosek.json', 'w') as fp:
    json.dump(dict_data, fp)


a = {'Nama Produk': product_name, 'Harga Produk': product_price, 'Produk Terjual': product_sold}
df = pd.DataFrame.from_dict(a, orient = 'index')
df = df.transpose()
df.to_excel('list.xlsx')

# #using API
# import requests
# shopee_url = 'https://shopee.co.id'
# keyword = 'iphone xs'
# header = {
#     'User-Agent' : 'Chrome',
#     'Referer' : '{}search?keyword={}'.format(shopee_url, keyword)
# }
# url = 'https://shopee.co.id/api/v4/search/search_items?by=relevancy&keyword={}&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2&view_session_id=dcfa1958-8f8b-44bc-9133-094c3bf4f69a'.format(keyword)

# #API requests
# r = requests.get(url, headers = header).json()

# #scraping
# col_list, price_list, sold_list, rating_list = [],[],[],[] 
# for item in r['items']:
#     col_list.append(item['item_basic']['name'])
#     price_list.append(item['item_basic']['price'])
#     sold_list.append(item['item_basic']['sold'])
#     rating_list.append(item['item_basic']['rating'])

