%----------------------------------------------------%
%                   Infecciones                      %
%----------------------------------------------------%
infeccion(virus_de_hepatitis_a).
infeccion(virus_de_hepatitis_b).
infeccion(virus_de_hepatitis_c).
infeccion(virus_de_hepatitis_d).
infeccion(virus_de_hepatitis_e).
infeccion(epstein_barr).
infeccion(cmv).
infeccion(herpes_virus_6).
infeccion(influenza).
infeccion(ebola).
infeccion(marbug).
%----------------------------------------------------%
%                      Drogas                        %
%----------------------------------------------------%
droga(paracetamol).
droga(isoniazida).
droga(nitrofurantoina).
droga(tetraciclina).
droga(ciprofloxacina).
droga(eritomicina).
droga(amoxicilina).
droga(acido_clavulanico).
droga(acido_valproico).
droga(halotano).
droga(sales_de_oro).
droga(propiltiouracilo).
droga(diclofenaco).
droga(sulfa).
%----------------------------------------------------%
%                      Toxinas                       %
%----------------------------------------------------%
toxina(hongos).
toxina(solventes_organicos).
toxina(hierbas_medicinales).
toxina(valerianas).
toxina(cianobaterias).
toxina(bacillus_cereus).
%----------------------------------------------------%
%                    Enfermedades                    %
%----------------------------------------------------%
enfermedad(higado_graso_agudo_del_embarazo).
enfermedad(sindrome_helpp).
enfermedad(hepatitis_autoinmune).
enfermedad(budd_chiari).
enfermedad(leucemia).
enfermedad(linfoma).
enfermedad(tuberculosis).
enfermedad(sindrome_de_reye).
%----------------------------------------------------%
%                      Sintomas                      %
%----------------------------------------------------%
%                  X es sintoma de Y                 %
%----------------------------------------------------%
sintoma(aletargado, virus_de_hepatitis_a).
sintoma(aletargado, virus_de_hepatitis_b).
sintoma(aletargado, virus_de_hepatitis_c).
sintoma(aletargado, virus_de_hepatitis_d).
sintoma(aletargado, virus_de_hepatitis_e).
sintoma(aletargado, epstein_barr).
sintoma(aletargado, cmv).
sintoma(aletargado, herpes_virus_6).
sintoma(aletargado, influenza).
sintoma(aletargado, ebola).
sintoma(aletargado, marbug).

sintoma(desorientado, virus_de_hepatitis_a).
sintoma(desorientado, virus_de_hepatitis_b).
sintoma(desorientado, virus_de_hepatitis_c).
sintoma(desorientado, virus_de_hepatitis_d).
sintoma(desorientado, virus_de_hepatitis_e).
sintoma(desorientado, epstein_barr).
sintoma(desorientado, cmv).
sintoma(desorientado, herpes_virus_6).
sintoma(desorientado, influenza).
sintoma(desorientado, ebola).
sintoma(desorientado, marbug).

sintoma(cambio_humor, hongos).
sintoma(cambio_humor, solventes_organicos).
sintoma(cambio_humor, hierbas_medicinales).
sintoma(cambio_humor, valerianas).
sintoma(cambio_humor, cianobaterias).
sintoma(cambio_humor, bacillus_cereus).

sintoma(confusion, hongos).
sintoma(confusion, solventes_organicos).
sintoma(confusion, hierbas_medicinales).
sintoma(confusion, valerianas).
sintoma(confusion, cianobaterias).
sintoma(confusion, bacillus_cereus).

sintoma(somnoliento, hongos).
sintoma(somnoliento, solventes_organicos).
sintoma(somnoliento, hierbas_medicinales).
sintoma(somnoliento, valerianas).
sintoma(somnoliento, cianobaterias).
sintoma(somnoliento, bacillus_cereus).

sintoma(comportamiento_inadecuado, higado_graso_agudo_del_embarazo).
sintoma(comportamiento_inadecuado, sindrome_helpp).
sintoma(comportamiento_inadecuado, hepatitis_autoinmune).
sintoma(comportamiento_inadecuado, budd_chiari).
sintoma(comportamiento_inadecuado, leucemia).
sintoma(comportamiento_inadecuado, linfoma).
sintoma(comportamiento_inadecuado, tuberculosis).
sintoma(comportamiento_inadecuado, sindrome_de_reye).

sintoma(comatoso, higado_graso_agudo_del_embarazo).
sintoma(comatoso, sindrome_helpp).
sintoma(comatoso, hepatitis_autoinmune).
sintoma(comatoso, budd_chiari).
sintoma(comatoso, leucemia).
sintoma(comatoso, linfoma).
sintoma(comatoso, tuberculosis).
sintoma(comatoso, sindrome_de_reye).

sintoma(coma_profundo, higado_graso_agudo_del_embarazo).
sintoma(coma_profundo, sindrome_helpp).
sintoma(coma_profundo, hepatitis_autoinmune).
sintoma(coma_profundo, budd_chiari).
sintoma(coma_profundo, leucemia).
sintoma(coma_profundo, linfoma).
sintoma(coma_profundo, tuberculosis).
sintoma(coma_profundo, sindrome_de_reye).

sintoma(estuporoso, paracetamol).
sintoma(estuporoso, isoniazida).
sintoma(estuporoso, nitrofurantoina).
sintoma(estuporoso, tetraciclina).
sintoma(estuporoso, ciprofloxacina).
sintoma(estuporoso, eritomicina).
sintoma(estuporoso, amoxicilina).
sintoma(estuporoso, acido_clavulanico).
sintoma(estuporoso, acido_valproico).
sintoma(estuporoso, halotano).
sintoma(estuporoso, sales_de_oro).
sintoma(estuporoso, propiltiouracilo).
sintoma(estuporoso, diclofenaco).
sintoma(estuporoso, sulfa).

sintoma(comportamiento_inadecuado, paracetamol).
sintoma(comportamiento_inadecuado, isoniazida).
sintoma(comportamiento_inadecuado, nitrofurantoina).
sintoma(comportamiento_inadecuado, tetraciclina).
sintoma(comportamiento_inadecuado, ciprofloxacina).
sintoma(comportamiento_inadecuado, eritomicina).
sintoma(comportamiento_inadecuado, amoxicilina).
sintoma(comportamiento_inadecuado, acido_clavulanico).
sintoma(comportamiento_inadecuado, acido_valproico).
sintoma(comportamiento_inadecuado, halotano).
sintoma(comportamiento_inadecuado, sales_de_oro).
sintoma(comportamiento_inadecuado, propiltiouracilo).
sintoma(comportamiento_inadecuado, diclofenaco).
sintoma(comportamiento_inadecuado, sulfa).
%----------------------------------------------------%
%                      Tratamiento                   %
%----------------------------------------------------%
tratamiento(confusion,bromocriptina).
tratamiento(cambio_humor,olanzapina).
tratamiento(somnoliento,flumazenil).
tratamiento(aletargado,flumazenil).
tratamiento(desorientado,n-acetilcisteina).
tratamiento(comportamiento_inadecuado,metilfenidato).
tratamiento(estuporoso,neomicina).
tratamiento(comatoso,hospitalizacion).
tratamiento(coma_profundo,hospitalizacion).
tratamiento(irritacion_intestinal,rifaximina).
tratamiento(infecciones,metronidazol).
tratamiento(hepatitis,[dieta, aspartato_de_ornitina, benzoato_de_sodio, lactosa_o_lactitol]).
%----------------------------------------------------%
%                        Ordenes                     %
%----------------------------------------------------%
tratar(X,Y) :- sintoma(Z,X), tratamiento(Z,Y).

un_sintoma(X) :- 
    write("Escriba el sintoma: "), nl, read(Y), nl, tratamiento(Y,W),
    write("El paciente "), write(X), write(" puede tener algo, pero no es grave."), nl, write("Tratar los sintomas con: "), write(W), nl; write("El sintoma no esta en la base de datos."), nl.

dos_sintomas(X) :- 
    write("Escriba el sintoma #1: "), nl, read(S1),
    write("Escriba el sintoma #2: "), nl, read(S2), sintoma(S1,Y), sintoma(S2,Z), (((Y == Z),
    write("El paciente "), write(X), write(" puede tener: "), write(Y), nl,
    write("Tratar los sintomas con: "), tratar(Y,W), write(W), nl,
    write("El paciente tambien puede tener hepatitis."), nl,
    write("Para tratar la hepatitis se sugiere tomar: "), tratamiento(hepatitis,D), write(D));
    write("El paciente no precenta enfermedad grave. "), nl, 
    write("Para el sintoma de "), write(S1), write(" tratar con: "), tratamiento(S1,H), write(H), nl,
    write("Para el sintoma de "), write(S2), write(" tratar con: "), tratamiento(S1,H), write(H)).

pregunta :- 
    write("Escriba el nombre del paciente: "), nl, read(X), nl, 
    write("Escoja de uno a dos sintomas: "), nl, read(Y), nl, 
    ((Y == 1), un_sintoma(X); (Y == 2), dos_sintomas(X); write("El numero escogido para "), write(X), write(" es invalido. "), nl).