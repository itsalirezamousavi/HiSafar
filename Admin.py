from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import csv
import os


# ************************************************************************************************************************************
# *** ADD Travel *********************************************************************************************************************
# ************************************************************************************************************************************
class AdminAD(QMainWindow):
    def __init__(self):
        super().__init__()

        self.availableLocation = ['-- Any --','Ahvaz', 'Arak', 'Ardabil', 'Bandar abbas', 'Birjand', 'Bojnord', 'Bosherhr', 'Esfehan', 'Ghazvin', 
                                    'Ghom', 'Gorgan', 'Hamedan', 'Ilam', 'Karaj', 'Kerman', 'Kermanshah', 'Khoram abad', 'Mashhad', 'Oromie', 'Rasht', 
                                    'Saary', 'Sanandaj', 'Semnan', 'Shahre kord', 'Shiraz', 'Tabriz', 'Tehran', 'Yasooj', 'Yazd', 'Zahedan', 'Zanjan']

        self.setWindowTitle('Admin')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(800,650)
        self.adminUiADComponents()
        self.show()


    def removeTravelUI(self):
        self.w = AdminRD()
        self.w.show()
        self.hide()
    def editTravelUI(self):
        self.w = AdminED()
        self.w.show()
        self.hide()
    def showTravelUI(self):
        self.w = AdminST()
        self.w.show()
        self.hide()


    def adminUiADComponents(self):
        self.addTravelBT = QPushButton('Add Travel',self)
        self.addTravelBT.setGeometry(50, 25, 175, 25)
        self.removeTravelBT = QPushButton('remove Travel',self)
        self.removeTravelBT.setGeometry(225, 25, 175, 25)
        self.removeTravelBT.clicked.connect(self.removeTravelUI)
        self.editTravellBT = QPushButton('Edit Travel',self)
        self.editTravellBT.setGeometry(400, 25, 175, 25)
        self.editTravellBT.clicked.connect(self.editTravelUI)
        self.showTravelBT = QPushButton('Show Travels',self)
        self.showTravelBT.setGeometry(575, 25, 175, 25)
        self.showTravelBT.clicked.connect(self.showTravelUI)

        self.fromWhereLabel = QLabel('From Where :', self)
        self.fromWhereLabel.setGeometry(50, 65, 170, 20)
        self.fromWhereCB = QComboBox(self)
        self.fromWhereCB.setGeometry(50, 90, 170, 25)
        self.fromWhereCB.addItems(self.availableLocation)

        self.toWhereLabel = QLabel('To Where :', self)
        self.toWhereLabel.setGeometry(230, 65, 170, 20)
        self.toWhereCB = QComboBox(self)
        self.toWhereCB.setGeometry(230, 90, 170, 25)
        self.toWhereCB.addItems(self.availableLocation)

        self.whenLabel = QLabel('When :', self)
        self.whenLabel.setGeometry(405, 65, 170, 20)
        self.when = QDateEdit(self,calendarPopup=True)
        self.when.setDateTime(QDateTime.currentDateTime())
        self.when.setGeometry(405, 90, 170, 25)

        self.timeLabel = QLabel('Time: (exp: 12:30)',self)
        self.timeLabel.setGeometry(590, 65, 170, 20)
        self.time = QLineEdit(self)
        self.time.setGeometry(580, 90, 170, 25)

        self.capacityLabel = QLabel('Capacity:',self)
        self.capacityLabel.setGeometry(50, 125, 170, 20)
        self.capacity = QLineEdit(self)
        self.capacity.setGeometry(50, 150, 170, 25)

        self.travelNumLabel = QLabel('Travel Number:',self)
        self.travelNumLabel.setGeometry(230, 125, 170, 20)
        self.travelNum = QLineEdit(self)
        self.travelNum.setGeometry(230, 150, 170, 25)

        self.priceLabel = QLabel('Price:',self)
        self.priceLabel.setGeometry(405, 125, 170, 20)
        self.price = QLineEdit(self)
        self.price.setGeometry(405, 150, 170, 25)

        self.submitBT = QPushButton('Add',self)
        self.submitBT.setGeometry(580, 150, 170, 25)
        self.submitBT.clicked.connect(self.addTravelFunc)

    def addTravelFunc(self):
        self.travelNumList = []
        with open('trvl.db', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row == []:
                    continue
                self.travelNumList.append(row[2])
        if self.travelNum.text() in self.travelNumList:
            msg = QMessageBox.warning(self, 'Error 101' , 'Selected Travel Number alredy Exist\nPlease enter another one')
        elif self.fromWhereCB.currentText() == '-- Any --' or self.toWhereCB.currentText() == '-- Any --':
            msg = QMessageBox.warning(self, 'Error 102' , 'Selected Travel Number most have Source and Destination ')
        else:
            with open('trvl.db','a') as tdb:
                csvwriter = csv.writer(tdb)
                row = [
                    self.fromWhereCB.currentText(),
                    self.toWhereCB.currentText(),
                    self.travelNum.text(),
                    self.capacity.text(),
                    str(self.when.date().toPyDate()),
                    self.time.text(),
                    self.price.text(),
                    []
                    ]
                csvwriter.writerow(row)
            msg = QMessageBox.information(self, 'Succes' , 'Selected Travel was succesfully Added')



# ************************************************************************************************************************************
# *** REMOVE Travel ******************************************************************************************************************
# ************************************************************************************************************************************
class AdminRD(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Admin')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(800,650)
        self.adminUiRDComponents()
        self.show()

    def addTravelUI(self):
        self.w = AdminAD()
        self.w.show()
        self.hide()
    def editTravelUI(self):
        self.w = AdminED()
        self.w.show()
        self.hide()
    def showTravelUI(self):
        self.w = AdminST()
        self.w.show()
        self.hide()


    def adminUiRDComponents(self):
        self.addTravelBT = QPushButton('Add Travel',self)
        self.addTravelBT.setGeometry(50, 25, 175, 25)
        self.addTravelBT.clicked.connect(self.addTravelUI)
        self.removeTravelBT = QPushButton('remove Travel',self)
        self.removeTravelBT.setGeometry(225, 25, 175, 25)
        self.editTravellBT = QPushButton('Edit Travel',self)
        self.editTravellBT.setGeometry(400, 25, 175, 25)
        self.editTravellBT.clicked.connect(self.editTravelUI)
        self.showTravelBT = QPushButton('Show Travels',self)
        self.showTravelBT.setGeometry(575, 25, 175, 25)
        self.showTravelBT.clicked.connect(self.showTravelUI)

        self.travelNumLabel = QLabel('Enter Travel Number:',self)
        self.travelNumLabel.setGeometry(50, 65, 345, 20)
        self.travelNum = QLineEdit(self)
        self.travelNum.setGeometry(50, 90, 345, 25)

        self.searchBT = QPushButton('Search',self)
        self.searchBT.setGeometry(405, 90, 345, 25)
        self.searchBT.clicked.connect(self.searchBTFunc)

        self.travelDetail = QLabel('Selected Travel Info :',self)
        self.travelDetail.setGeometry(50, 125, 700, 25)

        self.removeBT = QPushButton('Remove',self)
        self.removeBT.setGeometry(405, 160, 345, 25)
        self.removeBT.clicked.connect(self.removeTravelFunc)

    def searchBTFunc(self):
        self.found = False
        with open('trvl.db','r') as tdb:
            csvreader = csv.reader(tdb)
            for row in csvreader:
                if row == []:
                    continue
                elif row[2] == self.travelNum.text():
                    self.travelDetail.setText(str(row))
                    self.found = True
            if self.found == False:
                msg = QMessageBox.warning(
                    self, 'Not Found' , 'Selected Travel does not Exist\nIts been Deleted or it didnt Exist in the first place!')

    def removeTravelFunc(self):
        self.travelDetail.setText('')
        self.lines = list()
        with open('trvl.db', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                self.lines.append(row)
                if row == []:
                    continue
                if row[2] == self.travelNum.text():
                    self.passenger = row[7]
                    self.lines.remove(row)
        with open('trvl.db', 'w',newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(self.lines)
        msg = QMessageBox.information(self, 'Succes' , 'Selected Travel was succesfully Deleted')



# ************************************************************************************************************************************
# *** EDIT Travel ********************************************************************************************************************
# ************************************************************************************************************************************
class AdminED(QMainWindow):
    def __init__(self):
        super().__init__()

        self.availableLocation = ['-- Any --','Ahvaz', 'Arak', 'Ardabil', 'Bandar abbas', 'Birjand', 'Bojnord', 'Bosherhr', 'Esfehan', 'Ghazvin', 
                                    'Ghom', 'Gorgan', 'Hamedan', 'Ilam', 'Karaj', 'Kerman', 'Kermanshah', 'Khoram abad', 'Mashhad', 'Oromie', 'Rasht', 
                                    'Saary', 'Sanandaj', 'Semnan', 'Shahre kord', 'Shiraz', 'Tabriz', 'Tehran', 'Yasooj', 'Yazd', 'Zahedan', 'Zanjan']

        self.setWindowTitle('Admin')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(800,650)
        self.adminUiEDComponents()
        self.show()

    def addTravelUI(self):
        self.w = AdminAD()
        self.w.show()
        self.hide()
    def removeTravelUI(self):
        self.w = AdminRD()
        self.w.show()
        self.hide()
    def showTravelUI(self):
        self.w = AdminST()
        self.w.show()
        self.hide()


    def adminUiEDComponents(self):
        self.addTravelBT = QPushButton('Add Travel',self)
        self.addTravelBT.setGeometry(50, 25, 175, 25)
        self.addTravelBT.clicked.connect(self.addTravelUI)
        self.removeTravelBT = QPushButton('remove Travel',self)
        self.removeTravelBT.setGeometry(225, 25, 175, 25)
        self.removeTravelBT.clicked.connect(self.removeTravelUI)
        self.editTravellBT = QPushButton('Edit Travel',self)
        self.editTravellBT.setGeometry(400, 25, 175, 25)
        self.showTravelBT = QPushButton('Show Travels',self)
        self.showTravelBT.setGeometry(575, 25, 175, 25)
        self.showTravelBT.clicked.connect(self.showTravelUI)

        self.travelNumLabel = QLabel('Enter Travel Number:',self)
        self.travelNumLabel.setGeometry(50, 65, 345, 20)
        self.travelNum = QLineEdit(self)
        self.travelNum.setGeometry(50, 90, 345, 25)

        self.searchBT = QPushButton('Search',self)
        self.searchBT.setGeometry(405, 90, 345, 25)
        self.searchBT.clicked.connect(self.searchBTFunc)

        self.travelDetail = QLabel('Selected Travel Info :',self)
        self.travelDetail.setGeometry(50, 125, 700, 25)

        self.fromWhereLabel = QLabel('From Where :', self)
        self.fromWhereLabel.setGeometry(50, 160, 170, 20)
        self.fromWhereCB = QComboBox(self)
        self.fromWhereCB.setGeometry(50, 185, 170, 25)
        self.fromWhereCB.addItems(self.availableLocation)
        
        self.toWhereLabel = QLabel('To Where :', self)
        self.toWhereLabel.setGeometry(230, 160, 170, 20)
        self.toWhereCB = QComboBox(self)
        self.toWhereCB.setGeometry(230, 185, 170, 25)
        self.toWhereCB.addItems(self.availableLocation)

        self.whenLabel = QLabel('When :', self)
        self.whenLabel.setGeometry(405, 160, 170, 20)
        self.when = QDateEdit(self,calendarPopup=True)
        self.when.setDateTime(QDateTime.currentDateTime())
        self.when.setGeometry(405, 185, 170, 25)

        self.timeLabel = QLabel('Time: (exp: 12:30)',self)
        self.timeLabel.setGeometry(590, 160, 170, 20)
        self.time = QLineEdit(self)
        self.time.setGeometry(580, 185, 170, 25)

        self.capacityLabel = QLabel('Capacity:',self)
        self.capacityLabel.setGeometry(50, 220, 170, 20)
        self.capacity = QLineEdit(self)
        self.capacity.setGeometry(50, 245, 170, 25)

        self.priceLabel = QLabel('Price:',self)
        self.priceLabel.setGeometry(230, 220, 170, 20)
        self.price = QLineEdit(self)
        self.price.setGeometry(230, 245, 170, 25)

        self.submitBT = QPushButton('Edit',self)
        self.submitBT.setGeometry(405, 245, 345, 25)
        self.submitBT.clicked.connect(self.editTravelFunc)

    def searchBTFunc(self):
        with open('trvl.db','r') as tdb:
            csvreader = csv.reader(tdb)
            for row in csvreader:
                if row == []:
                    continue
                elif row[2] == self.travelNum.text():
                    self.travelDetail.setText(str(row))

    def editTravelFunc(self):
        self.passenger = list()
        self.lines = list()
        with open('trvl.db', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                self.lines.append(row)
                if row == []:
                    continue
                if row[2] == self.travelNum.text():
                    self.passenger = row[7]
                    self.lines.remove(row)
        with open('trvl.db', 'w',newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(self.lines)
            
        with open('trvl.db','a') as tdb:
            csvwriter = csv.writer(tdb)
            row = [
                self.fromWhereCB.currentText(),
                self.toWhereCB.currentText(),
                self.travelNum.text(),
                self.capacity.text(),
                str(self.when.date().toPyDate()),
                self.time.text(),
                self.price.text(),
                self.passenger
                ]
            csvwriter.writerow(row)
        msg = QMessageBox.information(self, 'Succes' , 'Selected Travel was succesfully Edited')



# ************************************************************************************************************************************
# *** SHOW Travel ********************************************************************************************************************
# ************************************************************************************************************************************
class AdminST(QMainWindow):
    def __init__(self):
        super().__init__()

        self.availableLocation = ['-- Any --','Ahvaz', 'Arak', 'Ardabil', 'Bandar abbas', 'Birjand', 'Bojnord', 'Bosherhr', 'Esfehan', 'Ghazvin', 
                                    'Ghom', 'Gorgan', 'Hamedan', 'Ilam', 'Karaj', 'Kerman', 'Kermanshah', 'Khoram abad', 'Mashhad', 'Oromie', 'Rasht', 
                                    'Saary', 'Sanandaj', 'Semnan', 'Shahre kord', 'Shiraz', 'Tabriz', 'Tehran', 'Yasooj', 'Yazd', 'Zahedan', 'Zanjan']

        self.setWindowTitle('Admin')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(800,650)
        self.adminUiSTComponents()
        self.show()

    def addTravelUI(self):
        self.w = AdminAD()
        self.w.show()
        self.hide()
    def removeTravelUI(self):
        self.w = AdminRD()
        self.w.show()
        self.hide()
    def editTravelUI(self):
        self.w = AdminED()
        self.w.show()
        self.hide()

    def adminUiSTComponents(self): 
        self.addTravelBT = QPushButton('Add Travel',self)
        self.addTravelBT.setGeometry(50, 25, 175, 25)
        self.addTravelBT.clicked.connect(self.addTravelUI)
        self.removeTravelBT = QPushButton('remove Travel',self)
        self.removeTravelBT.setGeometry(225, 25, 175, 25)
        self.removeTravelBT.clicked.connect(self.removeTravelUI)
        self.editTravellBT = QPushButton('Edit Travel',self)
        self.editTravellBT.setGeometry(400, 25, 175, 25)
        self.editTravellBT.clicked.connect(self.editTravelUI)
        self.showTravelBT = QPushButton('Show Travels',self)
        self.showTravelBT.setGeometry(575, 25, 175, 25)

        self.fromWhereLabel = QLabel('From Where :', self)
        self.fromWhereLabel.setGeometry(50, 65, 170, 20)
        self.fromWhereCB = QComboBox(self)
        self.fromWhereCB.setGeometry(50, 90, 230, 25)
        self.fromWhereCB.addItems(self.availableLocation)
        
        self.toWhereLabel = QLabel('To Where :', self)
        self.toWhereLabel.setGeometry(290, 65, 170, 20)
        self.toWhereCB = QComboBox(self)
        self.toWhereCB.setGeometry(290, 90, 230, 25)
        self.toWhereCB.addItems(self.availableLocation)

        self.searchBT = QPushButton('Search',self)
        self.searchBT.setGeometry(530, 90, 223, 25)
        self.searchBT.clicked.connect(self.showTravelFunc)

        self.travelTB = QTextBrowser(self)
        self.travelTB.setGeometry(50, 130, 700, 490)

    def showTravelFunc(self):
        self.travelTB.clear()
        with open('trvl.db','r') as tdb:
            csvreader = csv.reader(tdb)
            for row in csvreader:
                if row == []:
                    continue

                elif self.fromWhereCB.currentText() == '-- Any --' and self.toWhereCB.currentText() == '-- Any --':
                    self.travelTB.append(str(row))

                elif self.fromWhereCB.currentText() == '-- Any --' and row[1].lower() == self.toWhereCB.currentText().lower():
                    self.travelTB.append(str(row))

                elif self.fromWhereCB.currentText().lower() == row[0].lower() and self.toWhereCB.currentText() == '-- Any --':
                    self.travelTB.append(str(row))

                elif self.fromWhereCB.currentText().lower() == row[0].lower() and row[1].lower() == self.toWhereCB.currentText().lower():
                    self.travelTB.append(str(row))
                



# ************************************************************************************************************************************
# *** ADMIN **************************************************************************************************************************
# ************************************************************************************************************************************
class Admin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Admin')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(800,650)
        self.adminUiComponents()
        self.show()

    def open(self):
        self.w = AdminAD()
        self.w.show()
        self.hide()

    def login(self):
        with open('admin.db','r') as adb:
            csvreader = csv.reader(adb)
            for row in csvreader:
                if row == []:
                    continue
                if row[0] == self.user.text() and row[1] == self.password.text():
                    self.open()

    def adminUiComponents(self):
        self.userLabel = QLabel('Username:',self)
        self.userLabel.setGeometry(50, 25, 175, 25)
        self.user = QLineEdit(self)
        self.user.setGeometry(50, 50, 175, 30)
        self.passwordLabel = QLabel('Password:',self)
        self.passwordLabel.setGeometry(50, 85, 175, 25)
        self.password = QLineEdit(self)
        self.password.setGeometry(50, 110, 175, 30)
        self.addTravelBT = QPushButton('Log in',self)
        self.addTravelBT.setGeometry(50, 150, 175, 25)
        self.addTravelBT.clicked.connect(self.login)



App = QApplication(sys.argv)
win = Admin()
win.show()
App.exec()