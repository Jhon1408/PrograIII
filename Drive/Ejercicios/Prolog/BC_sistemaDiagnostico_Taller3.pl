/*
Tenemos el siguiente conocimiento directo:

Pedro padece gripe.
Pedro padece hepatitis
Juan padece hepatitis
Mar�a padece gripe
Carlos padece intoxicaci�n
La fiebre es s�ntoma de gripe
El cansancio es s�ntoma de hepatitis
La diarrea es s�ntoma de intoxicaci�n
El cansancio es s�ntoma de gripe
La aspirina suprime la fiebre
El Lomotil suprime la diarrea

Adem�s podemos aportar el siguiente conocimiento inferido:

Un f�rmaco alivia una enfermedad si la enfermedad tiene un s�ntoma que sea suprimido por
el f�rmaco.

Una persona deber�a tomar un f�rmaco si padece una enfermedad que sea aliviada por el
f�rmaco.

Construir un programa que refleje dicho conocimiento y permita resolver las siguientes
cuestiones:

1) �Podemos conocer qu� dolencia tiene Pedro? �Y Mar�a?
padece(pedro,Que_dolencia_tiene).
padece(maria,Que_dolencia_tiene).

2) �Qui�n padece gripe?
 padece(Enfermo,gripe).
 
3) �Qu� s�ntomas tiene Pedro?
 padece(pedro,Enfermedad),sintoma(Sintoma,Enfermedad).
 
4) �Qui�n padece diarrea?
padece(Paciente,Enfermedad),sintoma(diarrea,Enfermedad).


5) �Y qui�n est� cansado?
padece(Paciente,Enfermedad),sintoma(cansancio,Enfermedad).

6) �Hay alg�n f�rmaco que alivie a Pedro?
 recertar_a(pedro,Farmaco).
 
7) �Hay alg�n s�ntoma que compartan Juan y Mar�a?
padece(juan,Enfermedad),padece(maria,Enfermedad),sintoma(Sintoma,Enfermedad).

*/


padece(pedro,gripe).
padece(pedro,hepatitis).
padece(juan,hepatitis).
padece(maria,gripe).
padece(carlos,intoxicacion).
sintoma(fiebre,gripe).
sintoma(cansancio,hepatitis).
sintoma(diarrea,intoxicacion).
sintoma(cansancio,gripe).
suprime(aspirina,fiebre).
suprime(lomotil,diarrea).

cura(Enfermedad,Farmaco) :- sintoma(Sintoma,Enfermedad),suprime(Farmaco,Sintoma).
recertar_a(Paciente,Farmaco) :- padece(Paciente,Enfermedad),cura(Enfermedad,Farmaco).

