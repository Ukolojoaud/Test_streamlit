from bs4 import BeautifulSoup as bs
import requests
from csv import writer
import pandas as pd
url="https://nigeriapropertycentre.com/for-sale/lagos/alimosho"
 
page=requests.get(url)
 
soup=bs(page.content,'html.parser')
 
lists=soup.find_all('div',class_="wp-block property list")
with open('estate.csv','a+', encoding='utf-8', newline='') as f:
    thewriter=writer(f)
    header=['Title','Description','Location','Date','Price','Marketed']
    thewriter.writerow(header)
    
    for list in lists:
        title=list.find('div',class_="wp-block-title hidden-xs").text.replace('\n','')
        description=list.find('h4',class_="content-title").text.replace('\n','')
        location=list.find('address',class_="voffset-bottom-10").text.replace('\n','')
        date=list.find('span',class_="added-on").text.replace('\n','')
        price=list.find('span', class_="pull-sm-left").text.replace('\n','')
        marketed=list.find('span', class_="marketed-by pull-right hidden-xs hidden-sm text-right").text.replace('\n','')

        info=[title, description, location, date, price, marketed]
        
        thewriter.writerow(info)
