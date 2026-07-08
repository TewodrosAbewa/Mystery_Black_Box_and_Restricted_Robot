class List_Operation:
    def __init__(self):
        pass
    def element_wise_substraction(self, list_A, list_B):
        subs = [list_A[i] - list_B[i] for i in range(len(list_A))]
        return subs

    def element_wise_addition(self, list_A, list_B):
        subs = [list_A[i] + list_B[i] for i in range(len(list_A))]
        return subs

    def multiply_by_constant(self, list_A, K):
        return [K*list_A[i] for i in range(len(list_A))]

    def first_non_zero_index(self, list_A):
        for i in range(len(list_A)):
            if list_A[i] !=0:
                
                break
        return i
    
    def list_copy(self, list_):
       new_list = [None for _ in list_]
       for i in range(len(list_)):
           new_list[i] = list_[i] 
       return new_list
    
    def generate_sequence_list(self, row, k_times): # for example list_A = [2, 3, -1], k_times = 3, then
        copy_row = self.list_copy(row)                #             new_list = [ 1*[2, 3, -1],
        new_list = []
        try:                                     #                      2*[2 , 3, -1]
            for i in range(1, k_times+1):                    #                       3* [2, 3, -1]]
                copy_row = self.multiply_by_constant(row, i)
                new_list.append(copy_row)
        except:
            print("Some of constants are not INTEGER")
        return new_list
    
    