%Muestra los elementos la lista dejando un linea entre ellas

% Dos formas de crear una regla para mostra listas
mostrarLista(Lista) :- Lista=[Cabeza|Resto],write(Cabeza),nl,mostrarLista(Resto).

%% mostrarLista([]).
%% mostrarLista(Lista) :- Lista=[Cabeza|Resto],write(Cabeza),nl,mostrarLista(Resto).


%Determina si un elemento es miembro de una lista
miembro(X,[X| _ ]).
miembro(X,[ _ |R]):-miembro(X,R).