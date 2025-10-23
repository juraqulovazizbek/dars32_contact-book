
# 📒 Contact Book (Python OOP Project)

## 📖 Overview
**Contact Book** — bu Python’da **Object-Oriented Programming (OOP)** tamoyillari asosida yozilgan kichik loyiha bo‘lib, foydalanuvchiga kontaktlarni boshqarish imkonini beradi.  
Loyiha OOP’ni (class, inheritance, encapsulation, polymorphism) amaliy tarzda o‘rganish uchun juda qulay.

---

## 🏗 Project Structure

```

contact-book/
│
├── app/
│   ├── **init**.py
│   ├── contact.py
│   ├── contact_book.py
│   └── storage.py
│
├── main.py
└── README.md

````

---

## 🧠 OOP Concepts Used
- **Encapsulation** – kontakt ma’lumotlari xususiy atributlarda saqlanadi  
- **Abstraction** – foydalanuvchiga faqat kerakli metodlar taqdim etiladi  
- **Inheritance** – kerak bo‘lsa boshqa klasslar bilan kengaytirish mumkin  
- **Polymorphism** – bir xil metod nomlari turlicha ishlaydi (`display()` va h.k.)

---

## ⚙️ Features
✅ Add new contact  
✅ Show all contacts  
✅ Search contact by name  
✅ Update or delete contact  
✅ Save and load contacts (optional)

---

## 💻 Example Usage
```python
from app.contact_book import ContactBook

book = ContactBook()

book.add_contact("Ali", "+998901112233", "ali@example.com")
book.add_contact("Madina", "+998903334455", "madina@mail.com")

book.show_all()

book.search_contact("Ali")
book.delete_contact("Madina")
book.show_all()
````

---

---

## 🚀 Future Improvements

* Save/load contacts from JSON or CSV file
* CLI or GUI version (Typer / Tkinter)
* Add sorting and filtering
* Export contacts

---

## 🧑‍💻 Author

**Diyorbek Jumanov**
Python Backend Developer | OOP Trainer

📧 Email: [diyorbek@example.com](mailto:diyorbek@example.com)
🐙 GitHub: [github.com/diyorbek](https://github.com/diyorbek)

---

## 🏁 License

MIT License — open for learning and educational use.
