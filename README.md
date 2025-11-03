BANK MANAGEMENT SYSTEM - README
--------------------------------

Project Title:
Bank Management System (In-Memory Python Implementation)

Author:
Ayush Vishnoi

Description:
This project is a simple Bank Management System built using core Python concepts.
It allows users to create and manage bank accounts, deposit and withdraw money, 
and view account details — all stored in memory without using external databases.

--------------------------------
FEATURES
--------------------------------
1. Create a new bank account (Savings or Current)
2. Deposit money into an account
3. Withdraw money from an account
4. View account details
5. Display all registered accounts
6. Exit the system safely

--------------------------------
DATA STRUCTURES USED
--------------------------------
- Tuple: Stores fixed account types (Savings, Current)
- Dictionary: Stores all bank account data (key = account number)
- Set: Keeps track of unique account numbers

--------------------------------
HOW TO RUN THE PROGRAM
--------------------------------
1. Make sure Python 3 is installed on your system.
2. Save the file as "BANK MANAGEMENT SYSTEM.py".
3. Open a terminal or command prompt in the same folder.
4. Run the program using the command:
   python "BANK MANAGEMENT SYSTEM.py"

--------------------------------
CODE STRUCTURE
--------------------------------
- create_account(): Creates a new account and adds it to the dictionary.
- deposit_money(): Adds funds to an existing account.
- withdraw_money(): Deducts funds if balance is sufficient.
- display_account(): Shows details of a single account.
- display_all_accounts(): Lists all existing accounts.
- main menu loop: Lets users select operations interactively.

--------------------------------
NOTES
--------------------------------
- This project uses only core Python (no external libraries).
- All account data is stored temporarily during runtime.
  (Data will be lost when the program closes.)
- Designed for educational and learning purposes.

--------------------------------
AUTHOR’S NOTE
--------------------------------
This project was created to demonstrate Python basics —
like dictionaries, sets, tuples, functions, and control flow — 
in a practical, real-world application.

--------------------------------
END OF FILE
--------------------------------
