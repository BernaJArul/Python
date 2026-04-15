# Python program to find whether a number is armstrong or not

n = int(input("Enter a number:"))
s = 0
temp = n
while n>0 :
   rem = n%10
   s = s+(rem*rem*rem)
   n = n//10
if(temp == s):
   print(temp,"is an armstrong number")
else:
   print(temp,"is not an armstrong number")
