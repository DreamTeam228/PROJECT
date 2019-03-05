from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

def Scrap(url, what_to_search, number_span):
    soup = bs(urlopen(url), 'html.parser')
    strings = soup.find_all(what_to_search)
    String = strings[number_span].string
    #print(strings)
    return String


#Urls = ['http://12yards.ru/%D0%BF%D1%80%D0%B0%D0%B9%D1%81/', 'https://www.luckylori.ru/']
#NameOfAnticafe = ['12 Ярдов', 'Lucky Lori']
#WebSite = ['http://12yards.ru/', 'https://www.luckylori.ru/']
#WhatToSearch = ['span', 'span']
#NumberOf = [0, 148]
#Remove = ['\xa0']
#Price = []


#print("+----------------------------------------------------+")
#for i in range (0, len(Urls)):
#    String = Scrap(Urls[i], WhatToSearch[i], NumberOf[i]) 
#    price = String.split(" ")
#    for n in range (0, len(Remove)):
#        Price.append(price[0].replace(Remove[n], ""))
#        print("|  Name: " + NameOfAnticafe[i])
#        print("|  Price: "   + Price[i])
#        print("|  WebSite: " + WebSite[i])
#    print("+----------------------------------------------------+")
