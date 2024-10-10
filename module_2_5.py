def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        matrix.append(row)
        for j in range(m):
             row.append(value)
    return matrix
result1 = get_matrix(2,2,10)
print(result1)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result2)
print(result3)
result4 = get_matrix(0,0,0)
print(result4)
result5 = get_matrix(-1,-2,-1)
print(result5)