estilo(greenDay,punk).
escuchoElTema(juan,tema(basketcase,greenDay)).

/*
si la persona escucho un tema de cierta banda ^ la banda es de cierto estilo => 
la persona escucho ese estilo


escuchoElTema(Persona, tema(Nombre,Banda)) ^ estilo(Banda,Estilo) => escuchoElEstilo(Persona,Estilo).
*/

escuchoElEstilo(Persona,Estilo):- escuchoElTema(Persona, tema(_,Banda)) , estilo(Banda,Estilo).