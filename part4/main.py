def check_multiple(n1, n2):
    """
    בודקת האם אחד מהמספרים הוא כפולה של השני.
    מחזירה אמת אם כן, ושקר אחרת.
    """
    # 0 הוא כפולה של כל מספר (למעט חלוקה ב-0)
    if n1 == 0 or n2 == 0:
        return True 

    # בדיקה האם n1 מתחלק ב-n2
    if n2 != 0 and n1 % n2 == 0:
        return True
    
    # בדיקה האם n2 מתחלק ב-n1
    if n1 != 0 and n2 % n1 == 0:
        return True
        
    return False

def main():
    print("Welcome! Enter pairs of numbers. To exit enter -1.")
    
    while True:
        try:
            # קלט ראשון
            s1 = input("Enter first number: ")
            val1 = int(s1)
            
            # יציאה אם נקלט -1
            if val1 == -1:
                print("Program ended. Goodbye!")
                break
                
            # קלט שני
            s2 = input("Enter second number: ")
            val2 = int(s2)
            
            # יציאה אם נקלט -1 גם במספר השני
            if val2 == -1:
                print("Program ended. Goodbye!")
                break
            
            # בדיקה והדפסה
            if check_multiple(val1, val2):
                print(f"Yes, one of the numbers is a multiple of the other.")
            else:
                print(f"No, the numbers are not multiples of each other.")
                
        except ValueError:
            print("Invalid input. Please enter integers.")
            
if __name__ == "__main__":
    main()
