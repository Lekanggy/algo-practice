#Algo for factorial
# 1. Start algo
# 2. Read Input from user.
# 3.Initalize the result by 1
# 4.Repeat the above until n become 1.
#     a. Multiply n by the result.
#     b. Decrease n by 1 until it becomes 0.

def factoria(n):
    result = 1
    if n == 0:
        return result
    for i in range(1, n + 1):
        # print(i)
        result *= i
    return result

print(factoria(4))