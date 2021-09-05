# Program to add and subtract two matrices using list comprehension

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

def add_matrices(matrix1, matrix2):
    result = [[matrix1[i][j] + matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    for r in result:
        print(r)

def subtract_matrices(matrix1, matrix2):
    result = [[matrix1[i][j] + matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    for r in result:
        print(r)

add_matrices(X, Y)