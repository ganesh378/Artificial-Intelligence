def queen(b,r):
    if r==8:
        return True
    for i in range(8):
        if valid(b,r,i):
            b[r]=i
            if queen(b,r+1):
                return True
    return False
def valid(b,r,c):
    for i in range(r):
        if b[i]==c or abs(b[i]-c)==abs(i-r):
            return False
    return True
def board(b):
    for i in range(8):
        for j in range(8):
            if b[i]==j:
                print("q",end=" ")
            else:
                print("*",end=" ")
        print()
b=[0,0,0,0,0,0,0,0]
if queen(b,0):
    board(b)
else:
     print("no solution exist")
