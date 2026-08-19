"""
שיעור 4: רשימות, מילונים, ורישום פעולות ללוג
============================================

הרצה:
    uv run python lessons/04_lists_dicts_log.py

עד עכשיו הגדרנו משתנה נפרד לכל חדר. כשהבית גדל זה הופך לסיוט.
הפתרון הוא מבני נתונים: רשימה (list) ומילון (dict).
"""

# ======================================================================
# חלק 1: הבעיה
# ======================================================================

# משתנה נפרד לכל חדר. עם שלושה חדרים זה נסבל, עם עשרים זה בלתי אפשרי
light_living_room = 0
light_kitchen = 80
light_bedroom = 40

print(f"living: {light_living_room}%, kitchen: {light_kitchen}%, bedroom: {light_bedroom}%")
print()


# ======================================================================
# חלק 2: רשימה (list)
# ======================================================================

# רשימה היא אוסף ערכים לפי סדר. עוטפים בסוגריים מרובעים
rooms = ["living_room", "kitchen", "bedroom"]

print(rooms)
print(f"how many rooms: {len(rooms)}")
print(f"first room:  {rooms[0]}")     # הספירה מתחילה מאפס
print(f"last room:   {rooms[-1]}")    # מספר שלילי סופר מהסוף

# הוספה והסרה
rooms.append("office")
print(f"after append: {rooms}")

rooms.remove("living_room")
print(f"after remove: {rooms}")

# בדיקת שייכות
print(f"is 'kitchen' in the list? {'kitchen' in rooms}")
print(f"is 'garage' in the list?  {'garage' in rooms}")

print()

# מעבר על הרשימה בלולאה
for room in rooms:
    print(f"  room: {room}")

print()


# ======================================================================
# חלק 3: מילון (dict)
# ======================================================================

# מילון שומר זוגות של מפתח וערך. עוטפים בסוגריים מסולסלים.
# כאן המפתח הוא שם החדר, והערך הוא עוצמת התאורה שלו
room_lights = {
    "living_room": 0,
    "kitchen": 80,
    "bedroom": 40,
}

print(room_lights)

# קריאה לפי מפתח
print(f"kitchen: {room_lights['kitchen']}%")

# עדכון ערך קיים
room_lights["kitchen"] = 55
print(f"kitchen after update: {room_lights['kitchen']}%")

# הוספת מפתח חדש. אותו תחביר בדיוק
room_lights["office"] = 100
print(f"after adding office: {room_lights}")

# מחיקה
del room_lights["living_room"]
print(f"after deleting living room: {room_lights}")

print()

# בדיקת שייכות. זו בדיוק הבדיקה שתהפוך בהמשך למתודה validate_room
print(f"is 'kitchen' a room? {'kitchen' in room_lights}")
print(f"is 'garage' a room?  {'garage' in room_lights}")

print()

# מעבר על מילון. המתודה items מחזירה את המפתח ואת הערך יחד
for room, level in room_lights.items():
    state = "on" if level > 0 else "off"
    print(f"  {room:<12} {level:>3}%  ({state})")

print()

# בניית רשימה מתוך מילון, בשורה אחת
lit_rooms = [room for room, level in room_lights.items() if level > 0]
print(f"rooms with the light on: {lit_rooms}")

print()


# ======================================================================
# חלק 4: רישום פעולות ללוג
# ======================================================================

# הלוג הוא פשוט רשימה שאליה מוסיפים שורה בכל פעם שמשהו קורה.
# הוא עונה על השאלה "מה קרה כאן", ובלעדיו כמעט אי אפשר לאתר תקלות
log_history = []


def log(message):
    """שומרת את הפעולה ברשימה, ומדפיסה אותה למסך."""
    log_history.append(message)
    print(message)


def turn_on_light(room, brightness=100):
    """מדליקה אור בחדר, אחרי בדיקת תקינות. מחזירה True או False."""
    if room not in room_lights:
        log(f"room '{room}' does not exist in this home")
        return False
    if not 1 <= brightness <= 100:
        log(f"brightness must be between 1 and 100, got: {brightness}")
        return False
    room_lights[room] = brightness
    log(f"light in '{room}' is on at {brightness}%")
    return True


def turn_off_light(room):
    """מכבה אור בחדר. שימו לב שבדיקת התקינות מועתקת מכאן לשם."""
    if room not in room_lights:
        log(f"room '{room}' does not exist in this home")
        return False
    room_lights[room] = 0
    log(f"light in '{room}' is off")
    return True


turn_on_light("kitchen")
turn_on_light("bedroom", 40)
turn_on_light("garage")
turn_on_light("office", 150)
turn_off_light("kitchen")

print()
print(f"--- action history ({len(log_history)} actions) ---")
for index, action in enumerate(log_history, start=1):
    print(f"{index:>3}. {action}")

print()


# ======================================================================
# חלק 5: מה עוד לא בסדר כאן
# ======================================================================

# שימו לב לשתי בעיות בקוד שלמעלה:
#
# 1. אותה בדיקה בדיוק, room not in room_lights, מופיעה בשתי הפונקציות.
#    אם נשנה אותה במקום אחד ונשכח את השני, נקבל התנהגות לא עקבית.
#    הפתרון הוא פונקציית עזר אחת.
#
# 2. הפונקציות מסתמכות על המשתנים room_lights ו-log_history
#    שנמצאים בחוץ. זה אומר שאפשר לנהל רק בית אחד בכל התוכנית,
#    ושכל קוד אחר בקובץ יכול לשנות אותם בלי ידיעתנו.
#
# שתי הבעיות נפתרות באותו כלי, והוא נושא השיעור הבא: מחלקה.


def validate_room(room):
    """פונקציית העזר. בדיקה אחת שמשרתת את כל השאר."""
    if room in room_lights:
        return True
    log(f"room '{room}' does not exist in this home")
    return False


print(f"validate_room('kitchen') -> {validate_room('kitchen')}")
print(f"validate_room('garage')  -> {validate_room('garage')}")


# ======================================================================
# תרגיל
# ======================================================================
#
# 1. שכתבו את turn_on_light ואת turn_off_light כך שישתמשו
#    ב-validate_room במקום להעתיק את הבדיקה.
# 2. כתבו פונקציה turn_off_all_lights שמכבה את האור בכל החדרים,
#    ורושמת שורה אחת ללוג.
# 3. כתבו פונקציה brightest_room שמחזירה את שם החדר שהאור בו
#    הכי חזק. מה היא צריכה להחזיר כשכל האורות כבויים?
