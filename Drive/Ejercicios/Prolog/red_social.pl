esHombre(pedro).
esHombre(juan).
mujer(maria).
mujer(elena).
mujer(raquel).
mujer(belen).
gusta(juan,maria).
gusta(juan,elena).
gusta(pedro,raquel).
gusta(pedro,belen).
gusta(pedro,maria).
gusta(esHombre(pedro),raquel).


/*Con la variable anónima ( _ ), cuando estamos interesados en saber si existe
algún objeto que cumpla un objetivo. En el objetivo, la variable anónima hay que
verla como una variable libre, sin ninguna cuantificación, que forzará una única
sustitución: la primera que se encuentre.

Las variables anónimas son aquellas cuyo nombre es sólo el
carácter subrayado (_). Se usan cuando no es importante el nombre de la variable o
cuando la variable no puede unificar con otra, dentro de la misma cláusula.

?- gusta(X,maria).  ¿A quién le gusta María 
?- gusta(_,maria).  ¿Hay alguien a quien le gusta María
?- gusta(maria,_).  ¿Hay alguien que le guste a María
?- gusta(juan,X) , gusta(maria,Y).
?- gusta(juan,X) , gusta(maria,X).


gusta(_,maria). % ∀x (gusta(x,maria))

¿Hay algun hombre que le guste raquel?

*/

%Tiene pedro y juan los mismos gustos?

mismos_gusto(X,Y) :- gusta(X,W),gusta(Y,W).
