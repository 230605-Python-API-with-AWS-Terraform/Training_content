class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class BookManagementSystem:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        year = input("Enter the publication year of the book: ")
        book = Book(title, author, year)
        self.books.append(book)
        print("Book added successfully!")

    def display_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("List of books:")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. Title: {book.title}, Author: {book.author}, Year: {book.year}")

    def search_book(self):
        title = input("Enter the title of the book to search: ")
        found_books = []
        for book in self.books:
            if book.title.lower() == title.lower():
                found_books.append(book)
        
        if len(found_books) == 0:
            print("No matching books found.")
        else:
            print("Matching books:")
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")

    def delete_book(self):
        title = input("Enter the title of the book to delete: ")
        found_books = []
        for book in self.books:
            if book.title.lower() == title.lower():
                found_books.append(book)
        
        if len(found_books) == 0:
            print("No matching books found.")
        else:
            print("Matching books:")
            for i, book in enumerate(found_books, start=1):
                print(f"{i}. Title: {book.title}, Author: {book.author}, Year: {book.year}")
            
            choice = input("Enter the number of the book to delete: ")
            try:
                choice = int(choice)
                if choice >= 1 and choice <= len(found_books):
                    book_to_delete = found_books[choice - 1]
                    self.books.remove(book_to_delete)
                    print("Book deleted successfully!")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid choice.")

# Menu-driven interface
book_system = BookManagementSystem()

while True:
    print("\n*** Book Management System ***")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        book_system.add_book()
    elif choice == "2":
        book_system.display_books()
    elif choice == "3":
        book_system.search_book()
    elif choice == "4":
        book_system.delete_book()
    elif choice == "5":
        print("Thank you for using the Book Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
