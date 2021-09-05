# Program to transpose a matrix using a nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

def transpose_matrix(matrix):
    # iterate through rows
    for i in range(len(matrix)):
       # iterate through columns
       for j in range(len(matrix[0])):
           result[j][i] = matrix[i][j]
    for r in result:
        print(r)

transpose_matrix(X)