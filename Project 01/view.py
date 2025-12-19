from modules.storage import load_classes
from datetime import datetime

def get_start_time(class_item):
    return class_item["start_time"]

def view_todays_classes():
    classes = load_classes()
    
    today_index = datetime.today().weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    today = days[today_index]

    today_classes = []
    for c in classes:
        if c["day"].lower() == today.lower():
            today_classes.append(c)

    today_classes.sort(key=get_start_time)

    if not today_classes:
        print(f"\nNo classes scheduled for today ({today})")
        return

    print(f"\nToday's Classes ({today}):")
    for i, c in enumerate(today_classes, start=1):
        print(f"{i}. {c['subject']} ({c['start_time']} - {c['end_time']}) [{c['type']}]")


def view_tomorrows_classes():
    classes = load_classes()
    
    today_index = datetime.today().weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    tomorrow_index = (today_index + 1) % 7
    tomorrow = days[tomorrow_index]

    tomorrow_classes = []
    for c in classes:
        if c["day"].lower() == tomorrow.lower():
            tomorrow_classes.append(c)

    tomorrow_classes.sort(key=get_start_time)

    if not tomorrow_classes:
        print(f"\nNo classes scheduled for tomorrow ({tomorrow})")
        return

    print(f"\nTomorrow's Classes ({tomorrow}):")
    for i, c in enumerate(tomorrow_classes, start=1):
        print(f"{i}. {c['subject']} ({c['start_time']} - {c['end_time']}) [{c['type']}]")
