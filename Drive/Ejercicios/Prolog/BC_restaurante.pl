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

/*Cuando existen varios casos en que una relación se cumple, es decir una disyunción, se debe crear una
regla para cada caso.*/
/*
plato_principal(P) :- carne(P). %P es un plato_principal si P es un plato de carne.
plato_principal(P) :- pescado(P). %P es un plato_principal si P es un plato de pescado.
*/
plato_principal(P) :- carne(P); pescado(P).

/*HAGAMOS LA SIGUIENTE CONSULTA plato_principal(P). */

/* Tratamos a continuación la composición de una comida completa.
interpreta así: E,P,D satisfacen la relación comida si E satisface la 
relación entrada, si P satisface la relación plato_principal y D satisface la 
relación postre. */
comida(E,P,D) :- entrada(E), plato_principal(P), postre(D). 

/*HAGAMOS LA SIGUIENTE CONSULTA comida(E,P,D). */

/*HAGAMOS LA SIGUIENTE CONSULTA se desea conocer las comidas que contienen un plato de 
pescado  Esta pregunta se formula así: comida(E,P,D), pescado(P). */

