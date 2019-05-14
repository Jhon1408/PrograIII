client('A.Jones').
client('W.Metesk').

book_overdue('C.Watzer', book10098).
book_overdue('A.Jones',book29907).

basic_facility(reference_library).
basic_facility(enquiries_desk).

additional_facility(borrowing_book).
additional_facility(inter_library_loan).

general_facility(X) :- basic_facility(X).
general_facility(X) :- additional_facility(X).

facility(Pers,Fac) :-
  book_overdue(Pers,Book),
  !,
  basic_facility(Fac).

facility(Pers,Fac) :- general_facility(Fac).