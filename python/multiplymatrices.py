# Program to multiply two matrices using list comprehension

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

def multiply_matrices(matrix1, matrix2):
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*matrix2)] for X_row in matrix1]
    for r in result:
        print(r)

multiply_matrices(X, Y)