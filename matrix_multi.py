def dot_product(arrA, arrB):
    sum = 0
    for i in range(len(arrA)):
        sum += (arrA[i] * arrB[i])
    return sum

def get_column(matrix, idx=0):
    return [row[idx] for row in matrix]


def array_mult(A, B):
    new_list = list()
    for i in range(len(A)):
        row = A[i]
        inner_list = list()
        for j in range(len(B)):
            col = get_column(B, j)
            item = dot_product(row, col)
            inner_list.append(item)
        new_list.append(inner_list)
    return new_list

M1 = [[1, 2], [-2, 3], [1, 1]]
M2 = [[1,0,0],[0,1,0]]
ans = array_mult(M1, M2)

print(ans)

#print(get_column(M2, 2))

#print(dot_product([1, 2], [2, 4]))