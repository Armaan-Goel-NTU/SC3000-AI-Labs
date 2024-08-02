% facts
monarch(elizabeth).

son(elizabeth, charles).
son(elizabeth, andrew).
son(elizabeth, edward).
daughter(elizabeth, ann).

% list all the sons first then daughters
succession_old(M, C) :-
    son(M, C); daughter(M, C).

offspring(elizabeth, charles).
offspring(elizabeth, ann).
offspring(elizabeth, andrew).
offspring(elizabeth, edward).

male(charles).
male(andrew).
male(edward).
female(ann).

% list all the children
succession_new(M, C) :-
    offspring(M, C).