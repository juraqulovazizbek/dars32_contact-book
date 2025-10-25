from app.commands import Command


def main() -> None:

    command = Command()
    
    while True:
        print(
            "1 Add new contact\n"
            "2 Show all contacts\n"
            "3 Search contact by name\n"
            "4 Update contact"
            "5 Delete contact"
        )

        choice = input("> ")
        if choice == '1':
            command.add_contact()

        elif choice == '2':
            command.show_all()

        elif choice == '3':
            command.search_contact()

        elif choice == '4':
            command.update_contact()

main()
