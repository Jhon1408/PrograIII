%Hallar la longitud de una lista (es decir, el número de elementos que contiene).
%contarElementos([clara,tomas,jose,isabel],Total).


contarElementos([],0).
contarElementos([Cab|Cola],Total) :- contarElementos(Cola,Aux), Total is Aux+1.