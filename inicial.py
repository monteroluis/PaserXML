import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QTreeWidgetItem
import xml.etree.ElementTree as et

class Mainwindow(QDialog):
      def __init__(self):
        super(Mainwindow,self).__init__()
        loadUi("interfaz.ui",self)
        #self.mostrararbol()


app=QApplication(sys.argv)
mainwindow = Mainwindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(850)
widget.setFixedWidth(850)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("saliendo")