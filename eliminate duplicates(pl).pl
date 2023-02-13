% Define the predicate to eliminate duplicates
eliminate_duplicates([], []).
eliminate_duplicates([X], [X]).
eliminate_duplicates([X, X|Tail], Result) :-
    eliminate_duplicates([X|Tail], Result).
eliminate_duplicates([X, Y|Tail], [X|Result]) :-
    X \= Y,
    eliminate_duplicates([Y|Tail], Result).


