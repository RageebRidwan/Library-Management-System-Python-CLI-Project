def view_books(books):
    print("")
    for book in books:
        authors = ", ".join(book["authors"])

        print(
            book["title"],
            authors,
            book["isbn"],
            book["year"],
            book["price"],
            book["quantity"],
            sep=" | ",
        )
