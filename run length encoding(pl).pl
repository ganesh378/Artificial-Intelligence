
% Define the predicate to perform run-length encoding
run_length_encoding([], []).
run_length_encoding([X], [[1, X]]).
run_length_encoding([X, X|Tail], [[Count, X]|Result]) :-
    run_length_encoding([X|Tail], [[NewCount, X]|Result]),
    Count is NewCount + 1.
run_length_encoding([X, Y|Tail], [[1, X]|Result]) :-
    X \= Y,
    run_length_encoding([Y|Tail], Result).


