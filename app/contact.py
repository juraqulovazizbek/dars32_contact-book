class Contact:

    def __init__(self, name: str, phone: str, email: str) -> None:
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }
    
    def show_info(self):
        print(f"Ism: {self.name}, Tel: {self.phone}, Email: {self.email} ")