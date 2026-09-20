class Admin:

    def __init__(self, admin_id, username, password):

        self.admin_id = admin_id
        self.username = username
        self.password = password


    def view_books(self, db):

        return db.get_all_books()


    def view_members(self, db):

        return db.get_all_members()


    def view_issues(self, db):

        return db.get_all_issues()


    def view_payments(self, db):

        return db.get_all_payments()


    def add_book(self, db, book):

        try:
            book_id = db.add_book(book)

            return f"Book added successfully. Book ID: {book_id}"

        except Exception as e:
            return f"Error adding book: {e}"


    def add_member(self, db, member):

        try:
            member_id = db.add_member(member)

            return f"Member added successfully. Member ID: {member_id}"

        except Exception as e:
            return f"Error adding member: {e}"


    def update_book(self, db, book):

        try:
            result = db.update_book(book)

            if result == 0:
                return "Book not found."

            return "Book updated successfully."

        except Exception as e:
            return f"Error updating book: {e}"


    def update_member(self, db, member):

        try:
            result = db.update_member(member)

            if result == 0:
                return "Member not found."

            return "Member updated successfully."

        except Exception as e:
            return f"Error updating member: {e}"


    def delete_book(self, db, book_id):

        try:
            result = db.delete_book(book_id)

            if result == 0:
                return "Book not found."

            return "Book deleted successfully."

        except Exception as e:
            return f"Error deleting book: {e}"


    def delete_member(self, db, member_id):

        try:
            result = db.delete_member(member_id)

            if result == 0:
                return "Member not found."

            return "Member deleted successfully."

        except Exception as e:
            return f"Error deleting member: {e}"


    def issue_book(self, db, issue):

        try:
            result = db.issue_book(issue)

            if isinstance(result, str):
                return result

            return f"Book issued successfully. Issue ID: {result}"

        except Exception as e:
            return f"Error issuing book: {e}"


    def return_book(self, db, issue_id, book_id, return_date):

        try:

            issue = db.get_issue(issue_id)

            if not issue:
                return "Issue not found."

            if issue[1] != book_id:
                return "Book ID does not match the issue."

            if issue[5] != "Issued":
                return "Book is already returned."

            member_id = issue[2]

            result = db.return_book(
                issue_id,
                book_id,
                member_id,
                return_date
            )

            return result

        except Exception as e:
            return f"Error returning book: {e}"


    def add_payment(self, db, payment):

        try:
            payment_id = db.add_payment(payment)

            return f"Due created successfully. Payment ID: {payment_id}"

        except Exception as e:
            return f"Error creating due: {e}"