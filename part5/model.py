from typing import List
from Person import Person

# המחלקה שאחראית על הנתונים
class Model:
    def __init__(self):
        # רשימה ריקה שתשמור את האנשים
        self.people_list: List[Person] = []

    def add(self, name: str, address: str, phone: str) -> None:
        # יוצר אובייקט חדש ומוסיף לרשימה
        new_person = Person(name, address, phone)
        self.people_list.append(new_person)

    def get_all(self) -> List[Person]:
        # מחזיר את כל הרשימה (בשביל להציג אותה אחר כך)
        return self.people_list
