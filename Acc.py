# Base class
class BankAccount:
    def __init__(self, BankOwner, AccNo, AccBal=0):  # Fixed: __init__ should have double underscores
        self.BankOwner = BankOwner
        self.AccNo = AccNo
        self.AccBal = AccBal

# Function to create and display bank accounts
def create_accounts():
    accounts = []  # List to store account instances

    while True:
        # Query user for account details
        BankOwner = input("Enter the account owner's name (or 'exit' to quit): ")
        if BankOwner.lower() == 'exit':  # Allow user to exit
            break
        AccNo = input("Enter the account number: ")
        AccBal = float(input("Enter the initial balance: "))

        # Create a new instance of BankAccount
        new_account = BankAccount(BankOwner, AccNo, AccBal)
        accounts.append(new_account)  # Add the account to the list

        # Print account details
        print(f"\nAccount created successfully!")
        print(f"Account Owner: {new_account.BankOwner}")
        print(f"Account Number: {new_account.AccNo}")
        print(f"Account Balance: ${new_account.AccBal:.2f}\n")  # Fixed: Formatting to show two decimal places

    # Print all created accounts
    print("All created accounts:")
    for account in accounts:
        print(f"Account Owner: {account.BankOwner}, Account Number: {account.AccNo}, Account Balance: ${account.AccBal:.2f}")

# Call the function to start creating accounts
create_accounts()