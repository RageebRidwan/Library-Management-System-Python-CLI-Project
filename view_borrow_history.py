def view_borrow_history(borrowed_history):
    if not borrowed_history:
        print("\nNothing to show yet.")
    else:
        print("")
        for entry in borrowed_history:
            print(
                f'{entry["title"]} | Lender : {entry["lender"]} | Borrower : {entry["borrower"]} | Status : {entry['status']}'
            )
