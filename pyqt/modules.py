from scrap import Scrap

class anticafe():
    urls = []
    name = []
    website = []
    search = []
    numberofblock = []
    remove = []

    def Url(self):
        self.urls = ['http://12yards.ru/%D0%BF%D1%80%D0%B0%D0%B9%D1%81/', 
                              'https://www.luckylori.ru/']
        return self.urls

    def Name(self):
        self.name = ['12 Ярдов', 
                                 'Lucky Lori']
        return self.name

    def WebSite(self):
        self.website = ['http://12yards.ru/', 
                                      'https://www.luckylori.ru/']
        return self.website

    def Search(self):
        self.search = ['span',
                                    'span']
        return self.search

    def NumberOfBlockPrice(self):
        self.numberofblock = [0, 
                                                     148]
        return self.numberofblock

    def Remove(self):
        self.remove = ['\xa0']
        return self.remove



        


class zoo():
    urls = []
    name = []
    website = []
    search = []
    numberofblock = []
    remove = []

    def Url(self):
        self.urls = ['https://www.moscowzoo.ru/for-visitors/tickets/']
        return self.urls
    
    def Name(self):
        self.name = ['Московский Зоопарк']
        return self.name

    def WebSite(self):
        self.website = ['https://www.moscowzoo.ru/']
        return self.website

    def Search(self):
        self.search = ['h3']
        return self.search

    def NumberOfBlock(self):
        self.numberofblock = [5]
        return self.numberofblock

    def Remove(self):
        self.remove = []
        return self.remove