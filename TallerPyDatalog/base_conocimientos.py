# -*- coding: utf-8 -*-
from pyDatalog import pyDatalog

pyDatalog.create_terms('padre,madre,X,Y,Z,A,abuelos_paternos,abuelos_maternos,abuelas_paternas,abuelas_maternas,Abuelo,Abuela')
pyDatalog.create_terms('tiene,enfermo_de,tiene_sintoma,sintoma_de,elimina,recetar_a,alivia')

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
+madre('belen','carlitos')

abuelos_paternos(Y,X) <= padre(Z,X) & padre(Y,Z)
abuelas_paternas(Y,X) <= padre(Z,X) & madre(Y,Z)
abuelos_maternos(Y,X) <= madre(Z,X) & padre(Y,Z)
abuelas_maternas(Y,X) <= madre(Z,X) & madre(Y,Z)

def abuelopaterno(nombre):
  resultado = abuelos_paternos(Abuelo,nombre)
  return resultado

def abuelomaterno(nombre):
  resultado = abuelos_maternos(Abuelo,nombre)
  return resultado

def abuelapaterna(nombre):
  resultado = abuelas_paternas(Abuela,nombre)
  return resultado

def abuelamaterna(nombre):
  resultado = abuelas_maternas(Abuela,nombre)
  return resultado

+enfermo_de('manuel','gripa')
+tiene_sintoma('alicia','cansancio')

+sintoma_de('fiebre','gripe')
+sintoma_de('tos','gripe')
+sintoma_de('cansancio','anemia')

+elimina('vitaminas','cansancio')
+elimina('aspirinas','fiebre')
+elimina('jarabe','tos')

recetar_a(X,Y) <= enfermo_de(Y,A) & alivia(X,A)
alivia(X,Y) <= elimina(X,A) & sintoma_de(A,Y)
tiene(X,Y) <= tiene_sintoma(X,Z) & sintoma_de(Z,Y)


