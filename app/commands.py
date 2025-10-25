from app.contact_book import ContactBook
from app.contact import Contact
from app.utils import (
    validate_name,
    validate_phone,
    validate_email
)


class Command:
    
    def __init__(self):
        self.book = ContactBook()

    def add_contact(self):
        name = input("name: ")
        if not validate_name(name):
            raise ValueError("Name Xato kiritildi.")
        
        phone = input("phone: ")
        if not validate_phone(phone):
            raise ValueError("Phone Xato kiritildi.")
        
        email = input("email: ")
        if not validate_email(email):
            raise ValueError("Email Xato kiritildi.")

        contact = Contact(name, phone, email)
        self.book.add_contact(contact)

    def show_all(self):
        contacts = self.book.get_contacts()
        self.print_contacts(contacts)
        
    def print_contacts(self, contacts):
        for contact in contacts:
            print(contact.id, contact.name, contact.phone, contact.email)

    def search_contact(self):
        search = input("Search by name: ")

        contacts = self.book.get_conatct_by_name(search)
        self.print_contacts(contacts)
    
    def update_contact(self):
        self.show_all()

        id = input("ID: ")
        contact = self.book.get_contact(id)

        if contact is None:
            raise ValueError("Bunday id mavjud emas.")

        name = input("name: ")
        if not validate_name(name):
            raise ValueError("Name Xato kiritildi.")
        
        contact.name = name

        self.book.update_contact(contact)