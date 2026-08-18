"""
שיעור 2: קליטת נתונים מהמשתמש עם input
======================================

הרצה:
    uv run python lessons/02_input_smart_house.py

הכלל החשוב ביותר בשיעור הזה:
הפונקציה input תמיד מחזירה מחרוזת (string), גם כשהמשתמש הקליד מספר.
אם רוצים לחשב עם הערך, חייבים להמיר אותו.
"""

# ======================================================================
# חלק 1: input מחזירה טקסט
# ======================================================================

# הטקסט שבתוך הסוגריים מודפס למסך, ואז התוכנית עוצרת
# ומחכה שהמשתמש יקליד משהו וילחץ אנטר
house_name = input("what is your home called? ")

print(f"hello, {house_name}")
print(f"the type of what input returned: {type(house_name)}")

print()


# ======================================================================
# חלק 2: המרה למספר
# ======================================================================

# input מחזירה טקסט, ולכן "80" הוא מחרוזת ולא מספר.
# הפונקציה int ממירה מחרוזת למספר שלם
brightness_text = input("kitchen light brightness (0-100)? ")
brightness = int(brightness_text)

print(f"as text:   {brightness_text!r}  (type: {type(brightness_text).__name__})")
print(f"as number: {brightness}  (type: {type(brightness).__name__})")

# ההבדל בפועל. חיבור על מחרוזות מדביק אותן זו לזו,
# וחיבור על מספרים מחשב סכום
print(f"text + text:     {brightness_text + brightness_text}")
print(f"number + number: {brightness + brightness}")

print()

# אפשר לקצר ולעטוף את input ישירות ב-int
rooms_count = int(input("how many rooms in the home? "))
print(f"the home has {rooms_count} rooms")

print()


# ======================================================================
# חלק 3: תשובות של כן ולא
# ======================================================================

# strip מסירה רווחים מיותרים מההתחלה ומהסוף,
# ו-lower הופכת את כל האותיות לקטנות, כדי ש-Yes ו-yes יתקבלו כאותו דבר
answer = input("is the front door open? (yes/no) ").strip().lower()

# ההשוואה מחזירה True או False, בדיוק הערך שאנחנו רוצים לשמור
door_open = answer in ("yes", "y")

print(f"door_open = {door_open}")

print()


# ======================================================================
# חלק 4: בדיקת תקינות של הקלט
# ======================================================================

# אסור לסמוך על מה שהמשתמש מקליד. תמיד בודקים.
# הלולאה תחזור על עצמה עד שיתקבל ערך חוקי
while True:
    raw = input("bedroom light brightness (0-100)? ").strip()

    # isdigit בודקת שכל התווים הם ספרות, כדי ש-int לא יקרוס
    if not raw.isdigit():
        print("that is not a whole number, try again")
        continue

    value = int(raw)
    if not 0 <= value <= 100:
        print("the value must be between 0 and 100, try again")
        continue

    # הקלט תקין, יוצאים מהלולאה
    light_bedroom = value
    break

print(f"bedroom light: {light_bedroom}%")

print()


# ======================================================================
# חלק 5: דוח מצב הבית
# ======================================================================

door_status = "open" if door_open else "closed"

print("--- home status ---")
print(f"name:    {house_name}")
print(f"rooms:   {rooms_count}")
print(f"door:    {door_status}")
print(f"kitchen: {brightness}%")
print(f"bedroom: {light_bedroom}%")


# ======================================================================
# תרגיל
# ======================================================================
#
# 1. שאלו את המשתמש האם החלון פתוח, ושמרו את התשובה במשתנה window_open.
# 2. הוסיפו שורה לדוח המצב שמציגה את מצב החלון.
# 3. שאלו על עוצמת האור בסלון, עם אותה בדיקת תקינות כמו בחלק 4.
#    שימו לב כמה קוד הייתם צריכים להעתיק. זו בדיוק הסיבה שבשיעור הבא
#    נוציא את הבדיקה לפונקציה נפרדת.
