%---------------------------------------------------%
%              Base de Conocimientos                %
%---------------------------------------------------%
hombre(jose).
hombre(tomas).
hombre(jaime).
mujer(clara).
mujer(isabel).
mujer(ana).
mujer(patricia).

progenitor(clara, jose).
progenitor(tomas, jose).
progenitor(tomas, isabel).
progenitor(jose, ana).
progenitor(jose, patricia).
progenitor(patricia, jaime).

hijo(X,Y) :- progenitor(Y,X), hombre(X).
hija(X,Y) :- progenitor(Y,X), mujer(X).

abuelo(X,Y) :- progenitor(X,Z), progenitor(Z,Y).
bisabuelo(X,Y) :- abuelo(X,Z), progenitor(Z,Y).
%---------------------------------------------------%
%               Respuestas Taller 2                 %
%---------------------------------------------------%

% Dada la base de conocimiento de la anterior figura, 
% se pide el enunciado verbal de las siguientes preguntas.
% a. progenitor(jaime,X).
% ¿Quienes son los hijos de Jaime?
% b. progenitor(X,jaime).
% ¿Quienes son los padres de Jaime?
% c. progenitor(clara,X) , progenitor(X,patricia).
% ¿Quien es el hijo de Clara y padre de Patricia?

% Dada la base de conocimiento de la anterior figura 
% formula en PROLOG las siguientes preguntas:

% a. ¿Tiene Isabel un hijo o una hija?
% hijo(X, isabel).
% hija(X, isabel).
% b. ¿Quién es el progenitor de Patricia?
% progenitor(X, patricia).
% hija(patricia, X).
% c. Encuentre los abuelos de patricia.
% abuelos(X, patricia).
% d. Encuentre los bisabuelos de Jaime.
% bisabuelos(X, jaime).