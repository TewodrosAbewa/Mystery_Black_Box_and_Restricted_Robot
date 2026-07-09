from list_operation import List_Operation

class Matrix_Operation:
    def __init__(self):
        self.list_oper = List_Operation()

    def matrix_multiply(self, A, B):
        row, col = len(A), len(B[0])
        self.prod = [[None for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                self.prod[i][j] = sum([
                    (A[i][k] if isinstance(A[i][k], (int, float)) else A[i][k][0]) * 
                    (B[k][j] if isinstance(B[k][j], (int, float)) else B[k][j][0]) 
                    for k in range(len(B))])
        return self.prod
    

    def matrix_copy(self, input):
        row, col = len(input), len(input[0])
        copy = [[None for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                copy[i][j] = input[i][j]
        return copy
    

    def make_diago_elem_one(self, matrix_A):
        for i in range(len(matrix_A)):
            matrix_A[i] = self.list_oper.multiply_by_constant(matrix_A[i], 1/(matrix_A[i][i]))
            new_matrix = self.matrix_copy(matrix_A)
        return new_matrix
    def matrix_transpose(self, matrix_A):
        row, col = len(matrix_A), len(matrix_A[0])
        mat_trans = [[None for _ in range(row)] for _ in range(col)]
        for i in range(col):
            for j in range(row):
                mat_trans[i][j] = matrix_A[j][i]
        return mat_trans


