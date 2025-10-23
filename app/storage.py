import json

from app.contact import Contact


class Storage:

    def __init__(self):
        self.filename = "database/contacts.json"

    def save(self, contact: Contact):
        contact_dict = contact.to_dict()

        with open(self.filename, "w") as f:
            json.dump(contact_dict, f, indent=4)
