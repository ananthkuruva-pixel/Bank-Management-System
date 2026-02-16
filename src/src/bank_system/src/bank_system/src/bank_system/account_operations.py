from db_config import connect


def verify_pin(cursor, acc_id, passwordpin):
    """Verify if the entered PIN matches the database PIN"""
    cursor.execute("SELECT passwordpin FROM accounts WHERE id = %s", (acc_id,))
    result = cursor.fetchone()
    if result and result[0] == passwordpin:
        return True
    return False


def create_account():
    name = input("Enter your First name = ")
    email = input("Enter your email address = ")
    passwordpin = int(input("Create a strong 6 digits pin = "))
    balance = float(input("Enter your opening balance  must above 1000 = "))
    db = connect()
    cursor = db.cursor()
    sql = "INSERT INTO accounts (name, email, passwordpin, balance) VALUES (%s, %s, %s, %s)"
    values = (name, email, passwordpin, balance)
    cursor.execute(sql, values)
    db.commit()
    print("Account Created successfully!")
    db.close()


def view_accounts():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT id, name, email, balance FROM accounts")
    accounts = cursor.fetchall()
    print("All Accounts")
    for acc in accounts:
        print(f"ID: {acc[0]}, Name: {acc[1]}, Email: {acc[2]}, Balance: {acc[3]}")
    db.close()


def deposit_money():
    acc_id = int(input("Enter Account Id: "))
    passwordpin = int(input("Enter your pin: "))
    db = connect()
    cursor = db.cursor()
    
    if verify_pin(cursor, acc_id, passwordpin):
        amount = float(input("Enter deposit amount: "))
        cursor.execute("UPDATE accounts SET balance = balance + %s WHERE id = %s", (amount, acc_id))
        db.commit()
        print("Money Deposited successfully")
    else:
        print("Please enter correct pin")
    
    db.close()


def withdraw_money():
    acc_id = int(input("Enter Account Id: "))
    passwordpin = int(input("Enter your pin: "))
    db = connect()
    cursor = db.cursor()
    
    if verify_pin(cursor, acc_id, passwordpin):
        amount = float(input("Enter amount to withdraw: "))
        cursor.execute("SELECT balance FROM accounts WHERE id = %s", (acc_id,))
        result = cursor.fetchone()
        if result and result[0] >= amount:
            cursor.execute("UPDATE accounts SET balance = balance - %s WHERE id = %s", (amount, acc_id))
            db.commit()
            print("Withdrawal successfully")
        else:
            print("Insufficient balance")
    else:
        print("Please enter correct pin")
    
    db.close()


def check_balance():
    acc_id = int(input("Enter Account Id: "))
    passwordpin = int(input("Enter your pin: "))
    db = connect()
    cursor = db.cursor()
    
    if verify_pin(cursor, acc_id, passwordpin):
        cursor.execute("SELECT name, balance FROM accounts WHERE id = %s", (acc_id,))
        result = cursor.fetchone()
        if result:
            print(f"Account Holder: {result[0]}, Balance: {result[1]}")
        else:
            print("Account not found")
    else:
        print("Please enter correct pin")
    
    db.close()
