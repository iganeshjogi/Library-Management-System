class Book:

    def __init__(
        self,
        book_id,
        title,
        author,
        category,
        quantity,
        available_quantity
    ):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.quantity = quantity
        self.available_quantity = available_quantity


    def to_tuple(self):

        return (
            self.title,
            self.author,
            self.category,
            self.quantity,
            self.available_quantity
        )

    def __str__(self):

        return (
            f"Book ID: {self.book_id}\n"
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Category: {self.category}\n"
            f"Quantity: {self.quantity}\n"
            f"Available Quantity: {self.available_quantity}"
    )