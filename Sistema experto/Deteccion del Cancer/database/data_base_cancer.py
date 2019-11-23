from pyDatalog import pyDatalog

pyDatalog.create_terms('sintoma,cancer,tratamiento,revision')

#Sintomas (X es sintoma de Y)
+ sintoma(('Nauseas','Vomitos','Dolor de cabeza'),'Gliomas')
+ sintoma(('Perdida de la memoria','Convulsiones'),'TCG')
+ sintoma(('Problemas de vision','Dolor de cabeza','Dificultad de movimiento'),'Adenomas')
+ sintoma(('Nauseas','Problemas de vision'),'Neurinomas')
+ sintoma(('Perdida de la memoria','Dolor de cabeza'),'Meningiomas')
+ sintoma(('Nauseas','Problemas de vision','Dolor de cabeza'),'Meduloblastomas')
+ sintoma(('Cambios de comportamiento','Convulsiones','Debilidad'),'Craneofaringiomas')

#tipos de cancer
+ cancer('Cancer de mama','Metastasico')
+ cancer('Cancer de colon','Metastasico')
+ cancer('Cancer de rinon','Metastasico')
+ cancer('Cancer de pulmon','Metastasico')
+ cancer('Melanoma','Metastasico')
+ cancer('TCG','Primario')
+ cancer('Gliomas','Primario')
+ cancer('Adenomas','Primario')
+ cancer('Neurinomas','Primario')
+ cancer('Meningiomas','Primario')
+ cancer('Meduloblastomas','Primario')
+ cancer('Craneofaringiomas','Primario')

#Canceres primarios
+ tratamiento('Adenomas','Quimioterapia')
+ tratamiento('Neurinomas','Quimioterapia')
+ tratamiento('Meningiomas','Quimioterapia')
+ tratamiento('Gliomas','Radioterapia')
+ tratamiento('Meduloblastomas','Cirugia')
+ tratamiento('Craneofaringiomas','Cirugia')
+ tratamiento('Gliomas','Quimioterapia')
+ tratamiento('Gliomas','Cirugia')


#Canceres metastasicos
+ revision('Metastasico','RMN_de_la_cabeza')
+ revision('Metastasico','RMN_de_la_columna')
+ revision('Metastasico','RMNF_Cerebral')
+ revision('Metastasico','TC_de_la_cabeza')
+ revision('Metastasico','Biopsia')
+ revision('Metastasico','Diseminacion')

