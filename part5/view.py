from typing import Tuple, List
from Person import Person

# מחלקה שאחראית על כל ההדפסות והקלט מהמשתמש
class View:

    def show_menu(self) -> None:
        # מדפיס את התפריט הראשי
        print("\n--- Main Menu ---")
        print("1. Add new person")
        print("2. Display all people")
        print("3. Exit")

    def get_user_choice(self) -> str:
        # קולט את הבחירה של המשתמש
        return input("Select an option: ")

    def get_person_details(self) -> Tuple[str, str, str]:
        # מבקש מהמשתמש את כל הפרטים של האדם החדש
        print("\n--- Add Person ---")
        name = input("Enter name: ")
        address = input("Enter address: ")
        phone = input("Enter phone number: ")
        return name, address, phone

    def show_person(self, person: Person) -> None:
        # מדפיס אדם אחד בצורה מסודרת
        print(f"Name: {person.name}, Address: {person.address}, Phone: {person.phone}")

    def show_all_people(self, people: List[Person]) -> None:
        # עובר על כל הרשימה ומדפיס את כולם
        print("\n--- People List ---")
        if not people:
            print("The list is currently empty.")
        else:
            for person in people:
                self.show_person(person)

    def show_message(self, message: str) -> None:
        # מדפיס הודעה כללית (כמו הצלחה או שגיאה)
        print(message)
