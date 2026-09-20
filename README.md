# 📚 Library Management System

A console-based **Library Management System** built using **Python and
MySQL**.

The system provides separate Admin and Member access for managing books,
members, book issues, returns, and payment dues.

------------------------------------------------------------------------

## ✨ Features

### 👨‍💼 Admin

-   Admin login
-   Add, view, update and delete books
-   Add, view, update and delete members
-   Issue and return books
-   View issue records
-   Create and view payment dues

### 👤 Member

-   Member login
-   View available books
-   View personal issue records
-   View payment records
-   Pay outstanding dues

### 📊 Other Features

-   MySQL database connectivity
-   CRUD operations
-   Object-Oriented Programming
-   Foreign key relationships
-   PrettyTable console output
-   Modular Python structure

------------------------------------------------------------------------

## 🛠️ Technologies Used

  Technology               Purpose
  ------------------------ -----------------------------
  Python                   Application development
  MySQL                    Database
  MySQL Connector/Python   Python-MySQL connectivity
  PrettyTable              Table-based console display

------------------------------------------------------------------------

## 📁 Project Structure

``` text
Library-Management-System/
│
├── main.py
├── database.py
├── admin.py
├── member.py
├── book.py
├── issue.py
├── payment.py
├── library_management.sql
└── README.md
```

  File                       Description
  -------------------------- ------------------------------------------
  `main.py`                  Main application and menus
  `database.py`              MySQL connection and database operations
  `admin.py`                 Admin functionality
  `member.py`                Member functionality
  `book.py`                  Book model
  `issue.py`                 Issue and return functionality
  `payment.py`               Payment and due functionality
  `library_management.sql`   Database schema

------------------------------------------------------------------------

# 🚀 Setup and Installation

Follow these steps to run the project.

### 1. Clone the Repository

``` bash
git clone https://github.com/iganeshjogi/Library-Management-System.git
cd Library-Management-System
```

Or download the repository as a ZIP file and open it in VS Code.

### 2. Install Python

Check that Python is installed:

``` bash
python --version
```

### 3. Install MySQL

Install:

-   MySQL Server
-   MySQL Workbench

Make sure MySQL Server is running.

### 4. Create the Database

Open `library_management.sql` in MySQL Workbench and execute it.

It creates the:

``` text
library_management
```

database and these tables:

``` text
admin
book
member
issue
payment
```

### 5. Configure Database Connection

Open `database.py` and enter your own MySQL credentials:

``` python
self.conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="library_management"
)
```

Replace `YOUR_MYSQL_PASSWORD` with your local MySQL password.

> ⚠️ Never upload your real MySQL password to GitHub.

### 6. Install Python Packages

``` bash
pip install mysql-connector-python prettytable
```

### 7. Create an Admin Account

Open MySQL Workbench and run:

``` sql
USE library_management;

INSERT INTO admin (username, password)
VALUES ('admin', 'admin123');
```

You can replace these credentials with your own.

### 8. Run the Application

``` bash
python main.py
```

------------------------------------------------------------------------

# ▶️ How to Use

After starting the application, the main menu appears:

``` text
========== LIBRARY MANAGEMENT SYSTEM ==========

1. Admin Login
2. Member Login
0. Exit
```

## Admin Workflow

``` text
Admin Login
     ↓
Add Book
     ↓
Add Member
     ↓
Issue Book
     ↓
View Issues
     ↓
Create Due
     ↓
View Payments
     ↓
Return Book
```

The Admin menu provides:

``` text
1. Add Book
2. View Books
3. Update Book
4. Delete Book
5. Add Member
6. View Members
7. Update Member
8. Delete Member
9. Issue Book
10. Return Book
11. View Issues
12. View Payments
13. Create Due
0. Logout
```

## Member Workflow

First create a member using **Admin → Add Member**.

Then use:

``` text
Member Login
     ↓
View Books
     ↓
View My Issues
     ↓
View My Payments
     ↓
Pay Due
```

The Member menu provides:

``` text
1. View Books
2. View My Issues
3. View My Payments
4. Pay Due
0. Logout
```

------------------------------------------------------------------------

# 🗄️ Database Structure

``` text
library_management
│
├── admin
├── book
├── member
├── issue
└── payment
```

### Relationships

``` text
Book
  │
  └──────► Issue ◄────── Member
              │
              ▼
           Payment
```

Foreign keys:

``` text
issue.book_id       → book.book_id
issue.member_id     → member.member_id
payment.issue_id    → issue.issue_id
payment.member_id  → member.member_id
```

------------------------------------------------------------------------

# 🧩 OOP Concepts

The project uses:

-   Classes and Objects
-   Constructors
-   Methods
-   Encapsulation
-   Modular Programming
-   Database Connectivity

Main classes:

``` text
Admin
Member
Book
Issue
Payment
Database
```

------------------------------------------------------------------------

# 📊 Sample Output

The application uses **PrettyTable** for displaying records:

``` text
+---------+----------------+----------------+-------------+----------+-----------+
| Book ID | Title          | Author         | Category    | Quantity | Available |
+---------+----------------+----------------+-------------+----------+-----------+
|    1    | Python Basics  | Example Author | Programming |    5     |     5     |
+---------+----------------+----------------+-------------+----------+-----------+
```

------------------------------------------------------------------------

# 🔒 Security Note

This project is intended for learning and demonstration purposes.

For a production application, consider using:

-   Password hashing
-   Environment variables
-   Secure credential management
-   Strong authentication
-   Better input validation

------------------------------------------------------------------------

# 🎯 Learning Objectives

This project demonstrates practical use of:

-   Python
-   OOP
-   MySQL
-   SQL CRUD operations
-   Database relationships
-   Foreign keys
-   Python-MySQL connectivity
-   Modular programming
-   Authentication
-   Book and member management
-   Issue and return management
-   Payment tracking

------------------------------------------------------------------------

# 👨‍💻 Author

**Ganesh Jogi**

B.Tech Electrical Engineering \| Python \| SQL & MySQL \| Data Analytics
\| Data Science & AI

GitHub:\
https://github.com/iganeshjogi

------------------------------------------------------------------------

⭐ Feel free to explore the project and its source code.
