#Give a base and exponent, compute the power interger

def computerPower(base, exp):
    if exp == 0:
        return 1
    if base == 0:
        return 0
    return base * computerPower( base, exp - 1)

def optimisePow(base, n):
    return computerPower(base, n)
print(optimisePow(5, 2))