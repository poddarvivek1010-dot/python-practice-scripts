#  Library Book Tracker


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f"Checked out: '{self.title}' by {self.author}")
        else:
            print(f"Sorry!, '{self.title}' is already borrowed.")

    def return_book(self):
        self.is_available = True
        print(f"Returned: '{self.title}'")


# Creating objects
book_1 = Book("Python basics", "John Smith")
book_2 = Book("Clean code", "Robert Martin")
book_3 = Book("Data structures", "Sara Khan")

# Testing the Library Actions
print(" Library Status....")
book_1.check_out()
book_1.check_out()  # Trying to borrow it again
book_2.check_out()
book_3.check_out()

print()  # Clean spacing

book_1.return_book()
book_1.check_out()  # Now available again
