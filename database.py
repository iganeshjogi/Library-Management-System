import mysql.connector
from member import Member
from book import Book

class Database:

    def __init__(self):

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql_password",
            database="library_management"
        )

        self.cursor = self.conn.cursor()

        print("Database connected successfully.")


    def close(self):

        self.cursor.close()
        self.conn.close()

        print("Database connection closed.")


## BOOK OPERATIONS ##

    def add_book(self, book):

        sql = """
        INSERT INTO book
        (title, author, category, quantity, available_quantity)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = book.to_tuple()

        self.cursor.execute(sql, values)
        self.conn.commit()

        return self.cursor.lastrowid


    def get_all_books(self):

        sql = "SELECT * FROM book"

        self.cursor.execute(sql)

        rows = self.cursor.fetchall()

        books = []

        for row in rows:

            books.append(
                Book(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5]
                )
            )

        return books


    def get_book(self, book_id):

        sql = """
        SELECT * FROM book
        WHERE book_id = %s
        """

        self.cursor.execute(sql, (book_id,))

        row = self.cursor.fetchone()

        if row is None:
            return None

        return Book(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5]
        )


    def update_book(self, book):

        sql = """
        UPDATE book
        SET title = %s,
            author = %s,
            category = %s,
            quantity = %s,
            available_quantity = %s
        WHERE book_id = %s
        """

        values = (
            book.title,
            book.author,
            book.category,
            book.quantity,
            book.available_quantity,
            book.book_id
        )

        self.cursor.execute(sql, values)
        self.conn.commit()

        return self.cursor.rowcount


    def delete_book(self, book_id):

        sql = """
        DELETE FROM book
        WHERE book_id = %s
        """

        self.cursor.execute(sql, (book_id,))
        self.conn.commit()

        return self.cursor.rowcount

## MEMBER OPERATIONS ##

    def add_member(self, member):

        sql = """
        INSERT INTO member
        (name, email, phone, password)
        VALUES (%s, %s, %s, %s)
        """

        values = member.to_tuple()

        self.cursor.execute(sql, values)
        self.conn.commit()

        return self.cursor.lastrowid


    def get_all_members(self):

        sql = "SELECT * FROM member"

        self.cursor.execute(sql)

        rows = self.cursor.fetchall()

        members = []

        for row in rows:

            members.append(
                Member(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4]
                )
            )

        return members


    def get_member(self, member_id):

        sql = """
        SELECT * FROM member
        WHERE member_id = %s
        """

        self.cursor.execute(sql, (member_id,))

        row = self.cursor.fetchone()

        if row is None:
            return None

        return Member(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4]
        )


    def update_member(self, member):

        sql = """
        UPDATE member
        SET name = %s,
            email = %s,
            phone = %s,
            password = %s
        WHERE member_id = %s
        """

        values = (
            member.name,
            member.email,
            member.phone,
            member.password,
            member.member_id
        )

        self.cursor.execute(sql, values)
        self.conn.commit()

        return self.cursor.rowcount


    def delete_member(self, member_id):

        sql = """
        DELETE FROM member
        WHERE member_id = %s
        """

        self.cursor.execute(sql, (member_id,))
        self.conn.commit()

        return self.cursor.rowcount


## ADMIN LOGIN ##

    def admin_login(self, username, password):

        sql = """
        SELECT * FROM admin
        WHERE username = %s AND password = %s
        """

        self.cursor.execute(sql, (username, password))

        return self.cursor.fetchone()
        

## MEMBER LOGIN ##

    def member_login(self, email, password):

        sql = """
        SELECT * FROM member
        WHERE email = %s AND password = %s
        """

        self.cursor.execute(sql, (email, password))

        return self.cursor.fetchone()


## ISSUE OPERATIONS ## 

    def issue_book(self, issue):

        book = self.get_book(issue.book_id)

        if book is None:
            return "Book not found."

        if book.available_quantity <= 0:
            return "Book is not available."

        member = self.get_member(issue.member_id)

        if member is None:
            return "Member not found."

        sql = """
        INSERT INTO issue
        (book_id, member_id, issue_date, return_date, status)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = issue.to_tuple()

        self.cursor.execute(sql, values)

        issue_id = self.cursor.lastrowid

        update_sql = """
        UPDATE book
        SET available_quantity = available_quantity - 1
        WHERE book_id = %s
        """

        self.cursor.execute(update_sql, (issue.book_id,))

        self.conn.commit()

        return issue_id


    def get_all_issues(self):

        sql = "SELECT * FROM issue"

        self.cursor.execute(sql)

        return self.cursor.fetchall()


    def get_member_issues(self, member_id):

        sql = """
        SELECT * FROM issue
        WHERE member_id = %s
        """

        self.cursor.execute(sql, (member_id,))

        return self.cursor.fetchall()

    def get_issue(self, issue_id):

        sql = """
        SELECT * FROM issue
        WHERE issue_id = %s
        """

        self.cursor.execute(sql, (issue_id,))

        return self.cursor.fetchone()


    def member_has_issues(self, member_id):

        sql = """
        SELECT COUNT(*)
        FROM issue
        WHERE member_id = %s
        """

        self.cursor.execute(sql, (member_id,))

        result = self.cursor.fetchone()

        return result[0] > 0


## RETURN BOOK ## 

    def return_book(self, issue_id, book_id, member_id, return_date):

        sql = """
        UPDATE issue
        SET return_date = %s,
            status = 'Returned'
        WHERE issue_id = %s
        AND book_id = %s
        AND member_id = %s
        AND status = 'Issued'
        """

        self.cursor.execute(
            sql,
            (return_date, issue_id, book_id, member_id)
        )

        if self.cursor.rowcount == 0:
            return "Issue not found or book already returned."

        update_sql = """
        UPDATE book
        SET available_quantity = available_quantity + 1
        WHERE book_id = %s
        """

        self.cursor.execute(update_sql, (book_id,))

        self.conn.commit()

        return "Book returned successfully."


## PAYMENT/DUE ##

    def add_payment(self, payment):

        sql = """
        INSERT INTO payment
        (issue_id, member_id, amount, payment_date, status)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = payment.to_tuple()

        self.cursor.execute(sql, values)
        self.conn.commit()

        return self.cursor.lastrowid


    def get_all_payments(self):

        sql = "SELECT * FROM payment"

        self.cursor.execute(sql)

        return self.cursor.fetchall()


    def get_member_payments(self, member_id):

        sql = """
        SELECT * FROM payment
        WHERE member_id = %s
        """

        self.cursor.execute(sql, (member_id,))

        return self.cursor.fetchall()


    def pay_due(self, payment_id, member_id, payment_date):

        sql = """
        UPDATE payment
        SET payment_date = %s,
            status = 'Paid'
        WHERE payment_id = %s
        AND member_id = %s
        AND status = 'Unpaid'
        """

        self.cursor.execute(
            sql,
            (payment_date, payment_id, member_id)
        )

        self.conn.commit()

        return self.cursor.rowcount