:-dynamic known/3.

%% -------------------------------------PREDICADOS DE LA BASE DE CONOCIMIENTO--------------------
%% ----------------------------------------------------------------------------------------------
nostrils(external_tubular).
live(at_sea).
bill(hooked).
bill(flat).
size(large).

order(tubenose) :-
  nostrils(external_tubular),
  live(at_sea),
  bill(hooked).

order(waterfowl) :-
  feet(webbed),
  bill(flat).

family(albatross) :-
  order(tubenose),
  size(large),
  wings(long_narrow).

family(swan) :-
  order(waterfowl),
  neck(long),
  color(white),
  flight(ponderous).

bird(laysan_albatross):-
 family(albatross),
 color(white).

bird(black_footed_albatross):-
 family(albatross),
 color(dark).

bird(whistling_swan) :-
 family(swan),
 voice(muffled_musical_whistle).

bird(trumpeter_swan) :-
 family(swan),
 voice(loud_trumpeting).
%% ----------------------------------------------------------------------------------------------
%% ----------------------------------------------------------------------------------------------



%% -------------------------------------PREDICADOS PARA LA SHELL DE USUARIO----------------------
%% ----------------------------------------------------------------------------------------------

ask(A, V):-
  known(yes, A, V),  % succeed if true
  !.  % stop looking

ask(A, V):-
  known(_, A, V),  % fail if false
  !,
  fail.

ask(A, V):-
  write(A:V),  % ask user
  write('? : '),
  nl,
  read(Y),  % get the answer
  asserta(known(Y, A, V)),  % remember it
  Y == yes.  % succeed or fail

flight(X):- menuask(flight, X, [ponderous, agile, flap_glide]).

menuask(A, V, MenuList) :-
  write('What is the value for '), write(A:V), write('?'), nl,
  write(MenuList), nl,
  read(X),
  check_val(X, A, V, MenuList),
  asserta( known(yes, A, X) ),
  X == V.

check_val(X, A, V, MenuList) :-
  member(X, MenuList),
  !.

check_val(X, A, V, MenuList) :-
  write(X), write(' is not a legal value, try again.'), nl,
  menuask(A, V, MenuList).

eats(X):- ask(eats, X).
feet(X):- ask(feet, X).
wings(X):- ask(wings, X).
neck(X):- ask(neck, X).
color(X):- ask(color, X).
voice(X) :- ask(voice, X).
%% ----------------------------------------------------------------------------------------------
clean :- retractall(known(_,_,_)).
