# Uisng a new optimiser of O(logn) operations

def isEeven(n):
    if n % 2 == 0:
        return True
    return False

def square(n):
    return n * n

def powerLognOperation(n):
    if n == 0:
        return 1
    if isEeven(n):
        return square(powerLognOperation(n/2))
    else:
        return 2 * powerLognOperation(n - 1)
    

print(powerLognOperation(4))