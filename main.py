from app.contact_book import ContactBook


def main() -> None:

    book = ContactBook()
    
    while True:
        print(
            "1 Add new contact\n"
            "2 Show all contacts\n"
            "3 Search contact by name\n"
            "4 Update or delete contact"
        )

        choice = input("> ")
        if choice == '1':
            name = input("name: ")
            phone = input("phone: ")
            email = input("email: ")

            book.add_contact(name, phone, email)

        elif choice == '2':
            book.show_all()

main()
