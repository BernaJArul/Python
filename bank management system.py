#BANK MANAGEMENT SYSTEM

import datetime

def create_account(accounts, account_number, name, amount, account_type, contact):
    if account_number in accounts:
        print("Account number already exists.")
    else:
        accounts[account_number] = {
            "name": name,
            "balance": amount,
            "account_type": account_type,
            "contact": contact,
            "transactions": []
        }
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        accounts[account_number]["transactions"].append(f"{timestamp}: Account created with balance {amount}")
        print("Account created successfully.")

def get_account(accounts, account_number):
    if account_number not in accounts:
        print("Account number not found.")
        return None
    else:
        return accounts[account_number]

def deposit(account, amount):
    if amount <= 0:
        print("Invalid amount. Deposit amount must be greater than zero.")
    else:
        account["balance"] += amount
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        account["transactions"].append(f"{timestamp}: Deposited {amount}")
        print(f"Deposit successful. New balance: {account['balance']}")

def withdraw(account, amount):
    if amount <= 0:
        print("Invalid amount. Withdrawal amount must be greater than zero.")
    elif account["balance"] < amount:
        print("Insufficient balance for this withdrawal.")
    else:
        account["balance"] -= amount
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        account["transactions"].append(f"{timestamp}: Withdrew {amount}")
        print(f"Withdrawal successful. Remaining balance: {account['balance']}")

def check_balance(account):
    print(f"Account balance: {account['balance']}")

def display(account):
    print("*" * 70)
    print(f"Account Holder Name : {account['name']}")
    print(f"Account Type        : {account['account_type']}")
    print(f"Contact Number      : {account['contact']}")
    print(f"Account Balance     : {account['balance']}")
    print("Transaction History :")
    if account["transactions"]:
        for transaction in account["transactions"]:
            print(f"  - {transaction}")
    else:
        print("  No transactions yet.")
    print("*" * 70)

def main():
    accounts = {}
    while True:
        print("\nBank Management System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Display Account Details")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter new account number: ")
            name = input("Enter account holder's name: ")
            account_type = input("Enter account type (Savings/Checking): ")
            contact = input("Enter contact number: ")
            try:
                amount = float(input("Enter initial deposit amount: "))
                if amount < 0:
                    raise ValueError("Amount cannot be negative.")
            except ValueError as e:
                print(f"Invalid input for amount: {e}")
                continue
            create_account(accounts, account_number, name, amount, account_type, contact)

        elif choice == "2":
            account_number = input("Enter account number: ")
            account = get_account(accounts, account_number)
            if account:
                try:
                    amount = float(input("Enter deposit amount: "))
                except ValueError:
                    print("Invalid amount entered.")
                    continue
                deposit(account, amount)

        elif choice == "3":
            account_number = input("Enter account number: ")
            account = get_account(accounts, account_number)
            if account:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                except ValueError:
                    print("Invalid amount entered.")
                    continue
                withdraw(account, amount)

        elif choice == "4":
            account_number = input("Enter account number: ")
            account = get_account(accounts, account_number)
            if account:
                check_balance(account)

        elif choice == "5":
            account_number = input("Enter account number: ")
            account = get_account(accounts, account_number)
            if account:
                display(account)

        elif choice == "6":
            print("Thank you for using the Bank Management System. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
