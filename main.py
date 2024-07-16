from add_books import add_books
from view_books import view_books
from search import search
from search_authors import search_authors
from remove import remove
from lend_book import lend_book
from return_books import return_books
from view_borrow_history import view_borrow_history


def main():
    books = []
    borrowed_history = []
    text = """
Choose Your Options:
1. Add a book
2. View the books
3. Search
4. Search by author
5. Remove a book
6. Lend a book
7. Return a book
8. View borrow history
0. Exit
    """
    while True:
        print(text)
        option = input("Enter your option: ").strip()
        if option == "1":
            add_books(books)
            print("\nNew book has been added.")
        elif option == "2":
            if not books:
                print("\nNo book to show.")
            else:
                view_books(books)
        elif option == "3":
            search(books)
        elif option == "4":
            search_authors(books)
        elif option == "5":
            remove(books)
        elif option == "6":
            lend_book(books, borrowed_history)
        elif option == "7":
            return_books(books, borrowed_history)
        elif option == "8":
            view_borrow_history(borrowed_history)
        elif option == "0":
            print("\nGoodbye.")
            break


if __name__ == "__main__":
    main()
