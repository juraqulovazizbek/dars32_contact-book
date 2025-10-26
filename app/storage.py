import json
import os
import sys
class Storage:
    def __init__(self):
        self.filename = "contacts.json" 

    def save_all(self, contacts):
        data = []
        for c in contacts:
            data.append({
                "name": c.name,
                "phone": c.phone,
                "email": c.email
            })

        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_all(self):
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as f:
            data = json.load(f)

        return data