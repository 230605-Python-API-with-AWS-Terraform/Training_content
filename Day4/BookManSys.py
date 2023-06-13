from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, author, year):
        self._title = title
        self._author = author
        self._year = year

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    @abstractmethod
    def additional_info(self):
        pass


class FictionBook(Book):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self._genre = genre

    def additional_info(self):
        return f"Genre: {self._genre}"


class NonFictionBook(Book):
    def __init__(self, title, author, year, topic):
        super().__init__(title, author, year)
        self._topic = topic

    def additional_info(self):
        return f"Topic: {self._topic}"


class BookManagementSystem:
    def __init__(self):
        self._books = []

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        year = input("Enter the publication year of the book: ")
        book_type = input("Enter the type of book (fiction/non-fiction): ")

        if book_type.lower() == "fiction":
            genre = input("Enter the genre of the fiction book: ")
            book = FictionBook(title, author, year, genre)
        elif book_type.lower() == "non-fiction":
            topic = input("Enter the topic of the non-fiction book: ")
            book = NonFictionBook(title, author, year, topic)
        else:
            print("Invalid book type.")
            return

        self._books.append(book)
        print("Book added successfully!")

    def display_books(self):
        if len(self._books) == 0:
            print("No books available.")
        else:
            print("List of books:")
            for i, book in enumerate(self._books, start=1):
                print(f"{i}. {book.title} by {book.author} ({book.year})")
                print(book.additional_info())
                print()

    def search_book(self):
        title = input("Enter the title of the book to search: ")
        found_books = []
        for book in self._books:
            if book.title.lower() == title.lower():
                found_books.append(book)

        if len(found_books) == 0:
            print("No matching books found.")
        else:
            print("Matching books:")
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")
                print(book.additional_info())
                print()

    def delete_book(self):
        title = input("Enter the title of the book to delete: ")
        found_books = []
        for book in self._books:
            if book.title.lower() == title.lower():
                found_books.append(book)

        if len(found_books) == 0:
            print("No matching books found.")
        else:
            print("Matching books:")
            for i, book in enumerate(found_books, start=1):
                print(f"{i}. {book.title} by {book.author} ({book.year})")
                print(book.additional_info())
                print()

            choice = input("Enter the number of the book to delete: ")
            try:
                choice = int(choice)
                if choice >= 1 and choice <= len(found_books):
                    book_to_delete = found_books[choice - 1]
                    self._books.remove(book_to_delete)
                    print("Book deleted successfully!")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid choice.")


# Interface (optional)
class BookInterface:
    def add_book(self):
        pass

    def display_books(self):
        pass

    def search_book(self):
        pass

    def delete_book(self):
        pass


# Implementation of the interface
class BookManagementSystemWithInterface(BookInterface, BookManagementSystem):
    pass


# Menu-driven interface
book_system = BookManagementSystemWithInterface()

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
