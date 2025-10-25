from uuid import uuid1, UUID
from typing import Optional


class Contact:

    def __init__(self, name: str, phone: str, email: str, id: Optional[UUID] = None) -> None:
        self.id = id or uuid1()
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }
