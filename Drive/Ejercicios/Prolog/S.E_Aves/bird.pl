voice(muffled_musical_whistle).
voice(loud_trumpeting).

nostrils(external_tubular).
live(at_sea).
bill(hooked).
size(large).
flight(ponderous).

ask(Attr, Val):-
  write(Attr:Val),
  write('? '),
  nl,
  read(yes).

eats(X):- ask(eats, X).
feet(X):- ask(feet, X).
wings(X):- ask(wings, X).
neck(X):- ask(neck, X).
color(X):- ask(color, X).

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
