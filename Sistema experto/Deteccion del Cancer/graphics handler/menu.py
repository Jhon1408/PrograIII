import sys
from PyQt5 import uic, QtWidgets
from processing import pacienteInput

menu = "gui.ui"
paciente = "paciente.ui"
result = "result.ui"
doctor = "doctor.ui"

menuForm, base_1 = uic.loadUiType(menu)
pacienteForm, base_2 = uic.loadUiType(paciente)
result, base_3 = uic.loadUiType(result)
doctor, base_4 = uic.loadUiType(doctor)

class menu(QtWidgets.QMainWindow, menuForm):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        menuForm.__init__(self)
        self.setupUi(self)
        self.pacienteButton.clicked.connect(self.change)
        self.doctorButton.clicked.connect(self.doctorBut)
        
    def change(self):
        self.paciente = paciente()
        self.paciente.show()
        self.close()
    
    def doctorBut(self):
        self.doctorWindow = doctor()
        self.doctorWindow.show()
        self.close()

class result(base_3, result):
    def __init__(self):
        super(base_3, self).__init__()
        self.setupUi(self)
        self.exitButton.clicked.connect(self.close)

class paciente(base_2, pacienteForm):
    def __init__(self):
        super(base_2, self).__init__()
        self.setupUi(self)
        self.enviarButton.clicked.connect(self.send)
        
    def send(self):
        sexo = ''
        if(self.masculino.isChecked()):
            sexo = 'masculino'
        if(self.femenino.isChecked()):
            sexo = 'femenino'
        
        paciente = pacienteInput.pacienteInput()
        paciente.insertPersonal(sexo,self.edad.value())
        paciente.insertCancer(self.cancermama.isChecked(),self.cancerrinon.isChecked(),self.cancerpulmon.isChecked(),self.cancercolon.isChecked())
        paciente.insertSintomas(self.memoria.isChecked(),self.nauseas.isChecked(),self.vista.isChecked(),self.vomito.isChecked(),self.comportamiento.isChecked(),self.convulsiones.isChecked(),self.debilidad.isChecked(),self.dolor_cabeza.isChecked(),self.movimiento.isChecked())
        paciente.insertFamiliares(self.abuelos.isChecked(),self.tios.isChecked(),self.padres.isChecked())
        
        self.result = result()
        self.result.show()
        self.result.out.setHtml(str(paciente.mostrarResultado()))
        
class doctor(base_4, doctor):
    def __init__(self):
        super(base_4, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = menu()
    window.show()
    sys.exit(app.exec_())