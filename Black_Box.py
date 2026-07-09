
from matrix_operation import Matrix_Operation
from list_operation import List_Operation
class BLACK_BOX:                                     # INPUT form                          OUTPUT form
    def __init__(self, input, output):              # [[u11, u12, u13, ..., u1n],      [[v11, v12, v13, ..., v1n],
        self.input = input                          #  [u21, u22, u23, ..., u2n],       [v21, v22, v23, ..., v2n],
        self.output = output                        #           .                                  .
        self.matrix_operator = Matrix_Operation()   #           .                                  .
        self.list_operator = List_Operation()       #  [um1, um2, um3, ..., umn]]        [vm1, vm2, vm3, ..., vmn]]
    def gaussian_matr_builder(self):
        col_output = len(self.output[0]) # n
        row_input = len(self.input)      # m
        col_input = len(self.input[0])   # n

        self.all_equa = []
        for i in range(col_output): # (0, n-1)                                      
            curr_matr = self.matrix_operator.matrix_copy(self.input)  
            for j in range(row_input):  # (0, m)
                curr_matr[j].insert(col_input, self.output[j][i])
            
            self.all_equa.append(curr_matr)
        return self.all_equa
    
    def gauss_elim(self, argument_matrix):
        row = len(argument_matrix)  # this equal to number of row input m
        for i in range(row): # (0, m)
            t = self.list_operator.first_non_zero_index(argument_matrix[i])
            for j in range(i+1, row):
                if argument_matrix[j][t] !=0:
                    argument_matrix[j] = self.list_operator.multiply_by_constant(argument_matrix[j], argument_matrix[i][t]/argument_matrix[j][t])
                    argument_matrix[j] = self.list_operator.element_wise_substraction(argument_matrix[i], argument_matrix[j])
                
        row = len(argument_matrix)
        for i in range(row)[::-1]: # 3, 2, 1, 0
            t = self.list_operator.first_non_zero_index(argument_matrix[i])
            for j in range(i)[::-1]: #2, 1, 0
                if argument_matrix[j][t] !=0:
                    argument_matrix[j] = self.list_operator.multiply_by_constant(argument_matrix[j], argument_matrix[i][t]/argument_matrix[j][t])
                    argument_matrix[j] = self.list_operator.element_wise_substraction(argument_matrix[i], argument_matrix[j])
        reduced_row_echelon_matr = self.matrix_operator.make_diago_elem_one(argument_matrix)
        return reduced_row_echelon_matr # argument_matrix
    def final_solution_builder(self):
        self.arguments = self.gaussian_matr_builder()
        row, col = len(self.arguments[0]), len(self.arguments) # 
        self.solutions = [[None for _ in range(col)] for _ in range(row)]
        for i in range(col): # 
            elimi_matr = self.gauss_elim(self.arguments[i])
            for j in range(len(elimi_matr)):
                self.solutions[j][i] = elimi_matr[j][-1]
        return self.solutions
    def transform(self, new_input):
        transform_matr = self.final_solution_builder()
        self.new_output = self.matrix_operator.matrix_multiply(new_input, transform_matr)
        return self.new_output
    