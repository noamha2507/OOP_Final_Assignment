from dataclasses import dataclass

# מחלקה של אדם - משתמש ב-dataclass כדי שיהיה נוח
@dataclass
class Person:
    name: str       # השם של האדם
    address: str    # הכתובת שלו
    phone: str      # הטלפון שלו
