"""
שיעור 3: פונקציות, תנאים, וערך מוחזר
====================================

הרצה:
    uv run python lessons/03_def_if_return.py

שלוש מילות מפתח בשיעור הזה:
    def     מגדירה פונקציה, כלומר קטע קוד עם שם שאפשר להפעיל שוב ושוב
    if      מבצעת קוד רק אם תנאי מתקיים
    return  מחזירה ערך מהפונקציה לקוד שקרא לה
"""

# ======================================================================
# חלק 1: המילה def
# ======================================================================

# def פותחת הגדרה של פונקציה. אחריה השם, סוגריים, ונקודתיים.
# כל מה שמוזח פנימה שייך לפונקציה
def greet():
    print("welcome to the smart house")


# ההגדרה לבדה לא מריצה כלום. כדי להפעיל, כותבים את השם עם סוגריים
greet()
greet()  # אותה פונקציה, שימוש חוזר. זה בדיוק היתרון

print()


# ======================================================================
# חלק 2: פרמטרים
# ======================================================================

# פרמטר הוא ערך שהפונקציה מקבלת מבחוץ ועובדת איתו
def greet_home(name):
    print(f"welcome to {name}")


greet_home("Elad's Home")
greet_home("the office")

print()


# ערך ברירת מחדל: אם לא מעבירים ערך, פייתון משתמשת בזה שנקבע בהגדרה
def turn_on_light(room, brightness=100):
    print(f"light in '{room}' is on at {brightness}%")


turn_on_light("kitchen")                  # ברירת המחדל, 100
turn_on_light("bedroom", 40)              # לפי המיקום
turn_on_light("office", brightness=25)    # לפי שם הפרמטר, קריא יותר

print()


# ======================================================================
# חלק 3: המילה return
# ======================================================================

# פונקציה שרק מדפיסה לא מחזירה כלום. הערך שלה הוא None
def print_status(door_open):
    print("door is open" if door_open else "door is closed")


result = print_status(True)
print(f"what print_status returned: {result}")

print()


# פונקציה עם return מחזירה ערך, ואפשר לשמור אותו במשתנה,
# להשוות אותו, או להעביר אותו הלאה
def door_status(door_open):
    return "open" if door_open else "closed"


status = door_status(True)
print(f"door status: {status}")
print(f"is it open? {status == 'open'}")

print()


# return גם עוצרת את הפונקציה מיד. שום שורה אחריה לא תרוץ
def describe_brightness(brightness):
    if brightness == 0:
        return "off"
    if brightness < 30:
        return "dim"
    if brightness < 70:
        return "medium"
    return "bright"


for level in (0, 15, 50, 90):
    print(f"{level:>3}% -> {describe_brightness(level)}")

print()


# ======================================================================
# חלק 4: המילה if
# ======================================================================

# if בודקת תנאי. אם הוא נכון, הקוד המוזח מתחתיו רץ.
# elif נבדקת רק אם התנאי הקודם לא התקיים, ו-else תופסת את כל השאר
def check_window(window_open, temperature):
    if window_open and temperature < 10:
        return "close the window, it is cold outside"
    elif window_open:
        return "the window is open, enjoy the air"
    else:
        return "the window is closed"


print(check_window(True, 5))
print(check_window(True, 24))
print(check_window(False, 24))

print()


# אופרטורים להשוואה: ==  !=  <  <=  >  >=
# אופרטורים לוגיים:   and  or  not
def can_turn_on_light(room, rooms, brightness):
    """מחזירה True רק אם כל התנאים מתקיימים."""
    if room not in rooms:
        return False
    if not isinstance(brightness, int):
        return False
    if not 1 <= brightness <= 100:
        return False
    return True


rooms = ["kitchen", "bedroom", "living_room"]
print(can_turn_on_light("kitchen", rooms, 50))    # True
print(can_turn_on_light("garage", rooms, 50))     # False, אין חדר כזה
print(can_turn_on_light("kitchen", rooms, 150))   # False, עוצמה לא חוקית
print(can_turn_on_light("kitchen", rooms, "50"))  # False, טקסט ולא מספר

print()


# ======================================================================
# חלק 5: למה בכלל פונקציות
# ======================================================================

# בשיעור הקודם העתקנו את אותה בדיקת תקינות פעמיים.
# עכשיו כותבים אותה פעם אחת, ומשתמשים בה בכל מקום. זה עקרון DRY,
# כלומר Don't Repeat Yourself
def ask_brightness(prompt, answers):
    """
    קוראת ערך תקין מרשימת תשובות מוכנה.
    בשימוש אמיתי הרשימה מוחלפת בקריאה לפונקציה input.
    """
    for raw in answers:
        print(f"{prompt}{raw}")
        if not raw.isdigit():
            print("  that is not a whole number, try again")
            continue
        value = int(raw)
        if not 0 <= value <= 100:
            print("  the value must be between 0 and 100, try again")
            continue
        return value
    return 0


kitchen = ask_brightness("kitchen brightness? ", ["abc", "150", "80"])
bedroom = ask_brightness("bedroom brightness? ", ["40"])

print(f"kitchen: {kitchen}%, bedroom: {bedroom}%")


# ======================================================================
# תרגיל
# ======================================================================
#
# 1. כתבו פונקציה is_home_secure(door_open, window_open) שמחזירה True
#    רק אם גם הדלת וגם החלון סגורים.
# 2. כתבו פונקציה total_brightness(kitchen, bedroom, living) שמחזירה
#    את סכום עוצמות התאורה, ופונקציה שמחזירה את הממוצע.
# 3. הוסיפו ל-describe_brightness רמה נוספת בשם very dim,
#    לערכים שבין 1 ל-10.
