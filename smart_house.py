"""
בית חכם. מחלקה אחת שמייצגת בית, עם מצב (State) והתנהגות (Behavior).

השלבים בקוד:
1. בית ראשוני: דלת, חלון, ומנורה אחת.
2. הבית גדל: חדרים רבים, ולכן מבני נתונים כמו מילון ורשימה.
3. הימנעות מכפילות קוד: מתודת עזר אחת שמשרתת את כל השאר, עקרון DRY.
"""


class SmartHome:
    """בית חכם שמנהל דלת, חלון, ותאורה בכל אחד מהחדרים."""

    def __init__(self, name="My Smart Home", rooms=None):
        # מצב (State). הנתונים והתכונות של האובייקט
        self.name = name
        self.door_open = False
        self.window_open = False

        # מילון: שם החדר מוביל לעוצמת התאורה שלו באחוזים. אפס פירושו כבוי.
        # המילון חוסך לנו משתנה נפרד לכל חדר, כמו light_bedroom ו-light_kitchen
        default_rooms = ["living_room", "kitchen", "bedroom"]
        self.room_lights = {room: 0 for room in (rooms or default_rooms)}

        # רשימה: היסטוריית הפעולות שבוצעו בבית, לפי סדר ביצוען
        self.log_history = []
        self._log(f"home '{self.name}' created with rooms: {self.room_names()}")

    # ------------------------------------------------------------------
    # מתודות עזר
    # ------------------------------------------------------------------

    def _log(self, message):
        """שומר כל פעולה ברשימת ההיסטוריה ומדפיס אותה למסך."""
        self.log_history.append(message)
        print(message)

    def validate_room(self, room):
        """
        בדיקה אחת שמשרתת את כל המתודות שנוגעות בחדרים.
        זהו עקרון DRY: כותבים פעם אחת, משתמשים בכל מקום.
        """
        if room in self.room_lights:
            return True
        self._log(f"room '{room}' does not exist in this home")
        return False

    def room_names(self):
        """מחזיר את שמות החדרים כמחרוזת קריאה."""
        return ", ".join(sorted(self.room_lights))

    # ------------------------------------------------------------------
    # ניהול חדרים
    # ------------------------------------------------------------------

    def add_room(self, room):
        """מוסיף חדר חדש לבית, עם תאורה כבויה."""
        if room in self.room_lights:
            self._log(f"room '{room}' already exists")
            return False
        self.room_lights[room] = 0
        self._log(f"room '{room}' added")
        return True

    def remove_room(self, room):
        """מסיר חדר קיים מהבית."""
        if not self.validate_room(room):
            return False
        del self.room_lights[room]
        self._log(f"room '{room}' removed")
        return True

    # ------------------------------------------------------------------
    # דלת
    # ------------------------------------------------------------------

    def open_door(self):
        """פותח את הדלת, אם היא לא כבר פתוחה."""
        if self.door_open:
            self._log("door is already open")
            return False
        self.door_open = True
        self._log("door opened")
        return True

    def close_door(self):
        """סוגר את הדלת, אם היא לא כבר סגורה."""
        if not self.door_open:
            self._log("door is already closed")
            return False
        self.door_open = False
        self._log("door closed")
        return True

    # ------------------------------------------------------------------
    # חלון
    # ------------------------------------------------------------------

    def open_window(self):
        """פותח את החלון. בדיקת התקינות מונעת פעולה כפולה."""
        if self.window_open:
            self._log("window is already open")
            return False
        self.window_open = True
        self._log("window opened")
        return True

    def close_window(self):
        """סוגר את החלון."""
        if not self.window_open:
            self._log("window is already closed")
            return False
        self.window_open = False
        self._log("window closed")
        return True

    # ------------------------------------------------------------------
    # תאורה
    # ------------------------------------------------------------------

    def turn_on_light(self, room, brightness=100):
        """
        מדליק את האור בחדר מסוים, בעוצמה שבין 1 ל-100.
        ערך ברירת המחדל לעוצמה חוסך מהמשתמש לציין אותה בכל קריאה.
        """
        if not self.validate_room(room):
            return False
        if not isinstance(brightness, int) or isinstance(brightness, bool):
            self._log(f"brightness must be a whole number, got: {brightness!r}")
            return False
        if not 1 <= brightness <= 100:
            self._log(f"brightness must be between 1 and 100, got: {brightness}")
            return False
        self.room_lights[room] = brightness
        self._log(f"light in '{room}' is on at {brightness}%")
        return True

    def turn_off_light(self, room):
        """מכבה את האור בחדר מסוים."""
        if not self.validate_room(room):
            return False
        self.room_lights[room] = 0
        self._log(f"light in '{room}' is off")
        return True

    def turn_off_all_lights(self):
        """מכבה את האור בכל החדרים בבית."""
        for room in self.room_lights:
            self.room_lights[room] = 0
        self._log("all lights are off")
        return True

    def is_light_on(self, room):
        """מחזיר האם האור דולק בחדר מסוים."""
        if not self.validate_room(room):
            return False
        return self.room_lights[room] > 0

    def lit_rooms(self):
        """מחזיר רשימה של החדרים שהאור בהם דולק."""
        return [room for room, level in self.room_lights.items() if level > 0]

    # ------------------------------------------------------------------
    # דיווח מצב
    # ------------------------------------------------------------------

    def status(self):
        """מחזיר מילון עם מצב הבית כולו, נוח לבדיקות ולשירותים חיצוניים."""
        return {
            "name": self.name,
            "door_open": self.door_open,
            "window_open": self.window_open,
            "room_lights": dict(self.room_lights),
            "lit_rooms": self.lit_rooms(),
        }

    def show_log(self):
        """מדפיס את היסטוריית הפעולות לפי הסדר שבו בוצעו."""
        print(f"--- action history ({len(self.log_history)} actions) ---")
        for index, action in enumerate(self.log_history, start=1):
            print(f"{index:>3}. {action}")

    def __str__(self):
        """הייצוג הטקסטואלי של האובייקט, מה שמודפס כשקוראים לפונקציה print."""
        status_door = "open" if self.door_open else "closed"
        status_window = "open" if self.window_open else "closed"
        lights = self.lit_rooms()
        status_lights = ", ".join(lights) if lights else "none"
        return (
            f"{self.name}: door {status_door}, window {status_window}, "
            f"lights on in: {status_lights}"
        )

    def __repr__(self):
        return f"SmartHome(name={self.name!r}, rooms={sorted(self.room_lights)!r})"
