import sys
from datetime import date, datetime
from time import sleep
import PyQt5
from PyQt5.QtWidgets import QHBoxLayout, QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout
from PyQt5.QtCore import QTimer
import random
import time
class Reflex(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.etiket=QLabel("Reflex Test")
        self.etiket1=QLabel("")
        self.buton=QPushButton()
    
        v_box=QVBoxLayout()
        v_box.addWidget(self.etiket)
        v_box.addWidget(self.buton)
        v_box.addWidget(self.etiket1)

        h_box=QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("Reflex Test")
        self.show()
        self.cheat=0
        self.moment4=datetime.now()
        self.moment44=datetime.timestamp(self.moment4)
        a=random.randrange(3000,6000)
        QTimer.singleShot(a,self.red)
        self.buton.clicked.connect(self.reflex_time)
    def reflex_time(self):
        if self.cheat==2:
            self.moment2=datetime.now()
            self.moment22=datetime.timestamp(self.moment2)
            self.moment3=self.moment22-self.moment11
            self.etiket1.setText(str(format(self.moment3,".3f")))
        else:
            self.etiket1.setText("You pressed the button before its red!!")
    def red(self):

        self.buton.setStyleSheet("background-color: red")
        self.moment1=datetime.now()
        self.moment11=datetime.timestamp(self.moment1)
        self.cheat=2



app=QApplication(sys.argv)
reflex=Reflex()
sys.exit(app.exec_())