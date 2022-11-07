import time
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CHAR, VARCHAR, Column, Integer, ForeignKey, String
from sqlalchemy.orm import sessionmaker
import csv
from bs4 import BeautifulSoup
import requests




##################################################################################
url = "https://finance.yahoo.com/currencies?.tsrc=fin-srch"
req = requests.get(url)
req.encoding = "utf-8"
soup = BeautifulSoup(req.text, "html.parser")
##################################################################################

while True:

    
    euro_list = []
    yen_list = []
    thai_list = []

    courses_euro = soup.find_all('fin-streamer',{'data-symbol':'EURUSD=X'})
    for i in courses_euro:
        euro_list.append(i.string)
        

    courses_yen = soup.find_all('fin-streamer',{'data-symbol':'JPY=X'})
    for i in courses_yen:
        yen_list.append(i.string)

    courses_thai = soup.find_all('fin-streamer',{'data-symbol':'THB=X'})
    for i in courses_thai:
        thai_list.append(i.string)

    print(euro_list)
    print(yen_list)
    print(thai_list)
    
    time.sleep(5)




# result = session.query(Students_table.f_name).all()
# print(result)