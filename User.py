from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import csv


# ************************************************************************************************************************************
# *** USERNOLogedIn ******************************************************************************************************************
# ************************************************************************************************************************************
class UserNOLogedIn(QMainWindow):
    def __init__(self):
        super().__init__()

        self.sortByList = ['Price','Date']
        self.availableLocation = ['-- Any --','Ahvaz', 'Arak', 'Ardabil', 'Bandar abbas', 'Birjand', 'Bojnord', 'Bosherhr', 'Esfehan', 'Ghazvin', 
                                    'Ghom', 'Gorgan', 'Hamedan', 'Ilam', 'Karaj', 'Kerman', 'Kermanshah', 'Khoram abad', 'Mashhad', 'Oromie', 'Rasht', 
                                    'Saary', 'Sanandaj', 'Semnan', 'Shahre kord', 'Shiraz', 'Tabriz', 'Tehran', 'Yasooj', 'Yazd', 'Zahedan', 'Zanjan']

        self.setWindowTitle('HiSafar')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(800, 650)
        self.UiComponents()
        self.lastMinute()
        self.show()

    def submitFunc(self):
        self.travel.clear()

        with open('trvl.db','r') as trvldb:
            
            fromWhere = self.fromWhereCB.currentText()
            toWhere = self.toWhereCB.currentText()
            availableTravel = []
            csvreader = csv.reader(trvldb)

            if fromWhere == '-- Any --' and toWhere == '-- Any --':
                msg = QMessageBox.warning(self, 'Error' , 'We cant show you all of our Database\nPlease select at least one location')

            for row in csvreader:
                if row == []:
                    continue
                if fromWhere == '-- Any --' and row[1].lower() == toWhere.lower():
                    availableTravel.append(row)
                elif toWhere == '-- Any --' and row[0].lower() == fromWhere.lower():
                    availableTravel.append(row)
                elif row[0].lower() == fromWhere.lower() and row[1].lower() == toWhere.lower():
                    availableTravel.append(row)

        def sortByTime(row):
            time = row[5]
            if len(row[5]) == 4:
                time = '0' + row[5]
            sort = row[4] + time
            return sort
        def sortByPrice(row):
            return int(row[6])

        if self.sortByCB.currentText() == 'Price':
            availableTravel = sorted(availableTravel,key=sortByPrice)
        else:
            availableTravel = sorted(availableTravel,key=sortByTime)

        for item in availableTravel:
            string = f'{item[2]} : {item[0]}-{item[1]} : {item[4]},{item[5]} , Price = {item[6]}'
            self.travel.append(string)



    def login(self):
        updb = open('up.db','r')
        csvreader = csv.reader(updb)
        for row in csvreader:
            if row != '\n' and row != '' and row != ' ':
                if row[0] == self.id.text() and row[1] == self.password.text():
                    msg = QMessageBox.warning(self, 'Succes', 'You seccesfully loged in')
                    self.w = UserLogedIn(self.id.text())
                    self.w.show()
                    self.hide()
        updb.close()


    def openSignUpWindow(self):
        self.w = Signup()
        self.w.show()

    def lastMinute(self):
        with open('trvl.db','r') as tdb:
            csvreader = csv.reader(tdb)
            for row in csvreader:
                if row == []:
                    continue
                string = ''
                if row[4] == str(self.when.dateTime().toPyDateTime())[:10]:
                    string = f"<b>{row[0].capitalize()}-{row[1].capitalize()}</b>\n\nTravel Number : {row[2]} \n\nTime : {row[5]}\n************"
                    self.lastMinuteTB.append(string)
    
    def buy(self):
        msg = QMessageBox.warning(self, 'Error', 'You have to log in first')

    def UiComponents(self):
        self.idLabel = QLabel('ID :', self)
        self.idLabel.setGeometry(30, 60, 150, 20)
        self.id = QLineEdit(self)
        self.id.setGeometry(30, 90, 150, 25)
        self.passwordLabel = QLabel('Password :', self)
        self.passwordLabel.setGeometry(30, 120, 150, 20)
        self.password = QLineEdit(self)
        self.password.setGeometry(30, 150, 150, 25)
        self.loginBT = QPushButton('Log in', self)
        self.loginBT.setGeometry(30, 180, 150, 25)
        self.loginBT.clicked.connect(self.login)

        self.signupBT = QPushButton('Sign up', self)
        self.signupBT.setGeometry(30, 210, 150, 25)
        self.signupBT.clicked.connect(self.openSignUpWindow)

        self.lastMinuteLabel = QLabel('Last Minute Travel :',self)
        self.lastMinuteLabel.setGeometry(30, 250, 150, 20)
        self.lastMinuteTB = QTextBrowser(self)
        self.lastMinuteTB.setGeometry(30, 270, 150, 250)
        self.fromWhereLabel = QLabel('From Where :', self)
        self.fromWhereLabel.setGeometry(220, 60, 120, 20)
        self.fromWhereCB = QComboBox(self)
        self.fromWhereCB.setGeometry(220, 90, 120, 25)
        self.fromWhereCB.addItems(self.availableLocation)
        self.fromWhere = self.fromWhereCB.currentText()
        self.toWhereLabel = QLabel('To Where :', self)
        self.toWhereLabel.setGeometry(360, 60, 120, 20)
        self.toWhereCB = QComboBox(self)
        self.toWhereCB.setGeometry(360, 90, 120, 25)
        self.toWhereCB.addItems(self.availableLocation)
        # self.whenLabel = QLabel('When :', self)
        # self.whenLabel.setGeometry(500, 60, 120, 20)
        self.when = QDateEdit(self,calendarPopup=True)
        self.when.setDateTime(QDateTime.currentDateTime())
        self.when.hide()
        # self.when.setGeometry(500, 90, 120, 25)
        # self.whenCB = QCheckBox("I don't care When", self)
        # self.whenCB.setGeometry(640, 90, 140, 25)
        # self.whenCB.setChecked(True)
        self.sortByLabel = QLabel('Sort By :',self)
        self.sortByLabel.setGeometry(220, 120, 120, 20)
        self.sortByCB = QComboBox(self)
        self.sortByCB.setGeometry(220, 150, 120, 25)
        self.sortByCB.addItems(self.sortByList)
        self.submitBT = QPushButton('Submit', self)
        self.submitBT.setGeometry(360, 130, 410, 45)
        self.submitBT.clicked.connect(self.submitFunc)

        self.travelLabel = QLabel('Travel :', self)
        self.travelLabel.setGeometry(220, 190, 120, 20)
        self.travel = QTextBrowser(self)
        self.travel.setGeometry(220, 210, 550, 310)
        self.travelNumLabel = QLabel('Enter selected Travel Number:',self)
        self.travelNumLabel.setGeometry(220, 530, 180, 25)
        self.travelNum = QLineEdit(self)
        self.travelNum.setGeometry(410, 530, 170, 25)
        self.buyBT =QPushButton('Buy',self)
        self.buyBT.setGeometry(600, 530, 170, 26)
        self.buyBT.clicked.connect(self.buy)

# ************************************************************************************************************************************
# *** USERLogedIn ********************************************************************************************************************
# ************************************************************************************************************************************
class UserLogedIn(QMainWindow):
    def __init__(self,id):
        super().__init__()

        self.id = id
        self.logedIn = False
        self.user = ''

        self.sortByList = ['Price','Date']
        self.availableLocation = ['-- Any --','Ahvaz', 'Arak', 'Ardabil', 'Bandar abbas', 'Birjand', 'Bojnord', 'Bosherhr', 'Esfehan', 'Ghazvin', 
                                    'Ghom', 'Gorgan', 'Hamedan', 'Ilam', 'Karaj', 'Kerman', 'Kermanshah', 'Khoram abad', 'Mashhad', 'Oromie', 'Rasht', 
                                    'Saary', 'Sanandaj', 'Semnan', 'Shahre kord', 'Shiraz', 'Tabriz', 'Tehran', 'Yasooj', 'Yazd', 'Zahedan', 'Zanjan']

        self.setWindowTitle('HiSafar')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(800, 650)
        self.UiComponents()
        self.lastMinute()
        self.show()

    def submitFunc(self):
        self.travel.clear()

        with open('trvl.db','r') as trvldb:
            
            fromWhere = self.fromWhereCB.currentText()
            toWhere = self.toWhereCB.currentText()
            availableTravel = []
            csvreader = csv.reader(trvldb)

            if fromWhere == '-- Any --' and toWhere == '-- Any --':
                msg = QMessageBox.warning(self, 'Error' , 'We cant show you all of our Database\nPlease select at least one location')

            for row in csvreader:
                if row == []:
                    continue
                if fromWhere == '-- Any --' and row[1].lower() == toWhere.lower():
                    availableTravel.append(row)
                elif toWhere == '-- Any --' and row[0].lower() == fromWhere.lower():
                    availableTravel.append(row)
                elif row[0].lower() == fromWhere.lower() and row[1].lower() == toWhere.lower():
                    availableTravel.append(row)

        def sortByTime(row):
            time = row[5]
            if len(row[5]) == 4:
                time = '0' + row[5]
            sort = row[4] + time
            return sort
        def sortByPrice(row):
            return int(row[6])

        if self.sortByCB.currentText() == 'Price':
            availableTravel = sorted(availableTravel,key=sortByPrice)
        else:
            availableTravel = sorted(availableTravel,key=sortByTime)

        for item in availableTravel:
            string = f'{item[2]} : {item[0]}-{item[1]} : {item[4]},{item[5]} , Price = {item[6]}'
            self.travel.append(string)


    def lastMinute(self):
        with open('trvl.db','r') as tdb:
            csvreader = csv.reader(tdb)
            for row in csvreader:
                if row == []:
                    continue
                string = ''
                if row[4] == str(self.when.dateTime().toPyDateTime())[:10]:
                    string = f"<b>{row[0].capitalize()}-{row[1].capitalize()}</b>\n\nTravel Number : {row[2]} \n\nTime : {row[5]}\n************"
                    self.lastMinuteTB.append(string)
    
    def buy(self):
        with open('trvl.db','r') as tdb:
            csvreader = csv.reader(tdb)
            for row in csvreader:
                try:
                    if row == [] or row == '':
                        continue
                    if row[2] == self.travelNum.text():
                        x = Buy(self.travelNum.text(), self.id)
                except:
                    pass

    def cancelTicket(self):
        self.lines = list()
        self.travel = []

        with open('trvl.db', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                self.lines.append(row)
                if row == []:
                    continue
                if self.id in row[7].split('-'):
                    passenger = []
                    self.travel = row
                    string = ''
                    passenger = row[7].split('-')
                    passenger.remove(self.id)
                    if passenger != '[]':
                        flag = True
                        for item in passenger:
                            if flag:
                                string = item
                                flag = False
                            else:
                                string = f'{string}-{item}'
                    else:
                        string = '[]'
                    self.travel[7]=string
                    self.lines.remove(row)

        with open('trvl.db', 'w',newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(self.lines)
            writer.writerow(self.travel)
            msg = QMessageBox.information(self, 'Succes', 'Your canceltion was Succesfull')
    
    def logout(self):
        self.w = UserNOLogedIn()
        self.w.show()
        self.hide()       
            

    def UiComponents(self):

        self.lastMinuteLabel = QLabel('Last Minute Travel :',self)
        self.lastMinuteLabel.setGeometry(30, 250, 150, 20)
        self.lastMinuteTB = QTextBrowser(self)
        self.lastMinuteTB.setGeometry(30, 270, 150, 250)
        self.fromWhereLabel = QLabel('From Where :', self)
        self.fromWhereLabel.setGeometry(220, 60, 120, 20)
        self.fromWhereCB = QComboBox(self)
        self.fromWhereCB.setGeometry(220, 90, 120, 25)
        self.fromWhereCB.addItems(self.availableLocation)
        self.fromWhere = self.fromWhereCB.currentText()
        self.toWhereLabel = QLabel('To Where :', self)
        self.toWhereLabel.setGeometry(360, 60, 120, 20)
        self.toWhereCB = QComboBox(self)
        self.toWhereCB.setGeometry(360, 90, 120, 25)
        self.toWhereCB.addItems(self.availableLocation)
        # self.whenLabel = QLabel('When :', self)
        # self.whenLabel.setGeometry(500, 60, 120, 20)
        self.when = QDateEdit(self,calendarPopup=True)
        self.when.setDateTime(QDateTime.currentDateTime())
        self.when.hide()
        # self.when.setGeometry(500, 90, 120, 25)
        # self.whenCB = QCheckBox("I don't care When", self)
        # self.whenCB.setGeometry(640, 90, 140, 25)
        # self.whenCB.setChecked(True)
        self.sortByLabel = QLabel('Sort By :',self)
        self.sortByLabel.setGeometry(220, 120, 120, 20)
        self.sortByCB = QComboBox(self)
        self.sortByCB.setGeometry(220, 150, 120, 25)
        self.sortByCB.addItems(self.sortByList)
        self.submitBT = QPushButton('Submit', self)
        self.submitBT.setGeometry(360, 130, 410, 45)
        self.submitBT.clicked.connect(self.submitFunc)

        self.cancelTicketBT = QPushButton('Cancel Ticket', self)
        self.cancelTicketBT.setGeometry(30, 90, 150, 25)
        self.cancelTicketBT.clicked.connect(self.cancelTicket)

        self.logoutBT = QPushButton('Log Out', self)
        self.logoutBT.setGeometry(30, 120, 150, 25)
        self.logoutBT.clicked.connect(self.logout)

        self.travelLabel = QLabel('Travel :', self)
        self.travelLabel.setGeometry(220, 190, 120, 20)
        self.travel = QTextBrowser(self)
        self.travel.setGeometry(220, 210, 550, 310)
        self.travelNumLabel = QLabel('Enter selected Travel Number:',self)
        self.travelNumLabel.setGeometry(220, 530, 180, 25)
        self.travelNum = QLineEdit(self)
        self.travelNum.setGeometry(410, 530, 170, 25)
        self.buyBT =QPushButton('Buy',self)
        self.buyBT.setGeometry(600, 530, 170, 26)
        self.buyBT.clicked.connect(self.buy)

# ************************************************************************************************************************************
# *** Sign UP ************************************************************************************************************************
# ************************************************************************************************************************************
class Signup(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Sign up')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(300,210)
        self.signupUiComponents()
        self.show()

    def signupEmailPass(self):
        with open('up.db','r') as updb:
            csvreader = csv.reader(updb)
            for row in csvreader:
                if row[0] == self.personalID.text():
                    msgEmail = QMessageBox().warning(self, 'Warning', 'This ID already exists in the database,\n try logging in or use another ID')
                    return False
        return True

    def signup(self):
        if self.personalID.text() == '' or self.password.text() == '' or self.name.text() == '':
            msgEmpty = QMessageBox.warning(self, 'Warning', 'First 3 filds cant be empty')
            return 0
        if self.signupEmailPass():
            with open('up.db','a',newline='') as updb:
                csvwriter = csv.writer(updb)
                row = [
                    self.personalID.text(),
                    self.password.text(),
                    self.name.text(),
                    self.email.text(),
                    self.phoneNumber.text()
                    ]
                csvwriter.writerow(row)
                msgSuccess = QMessageBox.information(self, 'Success', f'Welcome to our app\nYou have successfully Sing Up')
                self.hide()

    def signupUiComponents(self):
        self.personalIDLabel = QLabel('personal ID :', self)
        self.personalIDLabel.setGeometry(25, 25, 100, 25)
        self.passwordLabel = QLabel('Password :', self)
        self.passwordLabel.setGeometry(25, 50, 100, 25)
        self.nameLabel = QLabel('Name :', self)
        self.nameLabel.setGeometry(25, 75, 100, 25)
        self.emailLabel = QLabel('Email :', self)
        self.emailLabel.setGeometry(25, 100, 100, 25)
        self.phoneNumberLabel = QLabel('Phone Number :', self)
        self.phoneNumberLabel.setGeometry(25, 125, 100, 25)

        self.personalID = QLineEdit(self)
        self.personalID.setGeometry(125, 25, 150, 23)
        self.password = QLineEdit(self)
        self.password.setGeometry(125, 50, 150, 23)
        self.name = QLineEdit(self)
        self.name.setGeometry(125, 75, 150, 23)
        self.email = QLineEdit(self)
        self.email.setGeometry(125, 100, 150, 23)
        self.phoneNumber = QLineEdit(self)
        self.phoneNumber.setGeometry(125, 125, 150, 23)

        self.signupBT = QPushButton('Sign up',self)
        self.signupBT.setGeometry(25, 155, 250, 25)
        self.signupBT.clicked.connect(self.signup)

# ************************************************************************************************************************************
# *** Buy ****************************************************************************************************************************
# ************************************************************************************************************************************
class Buy(QWidget):
    def __init__(self,travelNum,ID):
        super().__init__()
        self.travelNum = travelNum
        self.id = ID

        self.setWindowTitle('Buy')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(300,210)
        self.buyUiComponents()
        self.show()

    def buyUiComponents(self):
        self.lines = list()
        self.travel = []
        with open('trvl.db', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                self.lines.append(row)
                if row == []:
                    continue
                if row[2] == self.travelNum:
                    self.travel = row
                    self.lines.remove(row)
        
        with open('trvl.db', 'w',newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(self.lines)

        #print(self.travel)
        with open('trvl.db','a',newline='') as tdb:
            csvwriter = csv.writer(tdb)

            if self.id not in self.travel[7].split('-'):

                if self.travel[7] == 'str()':
                    self.travel[7] = str(self.id)
                else:
                    temp = f'{self.travel[7]}-{self.id}'
                    self.travel[7] = temp
                
                    
                self.travel[3] = str(int(self.travel[3])-1)
                csvwriter.writerow(self.travel)
                msg = QMessageBox.information(self, 'Succes' , 'thank you for choosing us\nyour perchuse was succesfull')
            
            else:
                #msg = QMessageBox.information(self, 'Fail' , 'You Alredy Bought this Ticket\nYou cant Buy it Again')
                csvwriter.writerow(self.travel)



App = QApplication(sys.argv)
win = UserNOLogedIn()
sys.exit(App.exec())