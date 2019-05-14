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
sintoma(confusion).
sintoma(cambio_humor).

sintoma(somnoliento).
sintoma(desorientado).
sintoma(comportamiento_inadecuado).

sintoma(estuporoso).
sintoma(aletargado).
sintoma(comatoso).
sintoma(coma_profundo).
%----------------------------------------------------%
%                      Tratamiento                   %
%----------------------------------------------------%
tratamiento(confusion,bromocriptina).
tratamiento(cambio_humor,olanzapina).
tratamiento(somnoliento,flumazenil).
tratamiento(desorientado,n-acetilcisteina).
tratamiento(comportamiento_inadecuado,metilfenidato).
tratamiento(estuporoso,neomicina).
tratamiento(aletargado,flumazenil).
tratamiento(comatoso,no_disponible).
tratamiento(coma_profundo,no_disponible).
tratamiento(irritacion_intestinal,rifaximina).
tratamiento(infecciones,metronidazol).
tratamiento(hepatitis,dieta).
tratamiento(hepatitis,aspartato_de_ornitina).
tratamiento(hepatitis,benzoato_de_sodio).
tratamiento(hepatitis,lactosa_o_lactitol).
%----------------------------------------------------%
%                        Ordenes                     %
%----------------------------------------------------%
diagnostico(P, D, T, E, I) :- 
    write("Que sintoma presenta: "), nl, read(S),
    (((sintoma(S), droga(D)) -> tieneHepatitis());
    ((sintoma(S), toxina(T)) -> tieneHepatitis());
    ((sintoma(S), enfermedad(E)) -> tieneHepatitis());
    ((sintoma(S), infeccion(I)) -> tieneHepatitis());
    ((sintoma(S) -> notieneHepatitis()));
    ((write("El paciente "), write(P), write(" esta sano, o sus sintomas no estan precentes en el sistema.")), nl)).

tieneHepatitis():- write("El paciente puede tener hepatitis."), nl.
notieneHepatitis():- write("El paciente no tiene hepatitis."), nl.

pregunta :- write("Nombre del paciente: "), nl, 
    read(P), write("¿Consume alguna droga?: "), nl,
    read(D), write("¿Consume alguna toxina?: "), nl, 
    read(T), write("¿Padece alguna enfermendad?: "), nl, 
    read(E), write("¿Tiene alguna infeccion?: "), nl, 
    read(I), diagnostico(P, D, T, E, I).