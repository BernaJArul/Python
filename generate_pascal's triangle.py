# Python program to generate a 2D list of Pascal's triangle upto n rows

n = int(input("Enter a number:"))
for i in range(n):
   print(' '*(n-i), end='')
   coef = 1
   for j in range(0, i + 1):
      print(coef, end=' ')
      coef = coef * (i - j) // (j + 1)
   print()
