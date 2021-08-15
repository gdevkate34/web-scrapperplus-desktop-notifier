import requests
from bs4 import BeautifulSoup
import sqlite3
from plyer import notification

conn = sqlite3.connect('vocab.db')
URL = ["https://www.indiabix.com/current-affairs/2021-06-01/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-02/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-03/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-04/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-05/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-06/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-07/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-08/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-09/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-10/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-11/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-12/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-13/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-14/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-15/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-16/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-17/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-18/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-19/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-20/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-21/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-22/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-23/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-24/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-25/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-26/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-27/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-28/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-29/"\
    ,"https://www.indiabix.com/current-affairs/2021-06-30/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-01/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-02/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-03/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-04/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-05/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-06/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-07/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-08/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-09/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-10/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-11/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-12/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-13/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-14/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-15/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-16/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-17/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-18/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-19/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-20/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-21/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-22/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-23/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-24/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-25/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-26/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-27/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-28/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-29/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-30/"\
    ,"https://www.indiabix.com/current-affairs/2021-07-31/"\
    ,"https://www.indiabix.com/current-affairs/2021-08-01/"\
    ,"https://www.indiabix.com/current-affairs/2021-08-02/"\
    ,"https://www.indiabix.com/current-affairs/2021-08-03/"\
    ,"https://www.indiabix.com/current-affairs/2021-08-04/"\
    ,"https://www.indiabix.com/current-affairs/2021-08-05/"\
    ,"https://www.indiabix.com/current-affairs/2021-08-06/"\
    ,"https://www.indiabix.com/current-affairs/2021-08-07/"\
    ,"https://www.indiabix.com/current-affairs/2021-08-08/"\
    ,"https://www.indiabix.com/current-affairs/2021-08-09/"\
    ,"https://www.indiabix.com/current-affairs/2021-08-10/"\
    ,"https://www.indiabix.com/current-affairs/2021-08-11/"\
    ,"https://www.indiabix.com/current-affairs/2021-08-12/"\
    ,"https://www.indiabix.com/current-affairs/2021-08-13/"]

current_affairs =[]
for url in URL:
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    mydivs = soup.find_all("div", {"class": "bix-ans-description"})

    for i in mydivs:
        current_affairs.append(i.text)

print(len(current_affairs))

conn =None
try:
    conn = sqlite3.connect('ca.db')
    print("Connected to db")
except:
    print("Error occurred!")

cursor = conn.cursor()

sql ='''CREATE TABLE IF NOT EXISTS Titles(
   Title TEXT NOT NULL
)'''
cursor.execute(sql)

for i in current_affairs:
    cursor.execute("INSERT INTO Titles(Title) VALUES (?)",(i,))
    # print("* ",i)

conn.commit()


