entrada(antipasto). 
entrada(sopa). 
entrada(quesos). 
carne(milanesa). 
carne(bife_de_chorizo). 
carne(pollo_asado). 
pescado(congrio). 
pescado(pejerey). 
postre(flan). 
postre(helado). 
postre(fruta). 

/*Cuando�existen�varios�casos�en�que�una�relaci�n�se�cumple,�es�decir�una�disyunci�n,�se�debe�crear�una
regla�para�cada�caso.*/
/*
plato_principal(P) :- carne(P). %P es un plato_principal si P es un plato de carne.
plato_principal(P) :- pescado(P). %P es un plato_principal si P es un plato de pescado.
*/
plato_principal(P) :- carne(P); pescado(P).

/*HAGAMOS LA SIGUIENTE CONSULTA plato_principal(P). */

/* Tratamos a continuaci�n la composici�n de una comida completa.
interpreta as�: E,P,D satisfacen la relaci�n comida si E satisface la 
relaci�n entrada, si P satisface la relaci�n plato_principal y D satisface la 
relaci�n postre. */
comida(E,P,D) :- entrada(E), plato_principal(P), postre(D). 

/*HAGAMOS LA SIGUIENTE CONSULTA comida(E,P,D). */

/*HAGAMOS LA SIGUIENTE CONSULTA se desea conocer las comidas que contienen un plato de 
pescado  Esta pregunta se formula as�: comida(E,P,D), pescado(P). */

