def square_no(n):
   squares = [x**2 for x in range(1,n+1)]
   return squares

n = int(input("Enter the number:"))
squares_list = square_no(n)
print("List of squares:",squares_list)
