padre(juan,carlos).
padre(juan,rosario).
padre(juan,soltero).
padre(victor,belen).
padre(carlos,elena).
padre(carlos,carlitos).
madre(maria,soltero).
madre(maria,carlos).
madre(maria,rosario).
madre(consuelo,belen).
madre(belen,elena).
madre(belen,carlitos). 

hermano_de(Hermano1,Hermano2) :- padre(Padre,Hermano1), padre(Padre,Hermano2), 
  madre(Madre,Hermano1), madre(Madre,Hermano2), Hermano1\=Hermano2.

/* SEGUN EJERCICIO
abuelo(Ab,Nieto) :- padre(Ab,Hijo) , padre(Hijo,Nieto). 
abuelo(Ab,Nieto) :- padre(Ab,Hija) , madre(Hija,Nieto). 

abuela(Ab,Nieto) :- madre(Ab,Hijo) , padre(Hijo,Nieto). 
abuela(Ab,Nieto) :- madre(Ab,Hija) , madre(Hija,Nieto). 
*/

/* ABUELOS PATERNO */
abuelo_paterno(X,Y) :- write('Abuelo Paterno'), padre(X,Z),padre(Z,Y).
abuelo_paterno(X,Y) :-  write('Abuela Paterna'), madre(X,Z), padre(Z,Y).


/* ABUELOS MATERNOS */
abuelo_materno(X,Y) :- write('Abuelo Materno'), padre(X,Z),madre(Z,Y).
abuelo_materno(X,Y) :- write('Abuela Materna'), madre(X,Z),madre(Z,Y).