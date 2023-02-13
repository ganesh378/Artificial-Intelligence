% Define the truth values for True and False
true.
false :- fail.

% Define a predicate to evaluate logical expressions
% using the ";", "," and "not" predicates.
eval(Expression, true) :- Expression.
eval(Expression, false) :- not(Expression).
eval((A,B), true) :- eval(A, true), eval(B, true).
eval((A,B), false) :- eval(A, false); eval(B, false).
eval((A;B), true) :- eval(A, true); eval(B, true).
eval((A;B), false) :- eval(A, false), eval(B, false).

% Define a predicate to generate a truth table for a given logical expression
truth_table(Expression) :-
    write('A      B      Result'), nl,
    write('------------------------'), nl,
    eval(Expression, true), write('true  '),
    eval(Expression, false), write('false '), nl.
