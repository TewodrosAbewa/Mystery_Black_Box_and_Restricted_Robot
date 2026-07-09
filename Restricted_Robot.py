from Black_Box import BLACK_BOX
from matrix_operation import Matrix_Operation
from list_operation import List_Operation
class Robot:
    def __init__(self, rules):
        self.mat_oper = Matrix_Operation()
        self.list_oper = List_Operation()

        self.rules = rules
        
    def find_constants(self, target_position):
        self.target_position = self.mat_oper.matrix_transpose(target_position)
        constant_finder = BLACK_BOX(self.mat_oper.matrix_transpose(self.rules), self.target_position) # I need transpose operation that enables to me transpose rules and target position
        self.constants = constant_finder.final_solution_builder()

        self.constants =  [self.constants[i][0] for i in range(len(self.constants))]
        for i in range(len(self.constants)):
            if float(self.constants[i]).is_integer():
                self.constants[i] = int(self.constants[i])
        return self.constants
    
    def movement_generator(self, target_position):
        constants = self.find_constants(target_position)
        self.movement = [[0 for i in target_position]]
        for i in range(len(self.rules)): # 0, 1, 2
            if i == 0:
                current = self.list_oper.generate_sequence_list(self.rules[i], constants[i])
            else:
                current = [self.list_oper.element_wise_addition(self.list_oper.generate_sequence_list(self.rules[i], constants[i])[k], self.movement[-1]) for k in range(constants[i])]

            self.movement.append(j for j in current) # [[a], [2a], [3c], [3c+1d], [3c+2d], [3c+3d]]
        fir_mov = 0
        for k in range(len(self.movement)):
            if k==len(self.movement) - 1:
                break
            print(f"I am Robot_X and 'm going from {self.movement[fir_mov]} to ->{self.movement[fir_mov+1]}")
            fir_mov = k+1

        return self.movement
