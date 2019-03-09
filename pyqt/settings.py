#+==================================================
#|ЭТО ПРОГРАММА ДЛЯ НАСТРОЙКИ ФАЙЛОВ, ОНА ДЛЯ СИСаДМИНА(ОНА НЕ ВЫПОЛНЕНА В ПОЛНОЙ МЕРЕ)
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
from scrap import (Scrap, 
                                      convertUrl)

class SettingsScrapper(QWidget):
    soup = ""
    PhoneNumbers = "PhoneNumbers: "
   # PhoneNumbers = ""
    Price = "Price: "
    #Price = ""
    Place = "Adress: "
    #Place = ""
    Metro = "Metro: "
    #Metro = ""

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
        
        self.setGeometry(150, 150, 600, 620)
        self.setWindowTitle('Настройка скрапера')
        self.show()
        
        
    def RunScrap(self):
        
        Url = self.url.text()
        
        print(Url)
        nameBlockPhone = (self.nameblockphone.text()).split(",")
        print(nameBlockPhone)
        numberBlockPhone = (self.numberblockphone.text()).split(",")
        NumberBlockPhone = []
        for i in range(0, len(numberBlockPhone)):
            NumberBlockPhone.append(int(numberBlockPhone[i]))

        self.soup = convertUrl(Url)
#==============================ДЛЯ НОМЕРОВ ТЕЛЕФОНОВ=============================
        for i in range(0, len(nameBlockPhone)):
            for n in range(0, len(numberBlockPhone)):
                a = ((Scrap(self.soup, nameBlockPhone[i], int(NumberBlockPhone[n]))).replace(" ", "")).replace("\xa0", "")
                self.PhoneNumbers = self.PhoneNumbers + a + " "
        self.textEdit(self.PhoneNumbers)
#=======================РАБОТА НАД НОМЕРАМИ ТУТ ЗАКАНЧИВАЕТСЯ=====================
        nameBlockPrice = (self.nameblockprice.text()).split(",")
        numberBlockPrice = (self.numberblockprice.text()).split(",")
        NumberBlockPrice = []
        for i in range(0, len(numberBlockPrice)):
            NumberBlockPrice.append(int(numberBlockPrice[i]))
#====================================ДЛЯ ЦЕННИКА===================================
        for i in range(0, len(nameBlockPrice)):
            for n in range(0, len(numberBlockPrice)):
                a = ((Scrap(self.soup, nameBlockPrice[i], int(NumberBlockPrice[n]))).replace(" ", "")).replace("\xa0", "").replace("рублей", "")
                self.Price = self.Price + a + " "
        self.textEdit(self.Price)
#=======================РАБОТА НАД ЦЕННИКОМ ТУТ ЗАКАНЧИВАЕТСЯ=====================
        NameBlockPlace = []
        NameBlockPlace.append(self.nameblockplace.text())
        numberBlockPlace = (self.numberblockplace.text()).split(",")
        NumberBlockPlace = []
        for i in range(0,len(numberBlockPlace)):
            NumberBlockPlace.append(int(numberBlockPlace[i]))
#====================================ДЛЯ АДРЕСА===================================
        for i in range(0, len(NameBlockPlace)):
            for n in range(0, len(NumberBlockPlace)):
                a =  Scrap(self.soup, NameBlockPlace[i], int(NumberBlockPlace[n]))
                self.Place = self.Place + a + " "
        self.textEdit(self.Place)
#============================РАБОТА НАД АДРЕСОМ ЗАКОНЧЕНА========================
        NameBlockMetro = (self.nameblockmetro.text()).split(',')
        numberBlockMetro = (self.numberblockmetro.text()).split(',')
        NumberBlockMetro = []
        for i in range(0, len(numberBlockMetro)):
            NumberBlockMetro.append(int(numberBlockMetro[i]))
#====================================ДЛЯ МЕТРО====================================
        for i in range(0, len(NameBlockMetro)):
            for n in range(0, len(NumberBlockMetro)):
                a = Scrap(self.soup, NameBlockMetro[i], NumberBlockMetro[n])
                self.Metro = self.Metro + a + " "
        self.textEdit(self.Metro)
#=============================РАБОТА НАД МЕТРО ЗАКОНЧЕНА=========================
        self.Clear()

    def Save(self):
        NewFile = open()


    def Clear(self):
        self.PhoneNumbers = ''
        self.Price = ''
        self.Place = ''
        self.Metro = ''
        nameBlockPhone = []
        numberBlockPhone = []
        nameBlockPrice = []
        numberBlockPrice = []
        NameBlockPlace = []
        numberBlockPlace = []
        NameBlockMetro = []
        NumberBlockMetro = []

    def textEdit(self, string):
        self.text.append(string)
        
        
        #172
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    SS = SettingsScrapper()
    sys.exit(app.exec_())