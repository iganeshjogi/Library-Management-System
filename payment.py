class Payment:

    def __init__(
        self,
        payment_id,
        issue_id,
        member_id,
        amount,
        payment_date,
        status
    ):
        self.payment_id = payment_id
        self.issue_id = issue_id
        self.member_id = member_id
        self.amount = amount
        self.payment_date = payment_date
        self.status = status


    def to_tuple(self):

        return (
            self.issue_id,
            self.member_id,
            self.amount,
            self.payment_date,
            self.status
        )