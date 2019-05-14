from pyDatalog import pyDatalog, pyEngine
import logging

pyEngine.Logging = True
logging.basicConfig(level=logging.INFO)

pyDatalog.create_terms('printmore_,W,X,Y,Z,padre,madre,hermano_de,Hermano1,Hermano2,Padre,Madre,abuelo')

+padre('juan','carlos')
+padre('juan','rosario')
+padre('juan','soltero')
+padre('victor','belen')
+padre('carlos','elena')
+padre('carlos','carlitos')
+madre('maria','soltero')
+madre('maria','carlos')
+madre('maria','rosario')
+madre('consuelo','belen')
+madre('belen','elena')

# def printmore_(x,y):
#   print('Printmore')
#   print('Valor X: {}').format(x.data)
#   print('Valor Y: {}').format(y.data)

# REGLA PARA HERMANOS CON SINTAXIS PROLOG
# hermano_de(Hermano1,Hermano2) :- padre(Padre,Hermano1), padre(Padre,Hermano2), 
#   madre(Madre,Hermano1), madre(Madre,Hermano2), Hermano1\=Hermano2.

hermano_de(Hermano1,Hermano2) <= padre(Padre,Hermano1) & padre(Padre,Hermano2) & madre(Madre,Hermano1)& madre(Madre,Hermano2)& (Hermano1!=Hermano2) 

# nombre_hermano=raw_input('Ingrese el nombre del hermano que desea buscar:')
# print('El/Los herman@s de ' + nombre_hermano  + ' son: ' )
# resultado = hermano_de('carlos',Hermano2)
# print(resultado)


# # REGLA PARA HERMANOS CON SINTAXIS PYDATALOG
def pedir_por_pantalla():
  nombre_hermano=raw_input('Ingrese el nombre del hermano que desea buscar:')
  return nombre_hermano

def usar_regla(nombre_hermano):
  resultado = hermano_de(nombre_hermano,Hermano2)
  return resultado

def mostrar_resultado(resultado):
  print(resultado)

def main():
  nombre_hermano = pedir_por_pantalla()
  resultado = usar_regla(nombre_hermano)
  mostrar_resultado(resultado)

main()