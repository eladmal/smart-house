"""
שיעור 1: הדפסה למסך ומשתנים
============================

הרצה:
    uv run python lessons/01_print_and_variables.py

בשיעור הזה אין עדיין מחלקות ואין אובייקטים. רק שתי אבני הבניין
הבסיסיות ביותר: הדפסה למסך, ושמירת נתונים במשתנים.
"""

# ======================================================================
# חלק 1: הפונקציה print
# ======================================================================

# print היא פונקציה. מה שכותבים בתוך הסוגריים, היא מדפיסה למסך.
print("Smart House - lesson 1")

# מחרוזת (string) היא טקסט. עוטפים אותה במרכאות, כפולות או בודדות
print("both quotes work")
print('exactly the same')

# שורה ריקה: קוראים ל-print בלי שום דבר בסוגריים
print()

# אפשר להעביר ל-print כמה ערכים, מופרדים בפסיק.
# פייתון תשים ביניהם רווח אחד באופן אוטומטי
print("door", "window", "light")

# הפרמטר sep קובע מה יופיע בין הערכים במקום הרווח
print("door", "window", "light", sep=" | ")

# הפרמטר end קובע מה יודפס בסוף. ברירת המחדל היא ירידת שורה
print("loading", end="...")
print("done")

print()


# ======================================================================
# חלק 2: משתנים
# ======================================================================

# משתנה הוא שם שמצביע על ערך. סימן השווה מבצע השמה, כלומר
# "קח את הערך מימין, ותן לו את השם משמאל"
house_name = "Elad's Home"

# מספר שלם (int)
rooms_count = 4

# מספר עשרוני (float)
temperature = 22.7

# ערך בוליאני (bool), אמת או שקר. שימו לב לאות הגדולה בהתחלה
door_open = False
window_open = True

# מחרוזת
front_door_color = "white"

print(house_name)
print(rooms_count)
print(temperature)
print(door_open)

print()


# ======================================================================
# חלק 3: מחרוזות מעוצבות (f-strings)
# ======================================================================

# הדרך הנוחה לשלב משתנים בתוך טקסט: מוסיפים את האות f לפני המרכאות,
# ומכניסים את שם המשתנה בתוך סוגריים מסולסלים
print(f"the home {house_name} has {rooms_count} rooms")
print(f"temperature: {temperature} degrees")

# בתוך הסוגריים המסולסלים אפשר גם לחשב
print(f"in fahrenheit: {temperature * 9 / 5 + 32}")

# עיגול לספרה אחת אחרי הנקודה, באמצעות f. אחרי נקודתיים
print(f"in fahrenheit: {temperature * 9 / 5 + 32:.1f}")

print()


# ======================================================================
# חלק 4: הטיפוס של כל ערך
# ======================================================================

# לכל ערך בפייתון יש טיפוס. הפונקציה type מגלה לנו אותו
print(type(house_name))
print(type(rooms_count))
print(type(temperature))
print(type(door_open))

print()


# ======================================================================
# חלק 5: המשתנים של הבית החכם
# ======================================================================

# עוצמת התאורה באחוזים, לכל חדר משתנה משלו.
# בהמשך נראה שזו בדיוק הבעיה שמילון בא לפתור
light_living_room = 0
light_kitchen = 80
light_bedroom = 0

print(f"living room light: {light_living_room}%")
print(f"kitchen light: {light_kitchen}%")
print(f"bedroom light: {light_bedroom}%")

print()

# שינוי ערך של משתנה: פשוט משימים לתוכו ערך חדש
light_bedroom = 40
print(f"bedroom light is now: {light_bedroom}%")

# הוספה לערך הקיים. שתי השורות הבאות עושות בדיוק אותו דבר
light_bedroom = light_bedroom + 10
light_bedroom += 10
print(f"bedroom light after two increases: {light_bedroom}%")

print()


# ======================================================================
# חלק 6: דוח מצב הבית
# ======================================================================

# ביטוי תנאי בשורה אחת: הערך שלפני if נבחר אם התנאי מתקיים,
# והערך שאחרי else נבחר אם לא
door_status = "open" if door_open else "closed"
window_status = "open" if window_open else "closed"

print("--- home status ---")
print(f"name:   {house_name}")
print(f"door:   {door_status}")
print(f"window: {window_status}")
print(f"lights: living {light_living_room}%, kitchen {light_kitchen}%, bedroom {light_bedroom}%")


# ======================================================================
# תרגיל
# ======================================================================
#
# 1. הוסיפו משתנה בשם light_office והדפיסו את מצבו.
# 2. הוסיפו משתנה בוליאני בשם alarm_on והדפיסו שורה בדוח המצב.
# 3. שנו את שם הבית והריצו שוב. שימו לב שהשינוי במקום אחד
#    משפיע על כל השורות שמשתמשות במשתנה.
