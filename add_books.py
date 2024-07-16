from backup import backup_books


def add_books(books):
    title = input("\nEnter book title: ").strip()
    authors = list(
        map(
            lambda x: x.strip(),
            input("Enter name/s of authors(use comma to separate): ").split(","),
        )
    )
    isbn = input("Enter ISBN number: ").strip()
    pub_year = int(input("Enter publishing year: ").strip())
    price = f'${float(input("Enter price: ").strip())}'
    quantity = int(input("Enter quantity: ").strip())

    book = {
        "title": title,
        "authors": authors,
        "isbn": isbn,
        "year": pub_year,
        "price": price,
        "quantity": quantity,
    }
    books.append(book)
    backup_books(books)
