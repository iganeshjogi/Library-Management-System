from database import Database
from admin import Admin
from member import Member
from book import Book
from issue import Issue
from payment import Payment
from datetime import date
from getpass import getpass
from prettytable import PrettyTable

db = Database()

def display_books(books):

    table = PrettyTable()

    table.field_names = [
        "Book ID",
        "Title",
        "Author",
        "Category",
        "Quantity",
        "Available"
    ]

    for book in books:
        table.add_row([
            book.book_id,
            book.title,
            book.author,
            book.category,
            book.quantity,
            book.available_quantity
        ])

    print(table)

def display_members(members):

    table = PrettyTable()

    table.field_names = [
        "Member ID",
        "Name",
        "Email",
        "Phone"
    ]

    for member in members:
        table.add_row([
            member.member_id,
            member.name,
            member.email,
            member.phone
        ])

    print(table)

def display_issues(issues):

    table = PrettyTable()

    table.field_names = [
        "Issue ID",
        "Book ID",
        "Member ID",
        "Issue Date",
        "Return Date",
        "Status"
    ]

    for issue in issues:
        table.add_row([
            issue[0],
            issue[1],
            issue[2],
            issue[3],
            issue[4],
            issue[5]
        ])

    print(table)

def display_payments(payments):

    table = PrettyTable()

    table.field_names = [
        "Payment ID",
        "Issue ID",
        "Member ID",
        "Amount",
        "Payment Date",
        "Status"
    ]

    for payment in payments:
        table.add_row([
            payment[0],
            payment[1],
            payment[2],
            f"₹{payment[3]:.2f}",
            payment[4],
            payment[5]
        ])

    print(table)


def main_menu():

    while True:

        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Admin Login")
        print("2. Member Login")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            admin = admin_login()

            if admin:
                print(f"Welcome, {admin.username}!")
                admin_menu(admin)

        elif choice == "2":

            member = member_login()

            if member:
                print(f"Welcome, {member.name}!")
                member_menu(member)

        elif choice == "0":
            print("Thank you for using Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


def member_login():

    email = input("Enter member email: ")
    password = getpass("Enter member password: ")

    result = db.member_login(email, password)

    if result:
        print("\nMember login successful!")

        return Member(
            result[0],
            result[1],
            result[2],
            result[3],
            result[4]
        )

    print("\nInvalid member credentials.")
    return None


def admin_login():

    username = input("Enter admin username: ")
    password = getpass("Enter admin password: ")

    result = db.admin_login(username, password)

    if result:
        print("\nAdmin login successful!")
        return Admin(
            result[0],
            result[1],
            result[2]
        )

    print("\nInvalid admin credentials.")
    return None


def member_menu(member):

    while True:

        print("\n========== MEMBER MENU ==========")
        print("1. View Books")
        print("2. View My Issues")
        print("3. View My Payments")
        print("4. Pay Due")
        print("0. Logout")

        choice = input("Enter your choice: ")

        if choice == "0":

            print("Member logged out.")
            break

        elif choice == "1":

            print("\n========== BOOKS ==========")

            books = member.view_books(db)

            if not books:
                print("No books found.")
            else:
                display_books(books)


        elif choice == "2":

            print("\n========== MY ISSUES ==========")

            issues = member.view_my_issues(db)

            if not issues:
                print("You have no issue records.")
            else:
                display_issues(issues)


        elif choice == "3":

            print("\n========== MY PAYMENTS ==========")

            payments = member.view_my_payments(db)

            if not payments:
                print("You have no payment records.")
            else:
                display_payments(payments)


        elif choice == "4":

            print("\n========== PAY DUE ==========")

            try:
                payment_id = int(input("Enter payment ID: "))

            except ValueError:
                print("Invalid payment ID. Please enter a number.")
                continue

            payment_date = date.today()

            result = member.pay_due(
                db,
                payment_id,
                payment_date
            )

            print(result)


        else:
            print("Invalid choice. Please try again.")


def admin_menu(admin):

    while True:

        print("\n========== ADMIN MENU ==========")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Add Member")
        print("6. View Members")
        print("7. Update Member")
        print("8. Delete Member")
        print("9. Issue Book")
        print("10. Return Book")
        print("11. View Issues")
        print("12. View Payments")
        print("13. Create Due")
        print("0. Logout")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Admin logged out.")
            break

        if choice == "1":

            print("\n========== ADD BOOK ==========")

            title = input("Enter book title: ")
            author = input("Enter author: ")
            category = input("Enter category: ")

            try:
                quantity = int(input("Enter quantity: "))

            except ValueError:
                print("Invalid quantity. Please enter a number.")
                continue

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            book = Book(
                0,
                title,
                author,
                category,
                quantity,
                quantity
            )

            print(admin.add_book(db, book))

        elif choice == "2":

            books = admin.view_books(db)

            print("\n========== BOOKS ==========")

            if not books:
                print("No books found.")
            else:
                display_books(books)


        elif choice == "3":

            print("\n========== UPDATE BOOK ==========")

            try:
                book_id = int(input("Enter book ID: "))

            except ValueError:
                print("Invalid book ID. Please enter a number.")
                continue

            book = db.get_book(book_id)

            if not book:
                print("Book not found.")
                continue

            print("\nWhat do you want to update?")
            print("1. Title")
            print("2. Author")
            print("3. Category")
            print("4. Quantity")

            update_choice = input("Enter your choice: ")

            if update_choice == "1":

                new_title = input("Enter new title: ")
                book.title = new_title

            elif update_choice == "2":

                new_author = input("Enter new author: ")
                book.author = new_author

            elif update_choice == "3":

                new_category = input("Enter new category: ")
                book.category = new_category

            elif update_choice == "4":

                try:
                    new_quantity = int(input("Enter new quantity: "))

                except ValueError:
                    print("Invalid quantity. Please enter a number.")
                    continue

                if new_quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue

                issued_quantity = book.quantity - book.available_quantity

                if new_quantity < issued_quantity:
                    print(
                        f"Cannot set quantity below {issued_quantity} "
                        "because those books are currently issued."
                    )
                    continue

                book.quantity = new_quantity
                book.available_quantity = new_quantity - issued_quantity

            else:

                print("Invalid choice.")
                continue

            print(admin.update_book(db, book))

        elif choice == "4":

            print("\n========== DELETE BOOK ==========")

            try:
                book_id = int(input("Enter book ID: "))

            except ValueError:
                print("Invalid book ID. Please enter a number.")
                continue

            book = db.get_book(book_id)

            if not book:
                print("Book not found.")
                continue

            if book.available_quantity < book.quantity:
                print("Cannot delete book.")
                print("This book currently has issued copies.")
                continue

            print("\nBook found:")
            print(book)

            confirm = input("Are you sure you want to delete this book? (yes/no): ")

            if confirm.lower() == "yes":

                print(admin.delete_book(db, book_id))

            else:

                print("Book deletion cancelled.")

        elif choice == "5":

            print("\n========== ADD MEMBER ==========")

            name = input("Enter member name: ")
            email = input("Enter member email: ")
            phone = input("Enter phone: ")
            password = input("Enter password: ")

            member = Member(
                0,
                name,
                email,
                phone,
                password
            )

            print(admin.add_member(db, member))

        elif choice == "6":

            print("\n========== MEMBERS ==========")

            members = admin.view_members(db)

            if not members:
                print("No members found.")
            else:
                display_members(members)
                

        elif choice == "7":

            print("\n========== UPDATE MEMBER ==========")

            try:
                member_id = int(input("Enter member ID: "))

            except ValueError:
                print("Invalid member ID. Please enter a number.")
                continue

            member = db.get_member(member_id)

            if not member:
                print("Member not found.")
                continue

            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Email")
            print("3. Phone")
            print("4. Password")

            update_choice = input("Enter your choice: ")

            if update_choice == "1":

                new_name = input("Enter new name: ")
                member.name = new_name

            elif update_choice == "2":

                new_email = input("Enter new email: ")
                member.email = new_email

            elif update_choice == "3":

                new_phone = input("Enter new phone: ")
                member.phone = new_phone

            elif update_choice == "4":

                new_password = input("Enter new password: ")
                member.password = new_password

            else:

                print("Invalid choice.")
                continue

            print(admin.update_member(db, member))

        elif choice == "8":

            print("\n========== DELETE MEMBER ==========")

            try:
                member_id = int(input("Enter member ID: "))

            except ValueError:
                print("Invalid member ID. Please enter a number.")
                continue

            member = db.get_member(member_id)

            if not member:
                print("Member not found.")
                continue

            print("\nMember found:")
            print(member)

            if db.member_has_issues(member_id):

                print("Cannot delete member.")
                print("This member has existing issue records.")
                continue

            confirm = input(
                "Are you sure you want to delete this member? (yes/no): "
            )

            if confirm.lower() == "yes":

                print(admin.delete_member(db, member_id))

            else:

                print("Member deletion cancelled.")


        elif choice == "9":

            print("\n========== ISSUE BOOK ==========")

            try:
                book_id = int(input("Enter book ID: "))

            except ValueError:
                print("Invalid book ID. Please enter a number.")
                continue

            book = db.get_book(book_id)

            if not book:

                print("Book not found.")
                continue

            print("\nBook found:")
            print(book)

            if book.available_quantity <= 0:

                print("Book is not available.")
                continue

            try:
                member_id = int(input("Enter member ID: "))

            except ValueError:
                print("Invalid member ID. Please enter a number.")
                continue

            member = db.get_member(member_id)

            if not member:

                print("Member not found.")
                continue

            issue_date = date.today()
            return_date = None
            status = "Issued"

            issue = Issue(
                0,
                book_id,
                member_id,
                issue_date,
                return_date,
                status
            )

            print(admin.issue_book(db, issue))


        elif choice == "10":

            print("\n========== RETURN BOOK ==========")

            try:
                issue_id = int(input("Enter issue ID: "))

            except ValueError:
                print("Invalid issue ID. Please enter a number.")
                continue

            try:
                book_id = int(input("Enter book ID: "))

            except ValueError:
                print("Invalid book ID. Please enter a number.")
                continue

            return_date = date.today()

            print(
                admin.return_book(
                    db,
                    issue_id,
                    book_id,
                    return_date
                )
            )


        elif choice == "11":

            print("\n========== ISSUES ==========")

            issues = admin.view_issues(db)

            if not issues:
                print("No issue records found.")
            else:
                display_issues(issues)


        elif choice == "12":

            print("\n========== PAYMENTS ==========")

            payments = admin.view_payments(db)

            if not payments:
                print("No payment records found.")
            else:
                display_payments(payments)


        elif choice == "13":

            print("\n========== CREATE DUE ==========")

            try:
                issue_id = int(input("Enter issue ID: "))

            except ValueError:
                print("Invalid issue ID. Please enter a number.")
                continue

            issue = db.get_issue(issue_id)

            if not issue:

                print("Issue not found.")
                continue

            if issue[5] != "Issued":

                print("Due can only be created for an issued book.")
                continue

            member_id = issue[2]

            print(f"Member ID: {member_id}")

            try:
                amount = float(input("Enter due amount: "))

            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            if amount <= 0:
                print("Due amount must be greater than 0.")
                continue

            payment_date = None
            status = "Unpaid"

            payment = Payment(
                0,
                issue_id,
                member_id,
                amount,
                payment_date,
                status
            )

            print(admin.add_payment(db, payment))

        else:

            print("Invalid choice. Please try again.")

main_menu()
db.close()