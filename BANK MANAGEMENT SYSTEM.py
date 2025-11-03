
# BANK MANAGEMENT SYSTEM
#Ayush Vishnoi
# Format: { account_number: {"name": ..., "balance": ...} }
bank_accounts = {}

def create_account():
    print("\n--- Create New Account ---")
    acc_num = input("Enter new account number: ")

    if acc_num in bank_accounts:
        print("This account number already exists!")
        return

    name = input("Enter account holder name: ")
    initial_balance = float(input("Enter initial deposit amount: "))

    # Store account details in dictionary
    bank_accounts[acc_num] = {"name": name, "balance": initial_balance}
    print(f"Account created for {name} with ₹{initial_balance}\n")

def deposit_money():
    print("\n--- Deposit Money ---")
    acc_num = input("Enter account number: ")

    if acc_num not in bank_accounts:
        print(" Account not found.")
        return

    amount = float(input("Enter amount to deposit: "))
    bank_accounts[acc_num]["balance"] += amount
    print(f" ₹{amount} deposited. New balance: ₹{bank_accounts[acc_num]['balance']}\n")

def withdraw_money():
    print("\n--- Withdraw Money ---")
    acc_num = input("Enter account number: ")

    if acc_num not in bank_accounts:
        print("Account not found.")
        return

    amount = float(input("Enter amount to withdraw: "))
    if amount > bank_accounts[acc_num]["balance"]:
        print("Not enough balance.")
    else:
        bank_accounts[acc_num]["balance"] -= amount
        print(f"₹{amount} withdrawn. Remaining balance: ₹{bank_accounts[acc_num]['balance']}\n")

def check_balance():
    print("\n--- Check Account Balance ---")
    acc_num = input("Enter account number: ")

    if acc_num in bank_accounts:
        details = bank_accounts[acc_num]
        print(f"Account Holder: {details['name']}")
        print(f"Current Balance: ₹{details['balance']}\n")
    else:
        print("Account not found.\n")

def show_all_accounts():
    print("\n--- All Bank Accounts ---")
    if not bank_accounts:
        print("No accounts found.")
    else:
        for acc_num, info in bank_accounts.items():
            print(f"Account No: {acc_num} | Name: {info['name']} | Balance: ₹{info['balance']}")
    print()

def main():
    while True:
        print("\n===== BANK MENU =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View All Accounts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            show_all_accounts()
        elif choice == "6":
            print(" Thank you for using the Bank Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

# Program starts here
if __name__ == "__main__":
    main()
