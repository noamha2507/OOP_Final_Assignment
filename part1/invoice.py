class Invoice:
    # בניית האובייקט ואתחול המשתנים
    def __init__(self, invoice_number, customer_name, amount, date, description):
        # שימוש ב-Setters להפעלת הבדיקות בעת היצירה
        self.invoice_number = invoice_number
        self.customer_name = customer_name
        self.amount = amount
        self.date = date
        self.description = description

    # הגדרת Property למספר החשבונית
    @property
    def invoice_number(self):
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, value):
        # בדיקה שהמספר חיובי
        if value > 0:
            self._invoice_number = value
        else:
            self._invoice_number = 1000 # ערך דיפולטיבי אם הקלט שגוי
            print("Invalid Invoice Number, set to default 1000")

    # הגדרת Property לשם הלקוח
    @property
    def customer_name(self):
        return self._customer_name
    
    @customer_name.setter
    def customer_name(self, value):
        # בדיקה שהשם לא ריק
        if len(value) > 0:
            self._customer_name = value
        else:
            self._customer_name = "Guest"
            print("Invalid Name, set to default 'Guest'")

    # הגדרת Property לסכום
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        # בדיקה שהסכום לא שלילי
        if value >= 0:
            self._amount = value
        else:
            self._amount = 0
            print("Invalid Amount, set to 0")

    # משתנים ללא בדיקות מיוחדות
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        self._date = value

    @property
    def description(self):
        return self._description
        
    @description.setter
    def description(self, value):
        self._description = value

    # חישוב המע"מ
    def calculate_vat(self):
        return self._amount * 0.17

    # הדפסת פרטי החשבונית
    def print_details(self):
        print("\n--- Invoice Details ---")
        print(f"Invoice Number: {self.invoice_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Description: {self.description}")
        print(f"Date: {self.date}")
        vat = self.calculate_vat()
        print(f"Amount before VAT: {self.amount}")
        print(f"VAT Amount: {vat:.2f}")
        print(f"Total to Pay: {self.amount + vat:.2f}")
        print("-----------------------")

# התוכנית הראשית
def main():
    print("Creating a new Invoice")
    
    # קליטת נתונים מהמשתמש
    inv_num = int(input("Enter Invoice Number: "))
    name = input("Enter Customer Name: ")
    amount = float(input("Enter Amount: "))
    date = input("Enter Date (DD/MM/YYYY): ")
    desc = input("Enter Description: ")

    # יצירת האובייקט
    my_invoice = Invoice(inv_num, name, amount, date, desc)

    # הפעלת פונקציית ההדפסה
    my_invoice.print_details()

main()

"""
תשובה לסעיף 1.ג:
מטרת הכימוס (Encapsulation) היא לאגד נתונים ומתודות תחת יחידה אחת (מחלקה) ולהסתיר את המימוש הפנימי ואת הנתונים הרגישים מפני גישה ישירה מבחוץ.
התוצאה היא הגנה על המידע (Data Integrity) ושליטה על האופן בו משתנים ערכים (למשל באמצעות Properties), מה שמונע הכנסת נתונים שגויים ומקל על תחזוקת הקוד.
"""