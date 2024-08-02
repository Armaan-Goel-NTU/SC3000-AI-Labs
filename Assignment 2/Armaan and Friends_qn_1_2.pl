% facts
company(appy).
company(sumsum).
smartphonetech(galactica-s3).
developed(sumsum,galactica-s3).
stole(stevey,galactica-s3).
boss(stevey,appy).
competitor(appy,sumsum).

competitor(X, Y) :- competitor(Y, X).
rival(X, Y) :- competitor(X, Y).
business(X) :- smartphonetech(X).

unethical(B) :-
    boss(B,C),
    company(C),
    stole(B,T),
    business(T),
    developed(R,T),
    rival(C,R),
    company(R).

