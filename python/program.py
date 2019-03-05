from scrap import Scrap
from modules import anticafe

anticafe = anticafe()

Urls = anticafe.Url()
WhatToSearch = anticafe.Search()
NumberOf = anticafe.NumberOfBlock()
NameOfAnticafe = anticafe.Name()
WebSite = anticafe.WebSite()
Remove = anticafe.Remove()

Price = []

print("+----------------------------------------------------+")
for i in range (0, len(Urls)):
    String = Scrap(Urls[i], WhatToSearch[i], NumberOf[i]) 
    price = String.split(" ")
    for n in range (0, len(Remove)):
        Price.append(price[0].replace(Remove[n], ""))
        print("|  Name: " + NameOfAnticafe[i])
        print("|  Price: "   + Price[i])
        print("|  WebSite: " + WebSite[i])
    print("+----------------------------------------------------+")