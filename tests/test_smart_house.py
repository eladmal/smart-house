"""בדיקות אוטומטיות למחלקה SmartHome."""

import pytest

from smart_house import SmartHome


@pytest.fixture
def home():
    """בית חדש לכל בדיקה, כדי שבדיקה אחת לא תשפיע על השנייה."""
    return SmartHome(name="Test Home", rooms=["kitchen", "bedroom"])


# ----------------------------------------------------------------------
# מצב התחלתי
# ----------------------------------------------------------------------


def test_new_home_starts_closed_and_dark(home):
    assert home.door_open is False
    assert home.window_open is False
    assert home.lit_rooms() == []


def test_default_rooms_are_created():
    default_home = SmartHome()
    assert set(default_home.room_lights) == {"living_room", "kitchen", "bedroom"}


# ----------------------------------------------------------------------
# דלת וחלון
# ----------------------------------------------------------------------


def test_open_and_close_door(home):
    assert home.open_door() is True
    assert home.door_open is True
    assert home.close_door() is True
    assert home.door_open is False


def test_opening_an_open_door_is_rejected(home):
    home.open_door()
    assert home.open_door() is False


def test_opening_an_open_window_is_rejected(home):
    home.open_window()
    assert home.open_window() is False
    assert home.window_open is True


# ----------------------------------------------------------------------
# תאורה
# ----------------------------------------------------------------------


def test_turn_on_light_uses_default_brightness(home):
    assert home.turn_on_light("kitchen") is True
    assert home.room_lights["kitchen"] == 100


def test_turn_on_light_with_explicit_brightness(home):
    home.turn_on_light("bedroom", brightness=40)
    assert home.is_light_on("bedroom") is True
    assert home.room_lights["bedroom"] == 40


@pytest.mark.parametrize("brightness", [0, -5, 101, 1000, "50", 50.5, None, True])
def test_invalid_brightness_is_rejected(home, brightness):
    assert home.turn_on_light("kitchen", brightness=brightness) is False
    assert home.room_lights["kitchen"] == 0


def test_turn_off_light(home):
    home.turn_on_light("kitchen")
    assert home.turn_off_light("kitchen") is True
    assert home.is_light_on("kitchen") is False


def test_turn_off_all_lights(home):
    home.turn_on_light("kitchen")
    home.turn_on_light("bedroom", brightness=20)
    home.turn_off_all_lights()
    assert home.lit_rooms() == []


# ----------------------------------------------------------------------
# חדרים ובדיקת התקינות המשותפת
# ----------------------------------------------------------------------


def test_validate_room_detects_missing_room(home):
    assert home.validate_room("kitchen") is True
    assert home.validate_room("garage") is False


def test_actions_on_a_missing_room_are_rejected(home):
    assert home.turn_on_light("garage") is False
    assert home.turn_off_light("garage") is False
    assert home.remove_room("garage") is False


def test_add_room(home):
    assert home.add_room("office") is True
    assert home.room_lights["office"] == 0
    assert home.add_room("office") is False


def test_remove_room(home):
    assert home.remove_room("kitchen") is True
    assert "kitchen" not in home.room_lights


# ----------------------------------------------------------------------
# דיווח מצב והיסטוריה
# ----------------------------------------------------------------------


def test_status_returns_a_full_snapshot(home):
    home.open_door()
    home.turn_on_light("kitchen", brightness=60)
    snapshot = home.status()

    assert snapshot["name"] == "Test Home"
    assert snapshot["door_open"] is True
    assert snapshot["window_open"] is False
    assert snapshot["lit_rooms"] == ["kitchen"]
    assert snapshot["room_lights"]["kitchen"] == 60


def test_status_does_not_expose_the_internal_dict(home):
    snapshot = home.status()
    snapshot["room_lights"]["kitchen"] = 99
    assert home.room_lights["kitchen"] == 0


def test_log_history_records_every_action(home):
    actions_before = len(home.log_history)
    home.open_door()
    home.turn_on_light("kitchen")
    assert len(home.log_history) == actions_before + 2


def test_str_describes_the_home(home):
    home.open_door()
    home.turn_on_light("bedroom")
    text = str(home)
    assert "Test Home" in text
    assert "door open" in text
    assert "bedroom" in text
