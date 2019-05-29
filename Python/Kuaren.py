# -*- coding: utf-8 -*-
import sys
from PyQt5 import uic, QtWidgets

from pyDatalog import pyDatalog
pyDatalog.create_terms('X,Y,Z,Preg,Resp')

qtCreatorFile = "Proyecto.ui" 

lista_preguntas=["1. ¿Tienes algun interes disenar programas de computacion<br/> y explorar nuevas apcaciones tecnologicas para uso del internet?"
,"2. ¿Disfrutas de criar, cuidar y tratar animales domesticos y<br/> de campo?"
,"3. ¿Has tenido la curiosidad de investigar sobre areas verdes,<br/> medio ambiente y cambios cmaticos?"
,"4. ¿Has intentado alguna vez ilustrar, dibujar o animar<br/> digitalmente?"
,"5. ¿Sientes alg{un interes en seleccionar, capacitar y motivar al<br/> personal de una organizacion/empresa?"
,"6. ¿Te gustaria reazar excavaciones para descubrir restos del<br/> pasado?"
,"7. ¿Te gusta resolver Problemas de Calculo Matematico?"
,"8. ¿Disfrutas investigando acerca del pasado y saber de historia?"
,"9. ¿Te gusta fotografiar paisajes?"
,"10. ¿Piensas en planificar cuales son las metas de una organizacion<br/> pubca o privada a mediano y largo plazo?"
,"11. ¿Has pensado disenar y planificar la produccion masiva de<br/> articulos?"
,"12. ¿Te gusta la programacion o cosas que tenga que ver con<br/> computadoras?"
,"13. ¿Disfrutas de organizar eventos y atender a sus asistentes?"
,"14. ¿Te gustas atender la salud de personas enfermas?"
,"15. ¿Te has visuazado controlando los ingresos y egresos de fondos y<br/> presentar el balance final de una institucion?"
,"16. ¿Disfrutas de ayudar a la sociedad con los problemas que<br/> tienen?"
,"17. ¿Te gusta la Fisica, Matematica, y todo lo que tenga que<br/> ver con numeros?"
,"18. ¿Investigar y probar nuevos productos farmaceuticos"
,"19. ¿Te vez reazando propuestas y formulando estrategias para<br/> aprovechar las relaciones economicas entre dos paises?"
,"20. ¿Disfrutas de pintar, hacer esculturas, ilustrar bros de<br/> arte, etcetera?"]

lista_respuestas = []



Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pregunta_actual=0
        self.lblPregunta.setText("<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">"+lista_preguntas[self.pregunta_actual]+"</span></p></body></html>")
        self.pregunta_actual=self.pregunta_actual+1
        self.btnSi.clicked.connect(self.afirmativo) 
        self.btnNo.clicked.connect(self.negativo)

    def calcular_respuesta(self):
    	pyDatalog.assert_fact('pregunta','Arte_y_creatividad','Ilustrar, dibujar y animar digitalmente',lista_respuestas[3])
    	pyDatalog.assert_fact('pregunta','Arte_y_creatividad','Fotografiar Paisajes',lista_respuestas[8])
    	pyDatalog.assert_fact('pregunta','Arte_y_creatividad','Disenar logotipos y portadas de una revista',lista_respuestas[10])
    	pyDatalog.assert_fact('pregunta','Arte_y_creatividad','Pintar, hacer esculturas, ilustrar libros de arte, etcetera',lista_respuestas[19])
    	pyDatalog.assert_fact('pregunta','Arte_y_creatividad','Prepararse para ser modelo profesional','X')
    	pyDatalog.assert_fact('pregunta','Arte_y_creatividad','Disenar juegos interactivos electronicos para computadora','X')
    	pyDatalog.assert_fact('pregunta','Arte_y_creatividad','Redactar guiones y libretos para un programa de television','X')
    	pyDatalog.assert_fact('pregunta','Arte_y_creatividad','Crear campanas publicitarias','X')

    	#Area II CIENCIAS SOCIALES
    	pyDatalog.assert_fact('pregunta','sociales','Realizar cavaciones para descubrir restos del pasado',lista_respuestas[5])
    	pyDatalog.assert_fact('pregunta','sociales','Organizar eventos y atender a sus asistentes',lista_respuestas[12])
    	pyDatalog.assert_fact('pregunta','sociales','Investigar el pasado y saber acerca de Historia',lista_respuestas[7])
    	pyDatalog.assert_fact('pregunta','sociales','Ayudar a la sociedad con los problemas que tienen',lista_respuestas[15])
    	pyDatalog.assert_fact('pregunta','sociales','Escribir articulos periodisticos, cuentos, novelas y otros','X')
    	pyDatalog.assert_fact('pregunta','sociales','Estudiar la diversidad cultural en el ambito rural y urbano','X')
    	pyDatalog.assert_fact('pregunta','sociales','Gestionar y evaluar convenios internacionales de cooperacion para el desarrollo social','X')

		# AREA III: ECONOMICA, ADMINISTRATIVA Y FINANCIERA.
    	pyDatalog.assert_fact('pregunta','administrativa','Seleccionar, capacitar y motivar al personal de una organizacion/empresa',lista_respuestas[4])
    	pyDatalog.assert_fact('pregunta','administrativa','Planificar cuales son las metas de una organizacion publica o privada a mediano y largo plazo',lista_respuestas[9])
    	pyDatalog.assert_fact('pregunta','administrativa','Controlar ingresos y egresos de fondos y presentar el balance final de una institucion',lista_respuestas[14])
    	pyDatalog.assert_fact('pregunta','administrativa','Hacer propuestas y formular estrategias para aprovechar las relaciones economicas entre dos paises',lista_respuestas[18])
    	pyDatalog.assert_fact('pregunta','administrativa','Elaborar campanas para introducir un nuevo producto al mercado','X')
    	pyDatalog.assert_fact('pregunta','administrativa','Supervisar las ventas de un centro comercial','X')
    	pyDatalog.assert_fact('pregunta','administrativa','Aconsejar a las personas sobre planes de ahorro e inversiones','X')
    	pyDatalog.assert_fact('pregunta','administrativa','Tener un negocio propio de tipo comercial','X')
    	pyDatalog.assert_fact('pregunta','administrativa','Organizar un plan de distribucion y venta de un gran almacen','X')

    	# AREA IV: CIENCIA Y TECONOLOGIA.
    	pyDatalog.assert_fact('pregunta','ciencia_y_tecnologia','Disenar programas de computacion y plorar nuevas aplicaciones tecnologicas para uso del internet',lista_respuestas[0])
    	pyDatalog.assert_fact('pregunta','ciencia_y_tecnologia','Resolver Problemas de Calculo Matematico',lista_respuestas[6])
    	pyDatalog.assert_fact('pregunta','ciencia_y_tecnologia','Te gusta la programacion o cosas que tenga que ver con computadoras',lista_respuestas[11])
    	pyDatalog.assert_fact('pregunta','ciencia_y_tecnologia','Te gusta la Fisica, Matematica, y todo lo que tenga que ver con numeros',lista_respuestas[16])
    	pyDatalog.assert_fact('pregunta','ciencia_y_tecnologia','Investigar y probar nuevos productos farmaceuticos','X')
    	pyDatalog.assert_fact('pregunta','ciencia_y_tecnologia','Disenar maquinas que puedan simular actividades humanas','X')
    	pyDatalog.assert_fact('pregunta','ciencia_y_tecnologia','Elaborar mapas, planos e imagenes para el estudio y analisis de datos geograficos','X')

    	# AREA V: CIENCIAS ECOLOGICAS, BIOLOGICAS Y DE SALUD.
    	pyDatalog.assert_fact('pregunta','biologia_y_salud','Criar, cuidar y tratar animales domesticos y de campo',lista_respuestas[1])
    	pyDatalog.assert_fact('pregunta','biologia_y_salud','Investigar sobre areas verdes, medio ambiente y cambios climaticos',lista_respuestas[2])
    	pyDatalog.assert_fact('pregunta','biologia_y_salud','Disenar cursos para ensenar a la gente sobre temas de salud e higiene','X')
    	pyDatalog.assert_fact('pregunta','biologia_y_salud','Atender la salud de personas enfermas',lista_respuestas[13])
    	pyDatalog.assert_fact('pregunta','biologia_y_salud','Hacer experimentos con plantas (frutas, arboles, flores)','X')
    	pyDatalog.assert_fact('pregunta','biologia_y_salud','Examinar y tratar los problemas visuales','X')
    	pyDatalog.assert_fact('pregunta','biologia_y_salud','Realizar el control de calidad de los alimentos',lista_respuestas[17])
    	pyDatalog.assert_fact('pregunta','biologia_y_salud','Atender y realizar ejercicios a personas que tienen limitaciones fisicas, problemas de lenguaje, etcetera','X')

    	s=str(pyDatalog.ask('pregunta(X,_,si)'))

    	SaveMax=max([s.count("biologia_y_salud"),
    		s.count("ciencia_y_tecnologia"),
			s.count("administrativa"),
			s.count("sociales"),
			s.count("Arte_y_creatividad")])

    	respuesta=""

    	if s.count("biologia_y_salud") == SaveMax:
    		respuesta=respuesta+"estudia una carrera del area de biologia y salud:  Biología, Farmacia, Zootecnia, Veterinaria, Medicina, Enfermería. <br/>"
    	if s.count("ciencia_y_tecnologia") == SaveMax:
    		respuesta=respuesta+"estudia una carrera del area de las ciencia y tecnologia: Ingenieria en sistemas, Ingenieria Civil, Electrónica, Física, Matemáticas, Ingeniería Mecatrónica. <br/>"
    	if s.count("administrativa") == SaveMax:
    		respuesta=respuesta+"estudia una carrera del area de las ciencias administrativas: Administración, Ingeniería comercial, Marketing, Gestión y Negocios internacionales, Finanzas.  <br/>"
    	if s.count("sociales") == SaveMax:
    		respuesta=respuesta+"estudia una carrera del area de las ciencias sociales: Trabajo Social, Historia y Geografía, Periodismo, Antropología, Arqueología.<br/>"
    	if s.count("Arte_y_creatividad") == SaveMax:	
    		respuesta=respuesta+"estudia una carrera del area de la facultad de belleas artes: Diseño Gráfico, Artes plasticas, Publicidad, Fotografía, actuación. <br/>"

    	self.lblRespuesta.setText("<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">"+respuesta+"</span></p></body></html>")


    def afirmativo(self):
    	if self.pregunta_actual==20:
    		lista_respuestas.append("si")
    		self.calcular_respuesta()
    	else:	
    		lista_respuestas.append("si")
    		self.lblPregunta.setText("<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">"+lista_preguntas[self.pregunta_actual]+"</span></p></body></html>")
    		self.pregunta_actual=self.pregunta_actual+1
    		
    def negativo(self):
	   	if self.pregunta_actual==20:
	   		lista_respuestas.append("no")
	   		self.calcular_respuesta()
	   	else:	
	   		lista_respuestas.append("no")
	   		self.lblPregunta.setText("<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">"+lista_preguntas[self.pregunta_actual]+"</span></p></body></html>")
	   		self.pregunta_actual=self.pregunta_actual+1

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())