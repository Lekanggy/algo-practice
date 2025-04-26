#Greatest common divisor given a/b i.e 28 / 16
#28/16 = 1 r 12 ..continue division with the remainder

def GCD(a, b):
    remainder = a % b
    if remainder == 0:
        return b
    return GCD(b, remainder)

print(GCD(28, 7))
