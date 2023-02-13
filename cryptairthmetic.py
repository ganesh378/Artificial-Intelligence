def solve(equation):
    letters = set(equation)
    letters.discard('+')
    letters.discard('=')
    letters.discard(' ')
    for num in range(10):
        for letter in letters:
            exec(f"{letter} = {num}")
        if eval(equation):
            return True
    return False

equation = "SEND + MORE = MONEY"
equation = equation.replace(" ", "")
letters = list(set(equation))
for letter in letters:
    equation = equation.replace(letter, f"{ord(letter) - ord('A')}")
print(solve(equation))
