import sys
from PyQt5 import uic, QtWidgets
from base_conocimientos import *

qtCreatorFile = "gui.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.busqueda.clicked.connect(self.makeSearch)
        #self.seleccion.clicked.connec(self.refrescar)
    
    def excersice(self):
        return self.seleccion.currentIndex()
    
    def refrescar(self):
        if(self.seleccion.currentIndex() == 0):
            asks
            self.seleccion.setItemText(0,"Abuelos paternos")
            self.seleccion.setItemText(0,"Abuelos maternos")
        else:
            self.seleccion.setItemText(0,"Abuelos paternos")
            self.seleccion.setItemText(0,"Abuelos maternos")
    
    def makeSearch(self):
        hijo = self.entrada.toPlainText()
        opcion = self.abuelos.currentIndex()
        if(opcion == 0):
            resultado1 = abuelopaterno(hijo)
            resultado2 = abuelapaterna(hijo)
        elif(opcion == 1):
            resultado1 = abuelomaterno(hijo)
            resultado2 = abuelamaterna(hijo)
        if((str(resultado1) or str(resultado2)) == '[]'):
            self.salida.setText('No tiene abuelos en la base de conocimiento.')
        else:
            self.salida.setText(str(resultado1)+'\n------\n'+str(resultado2))
            

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())