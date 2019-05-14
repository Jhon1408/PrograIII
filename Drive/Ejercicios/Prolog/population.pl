population(usa,203).
population(india,548).
population(china,800).
population(brazil,108).

area(usa,3).
area(india,1).
area(china,4).
area(brazil,3).

/*
The population density of country X is Y, if:
The population of X is P, and
The area of X is A, and
Y is calculated by dividing P by A
*/

density(Country, Y) :-
population(Country,Population),
area(Country,Area),
Y is Population/Area.


%Existe algun país que tenga un area entre LimitInf y LimitSup
range_area(LimitInf, LimitSup):- area(_,Area),Area >= LimitInf, Area =< LimitSup.

%Cual es el país que tiene un área entre los límites LimitInf y LimitSup
range_area(Country, LimitInf, LimitSup):- area(Country,Area),Area >= LimitInf, Area =< LimitSup.


%Existe un país que tenga un rango de población entre LimitInf y LimitSup
range_population(LimitInf, LimitSup) :- population(_,Population), Population >= LimitInf, Population =< LimitSup.

%Cuál es el país que tiene un rango de población entre los límites LimitInf y LimitSup
range_population(Country, LimitInf, LimitSup) :- population(Country,Population), Population >= LimitInf, Population =< LimitSup.


%Cree una regla que me permita consultar el país que tenga un rango de area entre los límites (LimitInf y LimitSup) y un rango poplacional entre los límites (LimitInf, LimitSup) 
%determinado por limites de la consulta
consult_ranges_and_country(Country, LimitInfArea, LimitSupArea, LimitInfPopulation, LimitSupPopulation):- 
area(Country,Area),population(Country,Population),Area >= LimitInfArea, Area =< LimitSupArea,
Population >= LimitInfPopulation, Population =< LimitSupPopulation.