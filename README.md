# בית חכם (Smart House)

תרגיל בתכנות מונחה עצמים בפייתון. הבית מיוצג כאובייקט אחד שיש לו מצב (State) והתנהגות (Behavior), בדיוק כמו חפץ בעולם האמיתי.

## הרעיון

לכל אובייקט בעולם יש שני דברים:

1. **מצב** (State / Attributes): הנתונים שלו. איך הוא נראה כרגע.
2. **התנהגות** (Behavior / Methods): הפעולות שהוא יודע לבצע.

בבית החכם יש דלת, חלון ומנורות. לכל אחד מהם יש מצב (פתוח או סגור, דולק או כבוי) ופעולות שהוא יודע לעשות.

## מבנה הפרויקט

```
smart-house/
├── smart_house.py    המחלקה SmartHome
├── main.py           נקודת הכניסה, הדגמה של השימוש במחלקה
├── tests/            בדיקות אוטומטיות
├── pyproject.toml    הגדרות הפרויקט והתלויות
└── .python-version   גרסת פייתון לפרויקט
```

## הרצה

```bash
uv run python main.py
```

## בדיקות

```bash
uv run pytest
```

## שלבי הפיתוח

### שלב 1: בית ראשוני

מחלקה אחת עם דלת, חלון ומנורה יחידה. משתנה נפרד לכל דבר: `door_open`, `window_open`, `light_on`.

### שלב 2: הבית גדל

כשמוסיפים חדרים, משתנה נפרד לכל חדר הופך לסיוט. במקום `light_bedroom` ו-`light_kitchen`, משתמשים במבני נתונים:

- המילון `room_lights` מנהל את כל החדרים במקום אחד. המפתח הוא שם החדר, והערך הוא עוצמת התאורה באחוזים.
- הרשימה `log_history` שומרת את היסטוריית הפעולות לפי סדר ביצוען.

### שלב 3: הימנעות מכפילות קוד

גם ב-`turn_on_light` וגם ב-`turn_off_light` הופיעה אותה בדיקה בדיוק: האם החדר קיים במילון. קוד משוכפל הוא מתכון לשגיאות, כי תיקון במקום אחד לא מגיע לשני.

הפתרון הוא מתודת העזר `validate_room`, שנקראת מתוך שאר המתודות באמצעות `self.validate_room(room)`. זהו עקרון DRY, כלומר Don't Repeat Yourself. כותבים פעם אחת, משתמשים בכל מקום.

## הממשק של המחלקה

| מתודה | תפקיד |
| --- | --- |
| `open_door()` / `close_door()` | פתיחה וסגירה של הדלת |
| `open_window()` / `close_window()` | פתיחה וסגירה של החלון |
| `add_room(room)` / `remove_room(room)` | הוספה והסרה של חדר |
| `turn_on_light(room, brightness=100)` | הדלקת אור בחדר, בעוצמה שבין 1 ל-100 |
| `turn_off_light(room)` | כיבוי האור בחדר |
| `turn_off_all_lights()` | כיבוי האור בכל הבית |
| `is_light_on(room)` | האם האור דולק בחדר |
| `lit_rooms()` | רשימת החדרים שהאור בהם דולק |
| `validate_room(room)` | בדיקה שהחדר קיים, משמשת את שאר המתודות |
| `status()` | מילון עם מצב הבית כולו |
| `show_log()` | הדפסת היסטוריית הפעולות |

כל מתודה שמשנה מצב מחזירה `True` בהצלחה ו-`False` בכישלון, כדי שאפשר יהיה לבדוק את התוצאה בקוד ולא רק לקרוא אותה במסך.

## דוגמה

```python
from smart_house import SmartHome

my_home = SmartHome(name="Elad's Home")
my_home.add_room("office")

my_home.open_door()
my_home.turn_on_light("kitchen")
my_home.turn_on_light("bedroom", brightness=40)

print(my_home)
my_home.show_log()
```
