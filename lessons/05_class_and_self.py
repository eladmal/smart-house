"""
שיעור 5: מחלקה, אובייקט, והמילה self
====================================

הרצה:
    uv run python lessons/05_class_and_self.py

בשיעור הקודם היו לנו משתנים גלובליים ופונקציות שתלויות בהם.
מחלקה אורזת את שניהם יחד: הנתונים והפעולות שמטפלות בהם, במקום אחד.
"""

# ======================================================================
# חלק 1: מחלקה ראשונה
# ======================================================================

# class מגדירה תבנית. היא עדיין לא בית, היא השרטוט של הבית.
# לפי התבנית הזאת אפשר לייצר בתים רבים, וכל אחד עם המצב שלו
class SimpleHome:

    # __init__ היא הפונקציה שרצה אוטומטית בכל פעם שנוצר אובייקט חדש.
    # קוראים לה בנאי (constructor), והיא קובעת את המצב ההתחלתי
    def __init__(self):
        self.door_open = False
        self.light_on = False

    def open_door(self):
        self.door_open = True
        print("door opened")


# יצירת מופע (instance), כלומר אובייקט אמיתי לפי התבנית
home = SimpleHome()
print(f"door at the start: {home.door_open}")
home.open_door()
print(f"door now:          {home.door_open}")

print()


# ======================================================================
# חלק 2: מה זו המילה self
# ======================================================================

# self הוא האובייקט עצמו, זה שעליו הופעלה המתודה.
# פייתון מעבירה אותו אוטומטית, ולכן הוא תמיד הפרמטר הראשון בהגדרה,
# אבל לעולם לא כותבים אותו בקריאה.
#
#     home.open_door()   מה שאנחנו כותבים
#     SimpleHome.open_door(home)   מה שפייתון עושה בפועל
#
# מכאן נובע הכלל: כל מה ששייך לאובייקט נגיש דרך self,
# גם נתונים (self.door_open) וגם מתודות אחרות (self.validate_room).

# וזה בדיוק היתרון: שני בתים נפרדים, כל אחד עם מצב משלו
home_a = SimpleHome()
home_b = SimpleHome()

home_a.open_door()

print(f"home_a door: {home_a.door_open}")
print(f"home_b door: {home_b.door_open}")  # לא הושפע כלל

print()


# ======================================================================
# חלק 3: הבית המלא
# ======================================================================

class SmartHome:
    """בית חכם שמנהל דלת, חלון, ותאורה בכל אחד מהחדרים."""

    def __init__(self, name="My Smart Home", rooms=None):
        # מצב (State). כל אלה שייכים לאובייקט הזה בלבד
        self.name = name
        self.door_open = False
        self.window_open = False
        self.room_lights = {room: 0 for room in (rooms or ["kitchen", "bedroom"])}
        self.log_history = []

        # מתודה קוראת למתודה אחרת של אותו אובייקט, דרך self
        self._log(f"home '{self.name}' created")

    # ------------------------------------------------------------------
    # מתודות עזר
    # ------------------------------------------------------------------

    def _log(self, message):
        """קו תחתון בתחילת השם הוא סימן מוסכם: מתודה לשימוש פנימי."""
        self.log_history.append(message)
        print(message)

    def validate_room(self, room):
        """הבדיקה המשותפת. עכשיו היא חלק מהאובייקט, לא פונקציה גלובלית."""
        if room in self.room_lights:
            return True
        self._log(f"room '{room}' does not exist in this home")
        return False

    # ------------------------------------------------------------------
    # פעולות
    # ------------------------------------------------------------------

    def open_door(self):
        if self.door_open:
            self._log("door is already open")
            return False
        self.door_open = True
        self._log("door opened")
        return True

    def close_door(self):
        if not self.door_open:
            self._log("door is already closed")
            return False
        self.door_open = False
        self._log("door closed")
        return True

    def turn_on_light(self, room, brightness=100):
        # שלוש שורות, ואפס כפילות. הבדיקה יושבת במקום אחד בלבד
        if not self.validate_room(room):
            return False
        if not isinstance(brightness, int) or not 1 <= brightness <= 100:
            self._log(f"brightness must be between 1 and 100, got: {brightness}")
            return False
        self.room_lights[room] = brightness
        self._log(f"light in '{room}' is on at {brightness}%")
        return True

    def turn_off_light(self, room):
        if not self.validate_room(room):
            return False
        self.room_lights[room] = 0
        self._log(f"light in '{room}' is off")
        return True

    def lit_rooms(self):
        return [room for room, level in self.room_lights.items() if level > 0]

    # ------------------------------------------------------------------
    # דיווח
    # ------------------------------------------------------------------

    def __str__(self):
        """מה שיודפס כשקוראים ל-print על האובייקט."""
        door = "open" if self.door_open else "closed"
        lights = ", ".join(self.lit_rooms()) or "none"
        return f"{self.name}: door {door}, lights on in: {lights}"

    def show_log(self):
        print(f"--- action history ({len(self.log_history)} actions) ---")
        for index, action in enumerate(self.log_history, start=1):
            print(f"{index:>3}. {action}")


# ======================================================================
# חלק 4: שימוש
# ======================================================================

my_home = SmartHome(name="Elad's Home", rooms=["kitchen", "bedroom", "office"])

my_home.open_door()
my_home.open_door()               # בדיקת התקינות תופסת פעולה כפולה
my_home.turn_on_light("kitchen")
my_home.turn_on_light("bedroom", brightness=40)
my_home.turn_on_light("garage")   # חדר שאינו קיים
my_home.turn_off_light("kitchen")

print()
print(my_home)
print()
my_home.show_log()

print()


# ======================================================================
# חלק 5: שני בתים, שני מצבים
# ======================================================================

# כל אובייקט מחזיק את הנתונים שלו. אין שום התנגשות ביניהם
office = SmartHome(name="The Office", rooms=["meeting_room"])
office.turn_on_light("meeting_room", brightness=70)

print()
print(my_home)
print(office)


# ======================================================================
# תרגיל
# ======================================================================
#
# 1. הוסיפו את המתודות open_window ו-close_window, באותו מבנה
#    בדיוק כמו open_door ו-close_door.
# 2. הוסיפו מתודה add_room שמוסיפה חדר חדש עם תאורה כבויה,
#    ומסרבת להוסיף חדר שכבר קיים.
# 3. הוסיפו מתודה status שמחזירה מילון עם כל מצב הבית.
#    למה עדיף שהיא תחזיר מילון ולא תדפיס אותו?
#
# הפתרון המלא נמצא בקובץ smart_house.py שבשורש הפרויקט.
