# 📚 Library Management System

A console-based Library Management System developed using **Python and MySQL** to manage books, members, book issues, returns, and payments through a structured and user-friendly menu-driven application.

## 📌 Project Overview

The Library Management System provides separate access for **Admin** and **Member** users.

The Admin can manage books and members, issue and return books, and manage payment dues. Members can view available books, check their issue and payment records, and pay their dues.

The project follows an object-oriented and modular structure, with database operations separated into a dedicated `Database` class.

## ✨ Features

### 👨‍💼 Admin

- Admin Login
- Add Book
- View Books
- Update Book
- Delete Book
- Add Member
- View Members
- Update Member
- Delete Member
- Issue Book
- Return Book
- View Issue Records
- View Payment Records
- Create Payment Due
- Logout

### 👤 Member

- Member Login
- View Books
- View My Issues
- View My Payments
- Pay Due
- Logout

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application development |
| MySQL | Database management |
| MySQL Connector/Python | Python–MySQL connectivity |
| PrettyTable | Tabular display of records |

## 🧱 Project Structure

```text
Library_Management_System/
│
├── main.py
├── database.py
├── admin.py
├── member.py
├── book.py
├── issue.py
├── payment.py
└── README.md