reigns(rhodri, 844, 878).
reigns(anarawd, 878, 916).
reigns(hywel_dda, 916,950).
reigns(lago_ap_idwal, 950, 979).
reigns(hywel_ap_ieauf, 979, 985).
reigns(cadwallon, 985, 986).
reigns(mareduud, 986, 999).

/*
We want to ask who was on the Welsh throne during a particular year
X was a prince during year Y if:
	X reigned between years A and B, and
	Y is between A and B, inclusive


prince(cadwallon, 985).
prince(X,900).

nodebug. commando for exit

*/


was_a_prince_in(X,Y) :- reigns(X,A,B), Y>=A, Y=<B.