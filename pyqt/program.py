from scrap import Scrap, convertUrl
from modules import anticafe, zoo

anticafe = anticafe()
zoo = zoo()

Urls = anticafe.Url()
WhatToSearch = anticafe.Search()
NumberOf = anticafe.NumberOfBlockPrice()
NameOf = anticafe.Name()
WebSite = anticafe.WebSite()
Remove = anticafe.Remove()


Price = []
Soup = []

print("+----------------------------------------------------+")

for i in range (0, len(Urls)):
    Soup.append(Urls[i])
    String = Scrap(Soup[i], WhatToSearch[i], NumberOf[i])
    price = String.split(" ")
    for n in range (0, len(Remove)):
        Price.append(price[0].replace(Remove[n], ""))
    print("|  Name: " + NameOf[i])
    print("|  Price: "   + Price[i])
    print("|  WebSite: " + WebSite[i])
    print("+----------------------------------------------------+")

Urls = zoo.Url()
WhatToSearch = zoo.Search()
NumberOf = zoo.NumberOfBlock()
NameOf = zoo.Name()
WebSite = zoo.WebSite()
Remove = zoo.Remove()
price = "string"

for i in range (0, len(Urls)):
    price = Scrap(Urls[i], WhatToSearch[i], NumberOf[i]) 
    for n in range (0, len(Remove)):
        Price.append(price[0].replace(Remove[n], ""))
    print("|  Name: " + NameOf[i])
    print("|  Price: "   + price)
    print("|  WebSite: " + WebSite[i])
    #print("Number phone, location, metro")
    print("+----------------------------------------------------+")