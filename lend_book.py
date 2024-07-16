from backup import backup_books, backup_borrow

def lend_book(books,borrowed_history):
    lender = input("Your name: ").strip()
    borrower = input("Name of the person you want to lend to: ").strip()

    name = input(f"Enter the name of the book you want to lend {borrower}: ").strip()
    found = False
    for sl, book in enumerate(books):
        if name.lower() in book['title'].lower():
            print(f'{sl+1}. {book['title']} ')
            found = True
    if not found:
        print("\nNo such book found.")
    else:
        option = int(input("\nChoose the number you want to lend: "))
        q = books[option-1]['quantity']
        if q > 0 :
            books[option-1]['quantity'] -= 1
            entry = {
                'title':books[option-1]['title'],
                'lender' : lender,
                'borrower':borrower,
                'status': "Not Returned"

            }
            borrowed_history.append(entry)
            backup_borrow(borrowed_history)
            backup_books(books)

            print(f"\nBook lent to {borrower} successfully.")
        else:
            print("\nNot enough book to lend.")
