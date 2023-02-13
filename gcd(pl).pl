gcd(X,X,X).
gcd(X,Y,D):-X>Y,R is X mod Y,gcd(Y,R,D).
gcd(X,Y,D):-X<Y,gcd(Y,X,D).
