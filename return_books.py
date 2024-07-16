from backup import backup_books, backup_borrow

def return_books(books, borrowed_history):
    returner = input("Enter your name: ").strip()
    found = False
    for idx, entry in enumerate(borrowed_history):
        if returner.lower() in entry["borrower"].lower() and entry['status'] == 'Not Returned':
            found = True
            print(f'{idx+1}. {entry['title']}')
    if not found:
        print('\nYou have no book to return.')
    else:
        option = int(input("Enter the number of book you want to return: ").strip())
        title = borrowed_history[option-1]['title']
        for book in books:
            if book['title'] == title:
                book['quantity'] += 1
                break
        borrowed_history[option-1]['status'] = 'Returned'
        backup_borrow(borrowed_history)
        backup_books(books)
        print("\nThe book has been returned.")

