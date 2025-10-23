from app.contact import Contact
from app.storage import Storage


class ContactBook:

    def __init__(self):
        self.storage = Storage()
    
    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.storage.save(contact)

    def show_all(self):
        pass
