

from PySide6.QtWidgets import (QDialog,
                                QMessageBox)
from ui.login import *
from Database import *

class Ui_Login(QDialog):
    #database connection
    db = None
    userId = ""
    def __init__(self, parent=None):
        super(Ui_Login, self).__init__(parent)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.pushButton_login.clicked.connect(self.clickLogin)
        #databese
        self.db = Database()

    def clickLogin(self):
        userId = self.ui.lineEdit_userid.text()
        password = self.ui.lineEdit_password.text()
        print(userId, password)
        if len(userId) == 0 or len(password) == 0:
            QMessageBox.information(None, "Information", "Input user Id and password.", QMessageBox.Yes)
            return            
        if self.db.checkPassword(userId, password) == False:
            QMessageBox.information(None, "Information", "User ID or password is not correct.", QMessageBox.Yes)
            return
        self.userId = userId
        self.close()

    def getUserId(self):
        return self.userId