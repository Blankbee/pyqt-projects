import sys
import sqlite3
from PyQt5 import QtWidgets
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.create_con()
    def create_con(self):
        con=sqlite3.connect("database_l.db")
        self.cursor=con.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Members (username TEXT,password TEXT)")
        con.commit()
    def init_ui(self):
        self.username=QtWidgets.QLineEdit()
        self.password=QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login=QtWidgets.QPushButton("Login")
        self.register=QtWidgets.QPushButton("Register")
        self.yazi_alani=QtWidgets.QLabel("")

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.username)
        v_box.addWidget(self.password)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.login)
        v_box.addWidget(self.register)

        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("User Login")
        self.login.clicked.connect(self.log_in)
        self.register.clicked.connect(self.registerf)
        self.show()
    def log_in(self):
        name=self.username.text()
        pw=self.password.text()
        self.cursor.execute("SELECT * FROM Members WHERE username=? and password=?",(name,pw))
        data=self.cursor.fetchall()
        if(len(data)==0):
            self.yazi_alani.setText("Username doesnt exists\nPlease try again")
        else:
            self.yazi_alani.setText("Welcome " + name)
    def registerf(self):
        name=self.username.text()
        pw=self.password.text()
        con=sqlite3.connect("pyqt/database_l.db")
        self.cursor=con.cursor()
        self.cursor.execute("INSERT INTO Members VALUES (?,?)",(name,pw))
        con.commit()
        self.yazi_alani.setText("Succesfully Registered")



app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())