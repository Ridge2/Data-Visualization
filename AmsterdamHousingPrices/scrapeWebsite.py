import sys
from requests_html import HTMLSession
from requests import get
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv


url = 'https://www.remax.nl/Condo-Apartment/For-Sale/AMSTERDAM/#mode=gallery&tt=261&cr=2&mpts=536&pt=536&cur=EUR&sb=MostRecent&page=1&sc=8&pm=1513&lsgeo=175,1513,0,0&sid=4dfd0388-3602-4fe8-8e28-79c9f6d42e45'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
apartment_containers = html_soup.find_all('div', class_='gallery-item-container')

print(type(apartment_containers))
print(len(apartment_containers))

first_apartment = apartment_containers[0]
second_apartment = apartment_containers[1]

# Traverse apartments
find_apartment_special_feature = html_soup.find_all('div', {'class':'gallery-transtype'})
find_apartment_names = html_soup.find_all('div', {'class':'gallery-title'})
find_apartment_price = html_soup.find_all('div', {'class':'gallery-price'})
find_apartment_room = html_soup.find_all('div', {'class':'gallery-attr'})

apt_name = []
apt_feat = []
apt_price = []
apt_room = []
i = 0;

for special_feature in find_apartment_special_feature:
    apt_feat.insert(i, special_feature.text)

for names in find_apartment_names:
    apt_name.insert(i, names.text)

for price in find_apartment_price:
    apt_price.insert(i, price.text)

for rooms in find_apartment_room:
    apt_room.insert(i, rooms.text)

"""    
count = 0
for count in range(count, 24):
    print (apt_feat[count], apt_name[count], apt_price[count], apt_room[count])
    count = count + 1
"""

count = 0
restartCount = 0
csvFile = open('../AmsterdamHousingPrices/data.csv', 'w')
with csvFile:
    myFields = ['Special Feature', 'Apartment Location', 'Apartment Price', 'Room Specs']
    writer = csv.DictWriter(csvFile, fieldnames=myFields)
    writer.writeheader()
    while(count < 24):
        writer.writerow({'Special Feature' : apt_feat[count], 'Apartment Location' : apt_name[count], 'Apartment Price' : apt_price[count],'Room Specs' : apt_room[count]})
        count = count + 1
        restartCount = restartCount + 1
        if(restartCount == 4):
            restartCount = 0