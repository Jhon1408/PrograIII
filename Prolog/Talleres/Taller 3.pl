%---------------------------------------------------%
%              Base de Conocimientos 1              %
%---------------------------------------------------%

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

abuelo_paterno(X,Y) :- padre(X,Z), padre(Z,Y) ; madre(X,Z), padre(Z,Y).
abuelo_materno(X,Y) :- padre(X,Z), madre(Z,Y) ; madre(X,Z), madre(Z,Y).

%---------------------------------------------------%
%              Base de Conocimientos 2              %
%---------------------------------------------------%

enfermo_de(manuel,gripe).
tiene_sintoma(alicia,cansancio).
tiene_sintoma(manuel,fiebre).
sintoma_de(fiebre,gripe).
sintoma_de(cansancio,anemia).
elimina(vitaminas,cansancio).
elimina(aspirina,fiebre).
elimina(jarabe,tos).

alivia(X,Y) :- elimina(X,A),sintoma_de(A,Y).
enfermode(X,Y) :- tiene_sintoma(X,Z),sintoma_de(Z,Y).
recetar_a(X,Y) :- enfermo_de(Y,A),alivia(X,A).

%---------------------------------------------------%
%             Solucion Preguntas                    %
%---------------------------------------------------%

% Consultas:
% alivia(X,gripe).
% X = aspirina.
% ¿Que alivia la gripe?
%
% alivia(X,cansancio).
% false.
% ¿Que alivia el cansancio?
% 
% alivia(X,anemia).
% X = vitaminas.
% ¿Que alivia la anemia?
%
% alivia(X,fiebre).
% false.
%
% enfermode(X,Y).
% X = alicia, Y = anemia;
% X = manuel, Y = gripe.

%---------------------------------------------------%
%              Base de Conocimientos 3              %
%---------------------------------------------------%

padece(pedro,gripe).
padece(pedro,hepatitis).
padece(juan,hepatitis).
padece(maria,gripe).
padece(carlos,intoxicacion).

es_sintoma(fiebre,gripe).
es_sintoma(cansancio,hepatitis).
es_sintoma(diarrea,intoxicacion).
es_sintoma(cansancio,gripe).

suprime(aspirina,fiebre).
suprime(lomotil,diarrea).

sintomas(X,Y) :- es_sintoma(Y,Z), padece(X,Z).
alivia_enfermedad(X,Y) :- suprime(X,Z), es_sintoma(Z,Y).
tomar(X,Y) :- padece(X,Z), alivia_enfermedad(Y,Z).

%---------------------------------------------------%
%             Solucion Preguntas                    %
%---------------------------------------------------%

% Consultas:
% padece(pedro,X). 
% padece(maria,X).
% sintomas(pedro,X).
% sintomas(X,diarrea).
% sintomas(X,cansancio).
% tomar(pedro,X).
% sintomas(X,gripe).