# Book Class Project


class BookProfile:
    # blueprint that stores simple information about books
    def __init__(self, book_title, book_author):
        self.title = book_title
        self.author = book_author

    # function to print out the details nicely
    def display_info(self):
        print(f"Book Title: {self.title}")
        print(f"Written By: {self.author}")


# Creating Unique Objects

# Object 1: Storing details for a Python programming book
book_1 = BookProfile("Why I am an atheist", "Bhagat Singh")

# Object 2: Storing details for a simple story book
book_2 = BookProfile("The Diary of a Young Girl", "Anne Frank")


#Running the Functions
print("--- Scanning Library Books ---")
book_1.display_info()

print()  # Just prints an empty line for spacing

book_2.display_info()
