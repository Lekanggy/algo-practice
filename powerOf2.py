#this sia special optimaization algortihm called the tail-called optimisation
# base case: when n is 0 return product which is 1 i.e 2^0 = 1


def powerOf2Optimisation(product, n):
    if n == 0:
        return product
    return powerOf2Optimisation(2 * product, n - 1)

def powerOf2(n):
    return powerOf2Optimisation(1, n)

print(powerOf2(6))


