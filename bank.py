import hashlib
import random
import time
bank_database = {}
def generate_account_number():
    return random.randint(1000000000, 9999999999)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def create_account():
    print("==== Create a New Account ====")
    first_name = input("Enter your First Name: ")
    last_name = input("Enter your Last Name: ")
    password = input("Create a Password: ")
    hashed_password = hash_password(password)
    balance = 0
    account_number = generate_account_number()
    bank_database[account_number] = {"first_name": first_name,"last_name": last_name,"password": hashed_password,"balance": balance}
    print(f"\nAccount successfully created! Your account number is {account_number}\n")
def login():
    print("==== Login to Your Account ====")
    account_number = int(input("Enter your Account Number: "))
    password = input("Enter your Password: ")
    hashed_password = hash_password(password)
    if account_number in bank_database and bank_database[account_number]['password'] == hashed_password:
        print(f"\nWelcome, {bank_database[account_number]['first_name']}!\n")
        return account_number
    else:
        print("Invalid account number or password. Please try again.")
        return None
def deposit(account_number):
    print("\n==== Deposit Money ====")
    amount = float(input("Enter the amount to deposit: "))
    bank_database[account_number]['balance'] += amount
    print(f"\nDeposit successful! New balance: {bank_database[account_number]['balance']}\n")
def withdraw(account_number):
    print("\n==== Withdraw Money ====")
    amount = float(input("Enter the amount to withdraw: "))
    if amount <= bank_database[account_number]['balance']:
        bank_database[account_number]['balance'] -= amount
        print(f"\nWithdrawal successful! New balance: {bank_database[account_number]['balance']}\n")
    else:
        print("\nInsufficient balance.\n")
def check_balance(account_number):
    print(f"\nYour current balance is: {bank_database[account_number]['balance']}\n")
def logout():
    print("\nLogging out...\n")
    time.sleep(1)
    print("Logged out successfully!\n")
def banking_app():
    while True:
        print("==== Welcome to the Banking App ====")
        print("1. Create a New Account")
        print("2. Login to Your Account")
        print("3. Exit")
        option = input("\nSelect an option: ")
        if option == "1":
            create_account()
        elif option == "2":
            account_number = login()
            if account_number:
                while True:
                    print("\n==== Banking Menu ====")
                    print("1. Deposit Money")
                    print("2. Withdraw Money")
                    print("3. Check Balance")
                    print("4. Logout")
                    choice = input("\nSelect an option: ")
                    if choice == "1":
                        deposit(account_number)
                    elif choice == "2":
                        withdraw(account_number)
                    elif choice == "3":
                        check_balance(account_number)
                    elif choice == "4":
                        logout()
                        break
                    else:
                        print("\nInvalid choice. Please select again.\n")
        elif option == "3":
            print("\nThank you for using the Banking App. Goodbye!\n")
            break
        else:
            print("\nInvalid option. Please try again.\n")
banking_app()
