padre(juan,pedro).
padre(jose,pedro).
padre(maria,pedro).
padre(pedro,pablo).
padre(ana,alberto).

madre(juan,ana).
madre(jose,ana).
madre(maria,ana).
madre(pedro,juanita).
madre(ana,julia).

abuelo_paterno(X,Y) :- padre(X,Z),padre(Z,Y).

hijo(X,Y) :- padre(Y,X).
hijo(X,Y) :- madre(Y,X).

descendiente(X,Y) :- hijo(X,Y).
descendiente(X,Y) :- hijo(X,Z),descendiente(Z,Y).

ancestro(X,Y) :- padre(X,Y).
ancestro(X,Y) :- madre(X,Y).
ancestro(X,Y) :- padre(X,Z),ancestro(Z,Y).
ancestro(X,Y) :- madre(X,Z),ancestro(Z,Y).

append([],L,L).
append([E|R1],L,[E|R2]) :- append(R1,L,R2).

sublista(S,L) :- append(_,X,L),append(S,_,X).
sublista([E|R],L) :- append(_,X,L),append([E|R],_,X).