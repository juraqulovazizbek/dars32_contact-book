
from app.contact_book import ContactBook


def main() -> None:

    book = ContactBook()
    
    while True:
        print(
            "1 Add new contact\n"
            "2 Show all contacts\n"
            "3 Search contact by name\n"
            "4 Update or delete contact\n"
            "5. Exit"
        )


        choice = input("> ")
        if choice == '1':
            name = input("name: ").capitalize
            phone = input("phone (faqar raqamlardan  IBORAT  bo'lsin.!) : ").isdigit

            email = input("email: ")

            book.add_contact(name, phone, email)

        elif choice == '2':
            book.show_all()
        elif choice == "3":
            name = input("Qidiriladigan ism: ")
            book.search_contact(name)
        elif choice == "4":
            name = input("O'chiriladigan ism: ")
            book.delete_contact(name)
        elif choice == "5":
            print("Dastur tugadi.")
            break
        else:
            print("Noto'g'ri tanlov")
main()