# Python program to calculate sum of squares of first n natural nos.

num = int(input("Enter a number:"))
sum = 0
for i in range(1, num+1):
   sum += (i*i)
print("Sum is:",sum)
