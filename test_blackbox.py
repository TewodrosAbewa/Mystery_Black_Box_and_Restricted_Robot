from Black_Box import BLACK_BOX

input = [[1, 2], [3, 4]]
output = [[5, 6], [7, 8]]
B_Box = BLACK_BOX(input, output)
solu = B_Box.final_solution_builder()
print(solu)

print(B_Box.transform([input]))
