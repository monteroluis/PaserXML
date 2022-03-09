import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTreeWidgetItem, QDialog
import xml.etree.ElementTree as et

class Inicio(QMainWindow):

   def __init__(self):
      super().__init__()
      self.inicializarGui()


   def inicializarGui(self):
       uic.loadUi('interfaz.ui', self)
       self.show()
       doc = open('Archivos/Concesionario.xml', 'r').read()
       self.mostrarArbol(self,doc)

   def mostrarArbol(self, s):
       tree = et.fromstring(s)
       self.treeWidget.setColumnCount(1)
       a = QTreeWidgetItem([tree.tag])
       self.treewidget.addTopLevelItem(a)

   def displaytree(a, s):
       for child in s:
           branch = QTreeWidgetItem([child.tag])
           a.addChild(branch)
          # displaytree(branch, child)

def main():
   app=QApplication(sys.argv)
   ventana=Inicio()
   sys.exit(app.exec())

if __name__=="__main__":
    main()