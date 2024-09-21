# Banking Application

This is a simple banking application implemented in Python. The application allows users to create accounts, log in, deposit money, withdraw money, check their balance, and log out. The account information is stored in a dictionary.

## Features

- **Create a New Account**: Users can create a new bank account.
- **Login to Your Account**: Users can log in to their existing accounts.
- **Deposit Money**: Users can deposit money into their accounts.
- **Withdraw Money**: Users can withdraw money from their accounts.
- **Check Balance**: Users can check their account balance.
- **Logout**: Users can securely log out of their accounts.

## Technologies

- Python

## Code Explanation

The script follows these steps:

1. **Generate Account Number**: Uses the `random` module to generate a unique 10-digit account number.
2. **Hash Password**: Uses the `hashlib` module to hash the user's password for secure storage.
3. **Create Account**: Prompts the user to enter their first name, last name, and password to create a new account. The account information is stored in the `bank_database` dictionary.
4. **Login**: Prompts the user to enter their account number and password to log in. The password is hashed and compared with the stored hash.
5. **Deposit Money**: Allows the user to deposit money into their account.
6. **Withdraw Money**: Allows the user to withdraw money from their account, checking for sufficient balance.
7. **Check Balance**: Displays the current balance of the user's account.
8. **Logout**: Logs the user out of their account.

## Usage

To use this script, simply run it in a Python environment. Follow the on-screen prompts to create an account, log in, and perform banking operations.
