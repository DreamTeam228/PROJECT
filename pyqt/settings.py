#+==================================================
#|
#|====================НЕ ТРОГАТЬ====================
#|                                              DON'T TOUCH
#+==================================================
from PyQt5.QtWidgets import (QWidget, 
                                                               QPushButton, 
                                                               QLineEdit, 
                                                               QInputDialog, 
                                                               QApplication, 
                                                               QTextEdit, 
                                                               QLabel)
import sys
import os
from scrap import (Scrap, 
                                      convertUrl)

class SettingsScrapper(QWidget):
    soup = ""
    PhoneNumbers = ""
    Price = ""
    Place = ""
    Metro = ""
    Description = ""

    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.btn = QPushButton('Run', self)
        self.btn.move(20, 580)
        self.btn1 = QPushButton('Save', self)
        self.btn1.move(110, 580)

        self.Label = QLabel('Url:', self)
        self.Label.move(20, 12)
        self.Label1 = QLabel('NameBlockPhone:', self)
        self.Label1.move(20, 62)
        self.Label2 = QLabel('NumberBlocksPhone:', self)
        self.Label2.move(20, 112)
        self.Label3 = QLabel('NameBlockPrice:', self)
        self.Label3.move(20, 162)
        self.Label4 = QLabel('NumberBlockPrice:', self)
        self.Label4.move(20, 212)
        self.Label5 = QLabel('NameBlockPlace:', self)
        self.Label5.move(20, 262)
        self.Label6 = QLabel('NumberBlockPlace:', self)
        self.Label6.move(20, 312)
        self.Label7 = QLabel('NameBlockMetro:', self)
        self.Label7.move(20, 362)
        self.Label8 = QLabel('NumberBlockMetro:', self)
        self.Label8.move(20, 412)
        self.Label9 = QLabel('NameBlockDescription:', self)
        self.Label9.move(20, 462)
        self.Label10 = QLabel('NumberBlockDescription:', self)
        self.Label10.move(20, 512)

        self.text = QTextEdit(self)
        self.text.resize(400,400)
        self.text.move(185,20)

        self.btn.clicked.connect(self.RunScrap)
        self.btn1.clicked.connect(self.Save)
        
        self.url = QLineEdit(self)
        self.url.move(20, 32)
        self.nameblockphone = QLineEdit(self)
        self.nameblockphone.move(20, 82)
        self.numberblockphone = QLineEdit(self)
        self.numberblockphone.move(20, 132)

        self.nameblockprice = QLineEdit(self)
        self.nameblockprice.move(20,182)
        self.numberblockprice = QLineEdit(self)
        self.numberblockprice.move(20,232)

        self.nameblockplace = QLineEdit(self)
        self.nameblockplace.move(20,282)
        self.numberblockplace = QLineEdit(self)
        self.numberblockplace.move(20,332)

        self.nameblockmetro = QLineEdit(self)
        self.nameblockmetro.move(20,382)
        self.numberblockmetro = QLineEdit(self)
        self.numberblockmetro.move(20,432)

        self.nameblockdescription = QLineEdit(self)
        self.nameblockdescription.move(20,482)
        self.numberblockdescription = QLineEdit(self)
        self.numberblockdescription.move(20, 532)
        
        self.setGeometry(150, 150, 600, 620)
        self.setWindowTitle('Настройка скрапера')
        self.show()
        
        
    def RunScrap(self):
        self.text.setText('')
        self.Clear()
        
        Url = self.url.text()
        self.soup = convertUrl(Url)
        
        print(Url)
#====================================ДЛЯ НОМЕРОВ ТЕЛЕФОНОВ========================
        if self.nameblockphone.text() == '':
            print('Name and Number block phone was skiped')
        else:
            nameBlockPhone = (self.nameblockphone.text()).split(",")
            numberBlockPhone = (self.numberblockphone.text()).split(",")
            NumberBlockPhone = []
            for i in range(0, len(numberBlockPhone)):
                NumberBlockPhone.append(int(numberBlockPhone[i]))
            for i in range(0, len(nameBlockPhone)):
                for n in range(0, len(numberBlockPhone)):
                    a = ((Scrap(self.soup, nameBlockPhone[i], int(NumberBlockPhone[n]))).replace(" ", "")).replace("\xa0", "")
                    self.PhoneNumbers = self.PhoneNumbers + a + " "
            self.textEdit(self.PhoneNumbers)
#====================================ДЛЯ ЦЕННИКА===================================
        if self.nameblockprice.text() == '':
            print('Name and Number block price was skiped')
        else:
            nameBlockPrice = (self.nameblockprice.text()).split(",")
            numberBlockPrice = (self.numberblockprice.text()).split(",")
            NumberBlockPrice = []
            for i in range(0, len(numberBlockPrice)):
                NumberBlockPrice.append(int(numberBlockPrice[i]))
            for i in range(0, len(nameBlockPrice)):
                for n in range(0, len(numberBlockPrice)):
                    a = ((Scrap(self.soup, nameBlockPrice[i], int(NumberBlockPrice[n]))).replace(" ", "")).replace("\xa0", "").replace("рублей", "")
                    self.Price = self.Price + a + " "
            self.textEdit(self.Price)
#====================================ДЛЯ АДРЕСА=====================================
        if self.nameblockplace.text() == '':
            print('Name and Number block place was skiped')
        else:
            NameBlockPlace = []
            NameBlockPlace.append(self.nameblockplace.text())
            numberBlockPlace = (self.numberblockplace.text()).split(",")
            NumberBlockPlace = []
            for i in range(0,len(numberBlockPlace)):
                NumberBlockPlace.append(int(numberBlockPlace[i]))
            for i in range(0, len(NameBlockPlace)):
                for n in range(0, len(NumberBlockPlace)):
                    a =  Scrap(self.soup, NameBlockPlace[i], int(NumberBlockPlace[n]))
                    self.Place = self.Place + a + " "
            self.textEdit(self.Place)
#====================================ДЛЯ МЕТРО======================================
        if self.nameblockmetro.text() == '':
            print('Name and Number block metro was skiped')
        else:
            NameBlockMetro = (self.nameblockmetro.text()).split(',')
            numberBlockMetro = (self.numberblockmetro.text()).split(',')
            NumberBlockMetro = []
            for i in range(0, len(numberBlockMetro)):
                NumberBlockMetro.append(int(numberBlockMetro[i]))
            for i in range(0, len(NameBlockMetro)):
                for n in range(0, len(NumberBlockMetro)):
                    a = Scrap(self.soup, NameBlockMetro[i], NumberBlockMetro[n])
                    self.Metro = self.Metro + a + " "
            self.textEdit(self.Metro)
#====================================ОПИСAНИЕ=====================================
        if self.nameblockdescription.text() == '':
            print('Name and Number block description was skiped')
        else:
            NameBlockDescription = (self.nameblockdescription.text()).split(',')
            numberBlockDescription = (self.numberblockdescription.text()).split(',')
            NumberBlockDescription = []
            for i in range(0, len(numberBlockDescription)):
                NumberBlockDescription.append(int(numberBlockDescription[i]))
            for i in range(0, len(NameBlockDescription)):
                for n in range(0, len(NumberBlockDescription)):
                    a = Scrap(self.soup, NameBlockDescription[i], NumberBlockDescription[n])
                    self.Description = self.Description + a + " "
            print(self.Description)
            self.textEdit(self.Description)
#====================================СОХРАНЕНИЕ=====================================         
    def Save(self):
        path = os.getcwd() + '/'
        Path = 'sites'
        settings = 'settings'
        settings = path + settings + '/'
        path = path + Path + '/'
        current_place = path + self.url.text().replace('https:', '').replace('http:', '').replace('www.', '').replace('/', '')
        settings_place = settings + self.url.text().replace('https:', '').replace('http:', '').replace('www.', '').replace('/', '')
        current_place = current_place + '/'
        settings_place = settings_place + '/'

        try:
            os.makedirs(settings_place, 0o777)
        except FileExistsError:
            print('Path settings was already created')
        else:
            print('Path settings was created')
        
        try:  
            os.makedirs(current_place, 0o777)
        except FileExistsError:  
            print('Path current was already created')
        else:  
            print('Path current created')
        
        file_numberblockprice = 'numberblockprice'
        file_nameblockprice = 'nameblockprice'

        file_numberblockphone = 'numberblockphone'
        file_nameblockphone = 'nameblockphone'

        file_numberblockplace = 'numberblockplace'
        file_nameblockplace = 'nameblockplace'

        file_numberblockmetro = 'numberblockmetro'
        file_nameblockmetro = 'nameblockmetro'

        file_numberblockdescription = 'numberblockdescription'
        file_nameblockdescription = 'nameblockdescription'

        file_price = 'Price'
        file_phonenumbers = 'PhoneNumbers'
        file_place = 'Place'
        file_metro = 'Metro'
        file_description = 'Description'
        file_url = 'Url'

        if self.url.text() !='':
            self.File(settings_place, file_url, self.url.text())

        if self.nameblockprice.text() != '':
            if self.numberblockprice.text() != '':
                self.File(current_place, file_price, self.Price)
                self.File(settings_place, file_nameblockprice, self.nameblockprice.text())
                self.File(settings_place, file_numberblockprice, self.numberblockprice.text())
        
        if self.nameblockplace.text() != '':
            if self.numberblockplace.text() != '':
                self.File(current_place, file_place, self.Place)
                self.File(settings_place, file_nameblockplace, self.nameblockplace.text())
                self.File(settings_place, file_numberblockplace, self.numberblockplace.text())
        
        if self.nameblockmetro.text() != '':
            if self.numberblockmetro.text != '':
                self.File(current_place, file_metro, self.Metro)
                self.File(settings_place, file_nameblockmetro, self.nameblockmetro.text())
                self.File(settings_place, file_numberblockmetro, self.numberblockmetro.text())
        
        if self.nameblockphone.text() != '':
            if self.numberblockphone.text() != '':
                self.File(current_place, file_phonenumbers, self.PhoneNumbers)
                self.File(settings_place, file_nameblockphone, self.nameblockphone.text())
                self.File(settings_place, file_numberblockphone, self.numberblockphone.text())
        
        if self.nameblockdescription.text() != '':
            if self.numberblockdescription.text() != '':
                self.File(current_place, file_description, self.Description)
                self.File(settings_place, file_nameblockdescription, self.nameblockdescription.text())
                self.File(settings_place, file_numberblockdescription, self.numberblockdescription.text())
    
    def File(self, Path, Name, text):
        File = open(Path + Name + '.txt', 'w+')
        File.close()
        File = open(Path + Name + '.txt', 'w')
        File.write(str(text))
        File.close()

    def Clear(self):
        self.PhoneNumbers = ''
        self.Price = ''
        self.Place = ''
        self.Metro = ''
        self.Description = ''

    def textEdit(self, string):
        self.text.append(string)
        
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    SS = SettingsScrapper()
    sys.exit(app.exec_())