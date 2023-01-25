import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout,QRadioButton,QTextEdit,QHBoxLayout,QFileDialog
from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow,QLineEdit

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.etiket=QLabel("Min rating degerini giriniz: ")
        self.ilk=QLineEdit()
        self.veri=QLabel("")
        self.buton=QPushButton("Sirala")

        v_box=QVBoxLayout()
        v_box.addWidget(self.etiket)
        v_box.addWidget(self.ilk)
        v_box.addWidget(self.veri)
        v_box.addWidget(self.buton)

        h_box=QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("Imdb verileri")
        self.buton.clicked.connect(self.imdb)
        self.show()
    def imdb(self):
        self.a=""
        self.url="https://www.imdb.com/chart/top/"
        self.response=requests.get(self.url)
        self.html_icerigi=self.response.content
        self.soup=BeautifulSoup(self.html_icerigi,"html.parser")
        self.basliklar=self.soup.find_all("td",{"class":"titleColumn"})
        self.ratingler=self.soup.find_all("td",{"class","ratingColumn imdbRating"})
        for baslik, rating in zip(self.basliklar,self.ratingler):
            baslik=baslik.text
            rating=rating.text

            baslik=baslik.strip()
            baslik=baslik.replace("\n","")

            rating=rating.strip()
            rating=rating.replace("\n","")
            if(float(rating)>float(self.ilk.text())):
                self.a=self.a + baslik  + " " + rating + "\n"
        self.veri.setText(self.a)




app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())