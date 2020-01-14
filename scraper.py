# import data from web
import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.co.uk/ASUS-XG49VQ-FreeSync-DisplayHDR400-AuraSync/dp/B07N4F132R?pf_rd_p=43a0c38b-793a-4c8f-8d81-3eec68ea2d41&pd_rd_wg=Hz27r&pf_rd_r=VYPHZ48DVFPDSJGPWE2A&ref_=pd_gw_wish&pd_rd_w=M2U8x&pd_rd_r=8c683cc4-ac08-4a4b-8fc3-9fda1c8e93cc&th=1'

headers = {"User-Agent":    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0'}

#return
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content,'html.parser')
soup2 = BeautifulSoup(soup.prettify(),"html.parser")

title = soup2.find(id="productTitle").get_text()
price = soup2.find(id="newBuyBoxPrice").get_text()

#Convert to 5th decimal
convert_price = price[-3]

print(title.strip())
print('Price:   ',price.strip())