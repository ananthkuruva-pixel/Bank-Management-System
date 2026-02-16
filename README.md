# 🏦 Bank Management System (Python + MySQL)

A **modular, CLI-based Bank Management System** built using **Python** and **MySQL**.
This project demonstrates **database connectivity, CRUD operations, and clean project architecture** following **industry-style Python packaging**.

---

## 🚀 Features

* Create new bank accounts
* Deposit and withdraw money
* Check account balance
* Persistent storage using MySQL
* Modular and maintainable code structure
* Basic unit testing included

---

## 🛠️ Tech Stack

* **Python 3**
* **MySQL**
* **mysql-connector-python**
* **PyTest (basic testing)**

---

## 📂 Project Structure

```
bank-management-system/
│
├── src/
│   └── bank_system/
│       ├── __init__.py
│       ├── main.py
│       ├── menu.py
│       ├── account_operations.py
│       └── db_config.py
│
├── tests/
│   └── test_basic.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ananthkuruva-pixel/Bank-Management-System.git
cd Bank-Management-System
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure MySQL

Create database and table:

```sql
CREATE DATABASE bank_db;

USE bank_db;

CREATE TABLE accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    balance FLOAT
);
```

Update credentials in:

```
src/bank_system/db_config.py
```

---

## ▶️ Run the Application

```bash
python -m bank_system.main
```

---

## 🧪 Run Tests

```bash
pytest
```

---

## 🎯 Learning Outcomes

* Python package structuring using **src layout**
* MySQL integration with **mysql-connector**
* Clean separation of **menu, logic, and database layers**
* Basic **unit testing practices**
* Writing **professional-quality README & repo structure**

---

## 👨‍💻 Author

**Anantha Kumar**

* GitHub: https://github.com/ananthkuruva-pixel

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 📸 Application Execution Output

The screenshot below demonstrates a complete execution flow of the
**Bank Management System CLI application**, including:

* Creating multiple bank accounts with secure PIN setup
* Viewing all stored customer accounts from the MySQL database
* Performing deposit and withdrawal transactions
* Validating incorrect and correct PIN authentication
* Checking final account balance after transactions
* Gracefully exiting the system

This confirms that the application is **fully functional**,
with proper **database persistence, transaction handling, and user interaction**
through a structured command-line interface.

---
---

## 🖥️ Complete Terminal Execution Output

Below is the full sample execution of the **Bank Management System CLI**,
showing account creation, transactions, PIN validation, and balance inquiry.

```
Bank Management System
1. Create Account
2. View Accounts
3. Deposit Money
4. Withdraw Money
5. Check Balance
6. Exit

Enter Your Choice: 1
Enter your First name = ananth
Enter your email address = ananth@gmail.com
Create a strong 6 digits pin = 123456
Enter your opening balance must above 1000 = 2000
Account Created successfully!

Enter Your Choice: 1
Enter your First name = bharath
Enter your email address = bharath@gmail.com
Create a strong 6 digits pin = 234567
Enter your opening balance must above 1000 = 3000
Account Created successfully!

Enter Your Choice: 2
All Accounts
ID: 1, Name: nandu, Email: nakjlj, Balance: 25532.0
ID: 2, Name: ananth, Email: ananth@amil.com, Balance: 36444.0
ID: 3, Name: ananth, Email: ananth@gmail.com, Balance: 2000.0
ID: 4, Name: bharath, Email: bharath@gmail.com, Balance: 3000.0

Enter Your Choice: 3
Enter Account Id: 1
Enter your pin: 123445
Please enter correct pin

Enter Your Choice: 3
Enter Account Id: 3
Enter your pin: 123456
Enter deposit amount: 20000
Money Deposited successfully

Enter Your Choice: 4
Enter Account Id: 3
Enter your pin: 123456
Enter amount to withdraw: 10000
Withdrawal successfully

Enter Your Choice: 5
Enter Account Id: 3
Enter your pin: 123456
Account Holder: ananth, Balance: 12000.0

Enter Your Choice: 6
Exiting System. Thank you!
```

### ✔ Functionalities Demonstrated

* Secure **account creation with PIN**
* Viewing stored accounts from **MySQL database**
* **Deposit and withdrawal** transactions
* **PIN validation** for security
* Accurate **balance calculation**
* Proper **system exit handling**

This confirms the application is **fully operational and database-integrated**.

---

