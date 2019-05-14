/*
Tenemos el siguiente conocimiento directo:

Pedro padece gripe.
Pedro padece hepatitis
Juan padece hepatitis
María padece gripe
Carlos padece intoxicación
La fiebre es síntoma de gripe
El cansancio es síntoma de hepatitis
La diarrea es síntoma de intoxicación
El cansancio es síntoma de gripe
La aspirina suprime la fiebre
El Lomotil suprime la diarrea

Además podemos aportar el siguiente conocimiento inferido:

Un fármaco alivia una enfermedad si la enfermedad tiene un síntoma que sea suprimido por
el fármaco.

Una persona debería tomar un fármaco si padece una enfermedad que sea aliviada por el
fármaco.

Construir un programa que refleje dicho conocimiento y permita resolver las siguientes
cuestiones:

1) ¿Podemos conocer qué dolencia tiene Pedro? ¿Y María?
padece(pedro,Que_dolencia_tiene).
padece(maria,Que_dolencia_tiene).

2) ¿Quién padece gripe?
 padece(Enfermo,gripe).
 
3) ¿Qué síntomas tiene Pedro?
 padece(pedro,Enfermedad),sintoma(Sintoma,Enfermedad).
 
4) ¿Quién padece diarrea?
padece(Paciente,Enfermedad),sintoma(diarrea,Enfermedad).


5) ¿Y quién está cansado?
padece(Paciente,Enfermedad),sintoma(cansancio,Enfermedad).

6) ¿Hay algún fármaco que alivie a Pedro?
 recertar_a(pedro,Farmaco).
 
7) ¿Hay algún síntoma que compartan Juan y María?
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

