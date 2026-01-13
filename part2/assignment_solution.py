# פתרון מטלה - תכנות מונחה עצמים (OOP)
# סעיף 2: הורשה

# מחלקת הבסיס - נייר ערך (Security)
class Security:
    def __init__(self, name, symbol, price):
        self.name = name          # שם נייר הערך
        self.symbol = symbol      # סימול (לדוגמה: AAPL)
        self.price = float(price) # מחיר נוכחי

    # מתודה להדפסת פרטים בסיסיים
    def show_info(self):
        print(f"--- Info for {self.symbol} ---")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")

# מחלקה יורשת 1 - מניה (Stock)
class Stock(Security):
    def __init__(self, name, symbol, price, dividend_yield):
        super().__init__(name, symbol, price) # קריאה לבנאי של מחלקת האב
        self.dividend_yield = float(dividend_yield) # תשואת דיבידנד

    # מתודה ייחודית למניה: חישוב דיבידנד צפוי
    def print_dividend_info(self):
        amount = self.price * (self.dividend_yield / 100)
        print(f"Expected Dividend: {amount:.2f}")

# מחלקה יורשת 2 - אג"ח (Bond)
class Bond(Security):
    def __init__(self, name, symbol, price, interest_rate):
        super().__init__(name, symbol, price)
        self.interest_rate = float(interest_rate) # ריבית שנתית

    # מתודה ייחודית לאג"ח: חישוב שווי לפדיון (פשטני - שנה אחת)
    def calculate_maturity_value(self):
        final_value = self.price * (1 + self.interest_rate / 100)
        print(f"Value after 1 year: {final_value:.2f}")

# מחלקה יורשת 3 - אופציה (Option)
class Option(Security):
    def __init__(self, name, symbol, price, expiration_date):
        super().__init__(name, symbol, price)
        self.expiration_date = expiration_date # תאריך פקיעה (מחרוזת)

    # מתודה ייחודית לאופציה: הצגת תוקף
    def show_expiry(self):
        print(f"Option expires on: {self.expiration_date}")


# --- תוכנית ראשית (Main) ---
# חלק זה קולט נתונים מהמשתמש ויוצר עצמים

print("Creating Stock (Manya)...")
s_name = input("Enter Stock Name: ")
s_symbol = input("Enter Stock Symbol: ")
s_price = input("Enter Price: ")
s_div = input("Enter Dividend Yield (%): ")
# יצירת מופע של מניה
stock1 = Stock(s_name, s_symbol, s_price, s_div)

print("\nCreating Bond (Agah)...")
b_name = input("Enter Bond Name: ")
b_symbol = input("Enter Bond Symbol: ")
b_price = input("Enter Price: ")
b_rate = input("Enter Interest Rate (%): ")
# יצירת מופע של אג"ח
bond1 = Bond(b_name, b_symbol, b_price, b_rate)

print("\nCreating Option (Optzia)...")
o_name = input("Enter Option Name: ")
o_symbol = input("Enter Option Symbol: ")
o_price = input("Enter Price: ")
o_date = input("Enter Expiration Date: ")
# יצירת מופע של אופציה
option1 = Option(o_name, o_symbol, o_price, o_date)

# --- קריאה למתודות ---
print("\n--- Results ---")

# שימוש בפולימורפיזם או קריאה ישירה - נשתמש בקריאה ישירה הכי פשוטה
print("Stock Details:")
stock1.show_info()           # מתודה ממחלקת האב
stock1.print_dividend_info() # מתודה ממחלקת הבן

print("\nBond Details:")
bond1.show_info()
bond1.calculate_maturity_value()

print("\nOption Details:")
option1.show_info()
option1.show_expiry()


# סעיף ד': מהי מטרת ההורשה ומהי תוצאתה?
# תשובה:
# המטרה של הורשה היא בעיקר לחסוך בכתיבה חוזרת של קוד ולעשות סדר.
# במקום להעתיק את אותן תכונות לכל מחלקה מחדש, אנחנו מגדירים אותן פעם אחת במחלקה כללית (האבא).
# התוצאה היא שמחלקות אחרות (הילדים) מקבלות אוטומטית את כל מה שיש במחלקה הכללית,
# ויכולות להוסיף עליה דברים משלהן.
