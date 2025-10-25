from typing import List

from app.contact import Contact
from app.storage import Storage


class ContactBook:

    def __init__(self):
        self.storage = Storage()
    
    def add_contact(self, contact: Contact):
        contact_dict = contact.to_dict()
        self.storage.add_contact(contact_dict)

    def get_contacts(self) -> List[Contact]:
        contacts = []
        for contact in self.storage.get_contacts():
            contacts.append(Contact(
                id=contact['id'],
                name=contact['name'],
                phone=contact['phone'],
                email=contact['email'],
            ))

        return contacts

    def get_conatct_by_name(self, search: str) -> List[Contact]:
        contacts = []
        for contact in self.storage.get_contacts():
            if search.lower() in contact['name'].lower():
                contacts.append(Contact(
                    id=contact['id'],
                    name=contact['name'],
                    phone=contact['phone'],
                    email=contact['email'],
                ))

        return contacts

    def update_contact(self, contact: Contact) -> Contact:
        contacts = self.storage.get_contacts()
        for i, item in enumerate(contacts):
            if item['id'] == contact.id:
                contacts[i] = contact.to_dict()

        self.storage.save_contacts(contacts)

    def delete_contact(self, id: str) -> None:
        pass

    def get_contact(self, id: str) -> None | Contact:
        for contact in self.storage.get_contacts():
            if contact['id'] == id:
                return Contact(
                    id=contact['id'],
                    name=contact['name'],
                    phone=contact['phone'],
                    email=contact['email'],
                )
            