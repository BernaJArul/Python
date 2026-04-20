rows = 3
columns = 3
matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
      ]

# Resultant transpose matrix initialization
transpose_matrix = [[0 for _ in range(rows)] for _ in range(columns)]
# Calculating the transpose
for i in range(rows):
   for j in range(columns):
      transpose_matrix[j][i] = matrix[i][j]
# Displaying the transpose matrix
print("\nThe transpose of the square matrix is:")
for row in transpose_matrix:
   for element in row:
      print(element, end=" ")
   print()
