# Python program to generate fibonacci series

n = int(input("Enter no of terms to be generated:"))
num1 = 0
num2 = 1
next_num = num2
count = 1
print (num1,num2)
while count <= n-2:
   print(next_num, end=" ")
   count += 1
   num1,num2 = num2,next_num
   next_num = num1 + num2
