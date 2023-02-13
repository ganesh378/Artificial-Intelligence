% Define the fibonacci predicate
fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(N, F) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fibonacci(N1, F1),
    fibonacci(N2, F2),
    F is F1 + F2.

% Generate the fibonacci series up to a certain number
generate_fibonacci_series(N, Result) :-
    findall(F, (between(0, N, X), fibonacci(X, F)), Result).
