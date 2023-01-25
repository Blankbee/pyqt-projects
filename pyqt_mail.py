import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout,QRadioButton,QTextEdit,QHBoxLayout,QFileDialog
from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow,QLineEdit

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.mail1=QLabel("Mail adresinizi giriniz: ")
        self.mail2=QLabel("Hedef mail adresini giriniz: ")
        self.pw=QLabel("Mailinizin sifresini girin: ")
        self.konu=QLabel("Mailinizin konusu: ")
        self.icerik=QLabel("Mailin icerigi: ")
        self.mail11=QLineEdit()
        self.mail21=QLineEdit()
        self.pw1=QLineEdit()
        self.pw1.setEchoMode(QLineEdit.Password)
        self.icerik1=QTextEdit()
        self.konu1=QLineEdit()
        self.buton=QPushButton("Gonder")
        self.sonuc=QLabel("")

        v_box=QVBoxLayout()
        v_box.addWidget(self.mail1)
        v_box.addWidget(self.mail11)
        v_box.addWidget(self.mail2)
        v_box.addWidget(self.mail21)
        v_box.addWidget(self.pw)
        v_box.addWidget(self.pw1)
        v_box.addWidget(self.konu)
        v_box.addWidget(self.konu1)
        v_box.addWidget(self.icerik)
        v_box.addWidget(self.icerik1)
        v_box.addStretch()
        v_box.addWidget(self.sonuc)
        v_box.addWidget(self.buton)

        h_box=QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("Mail Gonderme")
        self.buton.clicked.connect(self.mail)
        self.show()
    def mail(self):
        self.mesaj=MIMEMultipart()
        self.mesaj["From"]=self.mail11.text()
        self.mesaj["To"]=self.mail21.text()
        self.mesaj["Subject"]=self.konu1.text()
        self.yazi=self.icerik1.toPlainText()
        self.mesaj_govdesi=MIMEText(self.yazi,"plain")
        self.mesaj.attach(self.mesaj_govdesi)
        try:
            self.mail=smtplib.SMTP("smtp.gmail.com",587)
            self.mail.ehlo()
            self.mail.starttls()
            self.mail.login(self.mail11.text(),self.pw1.text())
            self.mail.sendmail(self.mesaj["From"],self.mesaj["To"],self.mesaj.as_string())
            self.sonuc.setText("Mail gonderme basarili.")
            self.mail.close()
        except:
            self.sonuc.setText("Bir sorun oluştu.")

app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())
