import requests
from bs4 import BeautifulSoup
import csv

#List of different pages

url_list = ['https://www.costco.co.uk/Appliances/Small-Kitchen-Appliances/Blenders-Juicers/c/cos_2.5.1',
            'https://www.costco.co.uk/Appliances/Small-Kitchen-Appliances/Coffee-Coffee-Capsules/c/cos_2.5.2']

#CHANGE THE NAME OF YOUR VARIABLE - I have it named costco.csv but you change it to another name if you want
with open('costco.csv', 'w') as costcowriter:
    csv_writer = csv.writer(costcowriter)
    csv_writer.writerow(['Product Name', 'Price', 'Product URL'])

for each_url in url_list:
    url = requests.get(each_url)
    soup = BeautifulSoup(url.text, 'lxml')

    products = soup.findAll('li', {'class':'product-item'})



    for each_product in products:
        name = each_product.find('div', {'class':'product-name-container'}).text.replace('\n', '').replace('"','')
        price = each_product.find('span', {'class':'product-price-amount'}).text.replace('\n', '').replace('"','')
        product_url = 'https://www.costco.co.uk' + each_product.find('a')['href'].replace('\n', '').replace('"','')
        print([name, price, product_url])
        #On each pass of each product, it will write to the CSV file.
        with open('costco.csv', 'a') as costcowriter:
            csv_writer = csv.writer(costcowriter)
            csv_writer.writerow([name, price, product_url])
