def search_authors(books):
    n = input("\nEnter author name: ").strip()
    found = False
    for book in books:
        for name in book["authors"]:
            if n.lower() in name.lower():
                author_names = ", ".join(book["authors"])
                print(f"{book['title']} | {author_names}")
                found = True
                break
    if not found:
        print(f"No author named {n}")
