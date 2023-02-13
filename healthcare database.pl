patient(john, flu).
patient(jane, headache).
patient(bob, broken_arm).
diagnose(Patient, Condition) :-
    patient(Patient, Condition).
treat(Patient, NewCondition) :-
    retract(patient(Patient, _OldCondition)),
    asserta(patient(Patient, NewCondition)).

