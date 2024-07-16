from backup import backup_books

def remove(books):
    name = input("Enter the name of book you want to remove: ").strip()
    found = False
    for sl, book in enumerate(books):
        if name.lower() in book['title'].lower():
            print(f'{sl+1}. {book['title']} ')
            found = True
    if not found:
        print("\nNo such book found.")
    else:
        option = int(input("\nChoose the number you want to remove: "))
        books.pop(option-1)
        backup_books(books)
        print("\nRemoved successfully.")
