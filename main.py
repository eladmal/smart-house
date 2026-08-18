"""נקודת הכניסה לתוכנית. מדגימה שימוש במחלקה SmartHome."""

from smart_house import SmartHome


def run_smart_house():
    print("Hello from your smart-house!")

    # יצירת מופע (אובייקט) מהמחלקה של הבית החכם
    my_home = SmartHome(name="Elad's Home")

    # הבית גדל, מוסיפים חדר
    my_home.add_room("office")

    # דלת וחלון
    my_home.open_door()
    my_home.open_window()
    my_home.open_window()  # בדיקת התקינות מונעת פעולה כפולה

    # תאורה
    my_home.turn_on_light("kitchen")
    my_home.turn_on_light("bedroom", brightness=40)
    my_home.turn_on_light("garage")  # חדר שאינו קיים, הבדיקה תתפוס אותו
    my_home.turn_on_light("office", brightness=150)  # עוצמה לא חוקית

    print()
    print(my_home)
    print()

    # סגירת הבית
    my_home.turn_off_all_lights()
    my_home.close_window()
    my_home.close_door()

    print()
    print(my_home)
    print()
    my_home.show_log()


if __name__ == "__main__":
    run_smart_house()
