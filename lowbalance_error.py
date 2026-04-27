#Python program to create a custom lowbalance error and raise if withdrawal exceeds balance

def withdraw(balance, amount):
   if amount > balance:
      raise ValueError("Insufficient balance")
   return balance - amount

# Initial balance
balance = 1000

# Attempt to withdraw an amount greater than the balance
try:
   balance = withdraw(balance, 1500)
   print("Withdrawal successful. Remaining balance:", balance)
except ValueError as e:
   print("Withdrawal failed:", e)

# Attempt to withdraw a valid amount
try:
   balance = withdraw(balance, 500)
   print("Withdrawal successful. Remaining balance:", balance)
except ValueError as e:
   print("Withdrawal failed:", e)
