def search(books):
    key = input("Enter title/isbn to search: ").strip()
    found = False
    for book in books:
        if key.lower() in book['title'].lower() or key in book['isbn']:
            print(f'\n{book['title']} - {book['quantity']}')
            found = True
    if not found:
        print("\nNo such item.")
