# -*- coding: utf-8 -*- 
from pyDatalog import pyDatalog, pyEngine
import logging

pyEngine.Logging = True
logging.basicConfig(level=logging.INFO)

# def regla_menu(atributo, opcion):
#   print('Atributo: {} opcion: {}').format(atributo,opcion)
#   assert_fact( 'tiene_sintoma', 'yes', organo, sintoma )

pyDatalog.create_terms('X, Y, Z, Sintoma, Organo,Enfermedad,tratamiento_enfermedad, print_, twice, tiene_sintoma, diagnostico, enfermedad')

tratamiento_enfermedad = {
  'moko': """ Para el manejo de la enfermedad se requiere con rmar el diagnóstico por parte del ICA y desarrollar el proceso de 
          erradicación de plantas afectadas y el control de focos de acuerdo con los protocolos de erradicación del ICA."""
}



+tiene_sintoma('hoja','seca') 
+tiene_sintoma('hoja','quebradiza')

lista_menu = ['seca', 'quebradiza', 'no_se_desprende', 'seca_en_bordes', 'franja_color_amarilla_intenso', 'amarillamiento_total', 'amarillamiento']

diagnostico(Enfermedad, Sintoma) <= tiene_sintoma(Organo, Sintoma) & (Enfermedad == 'moko')
enfermedad('moko') <= tiene_sintoma('hoja','seca') & tiene_sintoma('hoja','quebradiza')
#diagnostico('moko') <= tiene_sintoma(Organo, Sintoma1), tiene_sintoma(Organo, Sintoma2) & (Sintoma1 != Sintoma2)
#diagnostico(Enfermedad, Sintoma1,Sintoma2) <= tiene_sintoma('hoja',Sintoma1) & tiene_sintoma('hoja',Sintoma2) & (Sintoma1 != Sintoma2) & (Enfermedad == 'moko')

def mostrar_tratamiento(enfermedad):
  print(""" 
    Enfermedad: {}
    Tratamiento: {}
    """).format(enfermedad, tratamiento_enfermedad[enfermedad])

def print_(x):
    print('Print es {}: ').format(type(x))

def mostrar_resultado(resultado):
  mostrar_tratamiento(resultado.v()[0])

def pedir_por_pantalla(lista_menu):
  nombre_sintoma=raw_input('Seleccione: ' + str(lista_menu))
  return nombre_sintoma

def usar_regla(nombre_sintoma):
  resultado = diagnostico(Enfermedad,nombre_sintoma)
  return resultado

nombre_sintoma = pedir_por_pantalla(lista_menu)
resultado = usar_regla(nombre_sintoma)
mostrar_resultado(resultado)
