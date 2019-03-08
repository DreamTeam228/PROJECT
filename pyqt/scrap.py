from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

def convertUrl(url):
    soup = bs(urlopen(url), 'html.parser')
    return soup

def Scrap(soup, what_to_search, number_span):
    strings = soup.find_all(what_to_search)
    String = strings[int(number_span)].get_text(strip=True)
    for i in range (0, len(strings)):
        print("id" + str(i))
        print(strings[i])
    return String



if __name__ == "__main__":
    #Url = 'https://www.moscowzoo.ru/for-visitors/tickets/'
    #Url = 'http://12yards.ru/%d0%ba%d0%be%d0%bd%d1%82%d0%b0%d0%ba%d1%82%d1%8b/'#'https://www.luckylori.ru/'
    Url = 'https://www.luckylori.ru/'
    WhatToSearch = 'span'#'h3'#'strong'
    NumberOf = [5]#3#14ok#17ok
    prices = []
    ex = convertUrl(Url)
    for i in range(0,1):
        price = (Scrap(ex, WhatToSearch, NumberOf[i]))
        price = price.replace("\xa0", "")
        price = price.replace(" ", "")
        prices.append(price)
    print(prices)


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
