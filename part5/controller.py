from model import Model
from view import View

# המחלקה שמנהלת את הכל ומחברת בין המודל לתצוגה
class Controller:
    def __init__(self):
        # יוצרים מופע של המודל והתצוגה
        self.model = Model()
        self.view = View()

    def run(self) -> None:
        # הלולאה הראשית של התוכנית
        running = True
        while running:
            self.view.show_menu()
            choice = self.view.get_user_choice()

            if choice == '1':
                # הוספת אדם חדש
                name, address, phone = self.view.get_person_details()
                self.model.add(name, address, phone)
                self.view.show_message("Person added successfully!")

            elif choice == '2':
                # הצגת כל הרשימה
                all_people = self.model.get_all()
                self.view.show_all_people(all_people)

            elif choice == '3':
                # יציאה
                self.view.show_message("Thank you for using the system, goodbye!")
                running = False

            else:
                self.view.show_message("Error: Invalid choice, please try again.")
