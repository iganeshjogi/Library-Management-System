class Member:

    def __init__(
        self,
        member_id,
        name,
        email,
        phone,
        password
    ):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password


    def to_tuple(self):

        return (
            self.name,
            self.email,
            self.phone,
            self.password
        )
    

    def view_books(self, db):

        return db.get_all_books()


    def view_my_issues(self, db):

        return db.get_member_issues(self.member_id)


    def view_my_payments(self, db):

        return db.get_member_payments(self.member_id)


    def pay_due(self, db, payment_id, payment_date):

        try:
            result = db.pay_due(
                payment_id,
                self.member_id,
                payment_date
            )

            if result == 0:
                return "Payment not found or already paid."

            return "Payment completed successfully."

        except Exception as e:
            return f"Error processing payment: {e}"


    def __str__(self):

        return (
            f"Member ID: {self.member_id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone}"
        )