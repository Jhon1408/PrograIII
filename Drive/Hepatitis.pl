causa_de(hepatitis,virus_de_hepatitis_a).
causa_de(hepatitis,virus_de_hepatitis_b).
causa_de(hepatitis,virus_de_hepatitis_c).
causa_de(hepatitis,virus_de_hepatitis_d).
causa_de(hepatitis,virus_de_hepatitis_e).
causa_de(hepatitis,epstein_barr).
causa_de(hepatitis,cmv).
causa_de(hepatitis,herpes_virus_6).
causa_de(hepatitis,influenza).
causa_de(hepatitis,ebola).
causa_de(hepatitis,marbug).

causa_de(hepatitis,paracetamol).
causa_de(hepatitis,isoniazida).
causa_de(hepatitis,nitrofurantoina).
causa_de(hepatitis,tetraciclina).
causa_de(hepatitis,ciprofloxacina).
causa_de(hepatitis,eritomicina).
causa_de(hepatitis,amoxicilina).
causa_de(hepatitis,acido_clavulanico).
causa_de(hepatitis,acido_valproico).
causa_de(hepatitis,halotano).
causa_de(hepatitis,sales_de_oro).
causa_de(hepatitis,propiltiouracilo).
causa_de(hepatitis,diclofenaco).
causa_de(hepatitis,sulfa).


causa_de(hepatitis,hongos).
causa_de(hepatitis,solventes_organicos).
causa_de(hepatitis,hierbas_medicinales).
causa_de(hepatitis,valerianas).
causa_de(hepatitis,cianobaterias).
causa_de(hepatitis,bacillus_cereus).


causa_de(hepatitis,higado_graso_agudo_del_embarazo).
causa_de(hepatitis,sindrome_helpp).
causa_de(hepatitis,hepatitis_autoinmune).
causa_de(hepatitis,budd_chiari).
causa_de(hepatitis,leucemia).
causa_de(hepatitis,linfoma).
causa_de(hepatitis,tuberculosis).
causa_de(hepatitis,sindrome_de_reye).

sintoma_de(hepatitis,confusion).
sintoma_de(hepatitis,cambio_humor).

sintoma_de(hepatitis,somnoliento).
sintoma_de(hepatitis,desorientado).
sintoma_de(hepatitis,comportamiento_inadecuado).

sintoma_de(hepatitis,estuporoso).
sintoma_de(hepatitis,aletargado).
sintoma_de(hepatitis,comatoso).
sintoma_de(hepatitis,coma_profundo).



tratamiento(hepatitis,dieta).
tratamiento(hepatitis,lactulosa).
tratamiento(hepatitis,lactosa_o_lactitol).
tratamiento(hepatitis,benzoato_de_sodio).
tratamiento(hepatitis,aspartato_de_ornitina).
tratamiento(hepatitis,n-acetilcisteina).
tratamiento(hepatitis,neomicina).
tratamiento(hepatitis,metronidazol ).
tratamiento(hepatitis,rifaximina).
tratamiento(hepatitis,flumazenil).
tratamiento(hepatitis,bromocriptina). 
  
diagnostico(X,Y,Z):-
    sintoma_de(H,N), causa_de(H,M),
    ((  Y == N ) ->  ( Z == M ) ->  
    (   tratamiento(H,P), write("es posible que el paciente "), write(X), 
    write(" tenga "), write(H), write(" a causa de "), write(M), 
    write(" tratar con "), write(P), nl)).
diagnostico(_,Y,Z):-
    sintoma_de(H,N), causa_de(H,M),
    ((  Y \= N ) -> ( Z == M )  ->  write("el paciente "), write(" probablemtente no tenga "), write(H)).
diagnostico(_,Y,Z):-
    sintoma_de(H,N), causa_de(H,M),
    ((  Y == N ) -> (  Z \= M ) ->  write("el paciente "), write(" probablemtente no tenga "), write(H)).
diagnostico(_,Y,Z):-
    sintoma_de(H,N), causa_de(H,M),
    ((  Y \= N ) -> (  Z \= M ) ->  write("el paciente "), write(" probablemtente no tenga "), write(H)).
pregunta:-
    write("escriba el nombre del paciente: "), nl, read(X), nl, write(" escriba uno de sus sintomas: "),
    read(Y), nl, write(" y escriba una posible causa: "), nl,  read(Z), diagnostico(X,Y,Z).