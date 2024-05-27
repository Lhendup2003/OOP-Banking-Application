#Pema Lhendup
#02230221
#1 ICE
#chatgpt(https://chatgpt.com/?oai-dm=1)
#copilot
#wb3(https://www.w3schools.com/python/)
import random  # Importing the random module for generating random numbers
import os  # Importing the os module for interacting with the operating system

# Base Account class for shared attributes and methods
class Account:
    def __init__(self, account_number, password, account_type, balance=0):
        self.account_number = account_number  # Initializing account number attribute
        self.password = password  # Initializing password attribute
        self.account_type = account_type  # Initializing account type attribute
        self.balance = balance  # Initializing balance attribute
    
    # code to deposit money into the account
    def deposit(self, amount):
        self.balance += amount  # Adding deposit amount to the balance
        print(f"Deposited Ngultrum {amount}. New balance: Ngultrum {self.balance}")  # Printing deposit confirmation
    
    # code to withdraw money from the account
    def withdraw(self, amount):
        if amount > self.balance:  # Checking if withdrawal amount exceed current balance
            print("Insufficient funds.")  # If balance is insufficient
        else:
            self.balance -= amount  # Subtracting the withdrawal amount from the  balance
            print(f"Withdrew Ngultrum {amount}. New balance: Ngultrum {self.balance}")  # confirming the withdrew
    
    # Code to check the current balance of the account
    def check_balance(self):
        return self.balance  # Returning the current balance

    # code to transfer money to another account
    def transfer(self, amount, recipient_account):
        if amount > self.balance:  # Checking if transfer amount exceeds current balance
            print("Insufficient funds.")  # Printing message if balance is insufficient
        else:
            self.withdraw(amount)  # Withdrawing amount from sender's account
            recipient_account.deposit(amount)  # Depositing amount to recipient's account
            print(f"Transferred Ngultrum {amount} to account {recipient_account.account_number}")  # Printing transfer confirmation

    # COde to update the account number
    def update_account_number(self, new_account_number):
        self.account_number = new_account_number  # Updating the account number

    # Code to update the account password
    def update_password(self, new_password):
        self.password = new_password  # Updating the account password

    # Code to get account type to choose
    def get_account_details(self):
        if self.account_type == "Business":  # Checking account type
            return f"Business Account: {self.business_name}"  # Returning business account details
        elif self.account_type == "Personal":  # Checking account type
            return f"Personal Account: {self.owner_name}"  # Returning personal account details
        else:
            return "Unknown Account Type"  # Returning message for unknown account type

# Define a subclass BusinessAccount, inheriting from the Account superclass.
class BusinessAccount(Account):
        # Initialize a new BusinessAccount object with account number, password, balance,
         # and optional business name.
    def __init__(self, account_number, password, balance=0, business_name=""):
        super().__init__(account_number, password, "Business", balance)  # Calling superclass constructor
        # Initialize the business_name attribute specific to BusinessAccount.
        self.business_name = business_name  # Initializing business name attribute

# Define a subclass PersonalAccount, inheriting from the Account superclass.
class PersonalAccount(Account):
    # Initialize a new PersonalAccount object with account number, password, balance,and optional owner name.
    def __init__(self, account_number, password, balance=0, owner_name=""):
        super().__init__(account_number, password, "Personal", balance)  # Calling superclass constructor
        # Initialize the owner_name attribute specific to PersonalAccount.
        self.owner_name = owner_name  # Initializing owner name attribute

# Function to save account information to a file
def save_accounts(accounts):
    with open('accounts.txt', 'w') as file:  # Opening file in write mode
        for acc in accounts.values():  # Iterating over account objects
            data = [acc.account_number, acc.password, acc.account_type, str(acc.balance)]  # Creating data list
            if acc.account_type == "Business":  # Checking account type
                data.append(acc.business_name)  # Appending business name if account is of type Business
            elif acc.account_type == "Personal":  # Checking account type
                data.append(acc.owner_name)  # Appending owner name if account is of type Personal
            file.write(','.join(data) + '\n')  # Writing data to file

# Function to load account information from a file
def load_accounts():
    accounts = {}  # Creating an empty dictionary to store accounts
    if os.path.exists('accounts.txt'):  # Checking if file exists
        with open('accounts.txt', 'r') as file:  # Opening file in read mode
            for line in file:  # Iterating over lines in file
                parts = line.strip().split(',')  # Splitting line into parts
                account_number, password, account_type, balance = parts[:4]  # Extracting account information
                balance = float(balance)  # Converting balance to float
                if account_type == "Business":  # Checking account type
                    business_name = parts[4]  # Extracting business name
                    accounts[account_number] = BusinessAccount(account_number, password, balance, business_name)  # Creating BusinessAccount object
                elif account_type == "Personal":  # Checking account type
                    owner_name = parts[4]  # Extracting owner name
                    accounts[account_number] = PersonalAccount(account_number, password, balance, owner_name)  # Creating PersonalAccount object
    return accounts  # Returning loaded accounts dictionary

# Function to create a new account
def create_account():
    account_number = str(random.randint(10000, 99999))  # Generating random account number
    password = str(random.randint(1000, 9999))  # Generating random password
    account_type = input("Enter account type (Business/Personal): ").capitalize()  # Taking input for account type

    if account_type == "Business":  # Checking account type
        business_name = input("Enter business name: ")  # Taking input for business name
        account = BusinessAccount(account_number, password, business_name=business_name)  # Creating BusinessAccount object
    elif account_type == "Personal":  # Checking account type
        account_holder_name = input("Enter owner name: ")  # Taking input for owner name
        account = PersonalAccount(account_number, password, owner_name=account_holder_name)  # Creating PersonalAccount object
    else:
        print("Invalid Account Type")  # Printing message for invalid account type
        return None
    
    accounts = load_accounts()  # Loading existing accounts
    accounts[account_number] = account  # Adding new account to accounts dictionary
    save_accounts(accounts)  # Saving updated accounts to file
    print(f"Account created! Your account number is {account_number} and password is {password}")  # Printing account creation confirmation

# Function to login to an existing account
def login(accounts):
    account_number = input("Enter account number: ")  # Taking input for account number
    password = input("Enter password: ")  # Taking input for password
    account = accounts.get(account_number)  # Retrieving account from accounts dictionary
    if account and account.password == password:  # Checking if account exists and password is correct
                print(f"Welcome, {account.account_type} account holder!")  # Printing welcome message with account type
                return account  # Returning the logged-in account
    else:
        print("Invalid account number or password.")  # Printing message for invalid credentials
        return None  # Returning None if login fails

# Function to delete an account
def delete_account(account, accounts):
    if account.account_number in accounts:  # Checking if account exists in accounts dictionary
        del accounts[account.account_number]  # Deleting account from accounts dictionary
        save_accounts(accounts)  # Saving updated accounts to file
        print("Account Deleted Successfully.")  # Printing deletion confirmation
    else:
        print("Account Not Found.")  # Printing message if account not found

# Function to change account details
def change_account_details(account, accounts):
    print("\n1. Change Account Number\n2. Change Password")  # Printing options for changing account details
    choice = input("Enter choice: ")  # Taking input for choice

    if choice == '1':  # Checking if choice is to change account number
        new_account_number = input("Enter new account number: ")  # Taking input for new account number
        if new_account_number in accounts:  # Checking if new account number already exists
            print("Account number already exists.")  # Printing message if account number already exists
        else:
            old_account_number = account.account_number  # Storing old account number
            account.update_account_number(new_account_number)  # Updating account number
            accounts[new_account_number] = account  # Adding updated account to accounts dictionary
            del accounts[old_account_number]  # Deleting old account from accounts dictionary
            save_accounts(accounts)  # Saving updated accounts to file
            print("Account Number Changed Successfully.")  # Printing success message
    elif choice == '2':  # Checking if choice is to change password
        new_password = input("Enter new password: ")  # Taking input for new password
        account.update_password(new_password)  # Updating account password
        save_accounts(accounts)  # Saving updated accounts to file
        print("Password Changed Successfully.")  # Printing success message
    else:
        print("Invalid Choice.")  # Printing message for invalid choice

# Main function containing the program logic
def main():
    while True:
        print("\n1. Create Account\n2. Login\n3. Exit")  # Printing main menu options for user to choose the option
        choice = input("Enter choice: ")  # Taking input for choice

        if choice == '1':  # Checking if choice is to create an account
            create_account()  # Calling create_account function
        elif choice == '2':  # Checking if choice is to login
            accounts = load_accounts()  # Loading existing accounts
            account = login(accounts)  # Calling login function
            if account:
                while True:
                    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Transfer\n5. Delete Account\n6. Change Account Details\n7. Logout")  # Printing transaction options
                    trans_choice = input("Enter choice: ")  # Taking user input for transaction choice

                    if trans_choice == '1':  # Checking if choice is to deposit money
                        amount = float(input("Enter Amount To Deposit: "))  # Taking input for deposit amount
                        account.deposit(amount)  # Calling deposit method
                        save_accounts(accounts)  # Saving updated accounts to file
                    elif trans_choice == '2':  # Checking if choice is to withdraw money
                        amount = float(input("Enter Amount To Withdraw: "))  # Taking input for withdrawal amount
                        account.withdraw(amount)  # Calling withdraw method
                        save_accounts(accounts)  # Saving updated accounts to file
                    elif trans_choice == '3':  # Checking if choice is to check balance
                        print(f"Balance: Ngultrum {account.check_balance()}")  # Calling check_balance method and printing balance
                    elif trans_choice == '4':  # Checking if choice is to transfer money
                        recipient_number = input("Enter Recipient Account Number: ")  # Taking input for recipient account number
                        recipient = accounts.get(recipient_number)  # Retrieving recipient account from accounts dictionary
                        if recipient:  # Checking if recipient account exists
                            print(f"Recipient Account Details: {recipient.get_account_details()}")  # Printing recipient account details
                            confirm = input("Do you really want to proceed with the transfer? (yes/no): ").lower()  # Taking input for confirmation
                            if confirm == 'yes':  # Checking if confirmed
                                amount = float(input("Enter amount to transfer: "))  # Taking input for transfer amount
                                account.transfer(amount, recipient)  # Calling transfer method
                                save_accounts(accounts)  # Saving updated accounts to file
                            else:
                                print("Transfer Failed.")  # Printing cancellation message
                        else:
                            print("Sorry, Recipient Account Does Not Found.")  # Printing message if recipient account not found
                    elif trans_choice == '5':  # Checking if choice is to delete account
                        delete_account(account, accounts)  # Calling delete_account function
                        break  # Exiting transaction loop after account deletion
                    elif trans_choice == '6':  # Checking if choice is to change account details
                        change_account_details(account, accounts)  # Calling change_account_details function
                    elif trans_choice == '7':  # Checking if choice is to logout
                        save_accounts(accounts)  # Saving updated accounts to file
                        print("Logged Out.")  # Printing logout message
                        break  # Exiting transaction loop
        elif choice == '3':  # Checking if choice is to exit
            break  # Exiting main loop
        else:
            print("Invalid Choice. Please Try Again.")  # Printing message for invalid choice

# Entry point for the program
if __name__ == "__main__":
    main()  # Calling main function

