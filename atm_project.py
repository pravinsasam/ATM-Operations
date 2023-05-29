import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('bank.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table to store account information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY,
        name TEXT,
        balance REAL
    )
''')

# Function to create a new account
def create_account():
    name = input("Enter account holder's name: ")
    balance = float(input("Enter initial balance: "))
    
    # Insert the new account into the database
    cursor.execute('INSERT INTO accounts (name, balance) VALUES (?, ?)', (name, balance))
    conn.commit()

    # Retrieve the user ID of the newly created account
    cursor.execute('SELECT id FROM accounts WHERE name = ?', (name,))
    result = cursor.fetchone()
    
    if result is not None:
        account_id = result[0]
        print("Account created successfully!")
        print("Account ID:", account_id)
        print("---------------------------")
    else:
        print("Failed to create the account.")



# Function to deposit money into an account
def deposit():
    account_id = int(input("Enter account ID: "))
    amount = float(input("Enter amount to deposit: "))
    
    # Retrieve the current balance of the account
    cursor.execute('SELECT balance FROM accounts WHERE id = ?', (account_id,))
    result = cursor.fetchone()
    
    if result is None:
        print("Account not found.")
    else:
        balance = result[0]
        new_balance = balance + amount
        
        # Update the account balance in the database
        cursor.execute('UPDATE accounts SET balance = ? WHERE id = ?', (new_balance, account_id))
        conn.commit()
        
        print("Deposit successful!")
        print("New balance:", new_balance)
        print("---------------------------")

# Function to withdraw money from an account
def withdraw():
    account_id = int(input("Enter account ID: "))
    amount = float(input("Enter amount to withdraw: "))
    
    # Retrieve the current balance of the account
    cursor.execute('SELECT balance FROM accounts WHERE id = ?', (account_id,))
    result = cursor.fetchone()
    
    if result is None:
        print("Account not found.")
    else:
        balance = result[0]
        
        if amount > balance:
            print("Insufficient funds.")
        else:
            new_balance = balance - amount
            
            # Update the account balance in the database
            cursor.execute('UPDATE accounts SET balance = ? WHERE id = ?', (new_balance, account_id))
            conn.commit()
            
            print("Withdrawal successful!")
            print("New balance:", new_balance)
            print("---------------------------")

# Function to check the balance of an account
def check_balance():
    account_id = int(input("Enter account ID: "))
    
    # Retrieve the current balance of the account
    cursor.execute('SELECT balance FROM accounts WHERE id = ?', (account_id,))
    result = cursor.fetchone()
    
    if result is None:
        print("Account not found.")
        print("---------------------------")

    else:
        balance = result[0]
        print("Current balance:", balance)
        print("---------------------------")

# Main menu
def main_menu():
    print("Banking System")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")
    
    if choice == '1':
        create_account()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        check_balance()
    elif choice == '5':
        print("Thank you for using our banking system!")
        conn.close()
        exit()
    else:
        print("Invalid choice. Please try again.")
        print("---------------------------")

# Main program
while True:
    main_menu()