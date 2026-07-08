
from matrix_operation import Matrix_Operation
from list_operation import List_Operation
class BLACK_BOX:
    def __init__(self, input, output):
        self.input = input
        self.output = output
        self.matrix_operator = Matrix_Operation()
        self.list_operator = List_Operation()
    def gaussian_matr_builder(self):
        col_output = len(self.output[0])
        row_input = len(self.input)
        col_input = len(self.input[0])

        self.all_equa = []
        for i in range(col_output):                                       
            curr_matr = self.matrix_operator.matrix_copy(self.input)
            for j in range(row_input):
                curr_matr[j].insert(col_input, self.output[j][i])
            
            self.all_equa.append(curr_matr)
        return self.all_equa
    
    def gauss_elim(self, argument_matrix):
        row = len(argument_matrix)
        for i in range(row):
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
        # reduced_row_echelon_matr = self.matrix_operator.make_diago_elem_one(argument_matrix)
        return argument_matrix #reduced_row_echelon_matr
    def final_solution_builder(self):
        arguments = self.gaussian_matr_builder()
        row, col = len(arguments[0]), len(arguments)
        self.solutions = [[None for _ in range(col)] for _ in range(row)]
        for i in range(col):
            elimi_matr = self.gauss_elim(arguments[i])
            for j in range(len(elimi_matr)):
                self.solutions[j][i] = elimi_matr[j][-1]
        return self.solutions
    def transform(self, new_input):
        self.new_output = self.matrix_operator.matrix_multiply(new_input, self.final_solution_builder())
        return self.new_output
    