import json
from typing import List


class Storage:

    def __init__(self):
        self.filename = "database/contacts.json"

    def add_contact(self, contact: dict):
        contacts = self.get_contacts()
        contacts.append(contact)
        self.save_contacts(contacts)

    def save_contacts(self, contacts: List[dict]):
        with open(self.filename, "w") as f:
            json.dump(contacts, f, indent=4)

    def get_contacts(self) -> List[dict]:
        with open(self.filename) as f:
            return json.load(f)
