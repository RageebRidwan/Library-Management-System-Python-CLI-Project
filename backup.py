def backup_books(books):
    with open("books_data.csv", "wt") as b:
        for book in books:
            line = f'{book['title']},{book['authors']},{book['isbn']},{book['year']},{book['price']},{book['quantity']}\n'
            b.write(line)

def backup_borrow(borrowed_history):
    with open("borrow_data.csv",'wt') as bp:
        for entry in borrowed_history:
            line = f'{entry['title']},{entry['lender']},{entry['borrower']},{entry['status']}\n'
            bp.write(line)

