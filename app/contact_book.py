
from app.contact import Contact
from app.storage import Storage

class ContactBook:
    def __init__(self):
        self.storage = Storage()
        self.contacts = []

        data = self.storage.load_all()
        for item in data:
            self.contacts.append(Contact(item["name"], item["phone"], item["email"]))

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        self.storage.save_all(self.contacts)
        print(f"{name} kontakt qo‘shildi!")

    def show_all(self):
        if not self.contacts:
            print("Kontaktlar yo‘q!")
        else:
            print("\n--- Barcha kontaktlar ---")
            for c in self.contacts:
                c.show_info()

    def search_contact(self, name):
        name = name.strip().lower()
        results = [c for c in self.contacts if name in c.name.lower()]

        if results:
            print("\nTopildi:")
            for c in results:
                c.show_info()
        else:
            print("Kontakt topilmadi!")

    def delete_contact(self, name):
        name = name.strip().lower()
        for c in self.contacts:
            if c.name.lower() == name:
                self.contacts.remove(c)
                self.storage.save_all(self.contacts)
                print(f"{c.name} o‘chirildi!")
                return
        print("Bunday kontakt yo‘q")
