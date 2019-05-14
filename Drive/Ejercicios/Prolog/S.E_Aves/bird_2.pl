:-dynamic known/3.

nostrils(external_tubular).
live(at_sea).
bill(hooked).
bill(flat).
size(large).
flight(ponderous).

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


eats(X):- ask(eats, X).
feet(X):- ask(feet, X).
wings(X):- ask(wings, X).
neck(X):- ask(neck, X).
color(X):- ask(color, X).
voice(X) :- ask(voice, X).

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

clean :- retractall(known(_,_,_)).
