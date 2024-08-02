% facts
monarch(elizabeth).

son(elizabeth, charles, 1).
son(elizabeth, andrew, 3).
son(elizabeth, edward, 4).
daughter(elizabeth, ann, 2).

succession(M) :-
    % must be a monarch
    monarch(M),

    % find all offsprings (setof will sort them by default)
    setof(BirthOrder-Child, (son(M, Child, BirthOrder); daughter(M, Child, BirthOrder)), SuccessionLine),

    print_list(SuccessionLine).

% helper function to print the list without the birth order 
print_list([]).
print_list([BirthOrder-Child|Tail]) :-
    writeln(Child),
    print_list(Tail).
