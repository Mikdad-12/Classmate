from modules.storage import load_classes, save_classes

def delete_class():
    classes = load_classes()

    if not classes:
        print("\nNo classes to delete!")
        return

    print("\nAll Classes:")
    for i, c in enumerate(classes, start=1):
        print(f"{i}. {c['subject']} ({c['day']} {c['start_time']}-{c['end_time']}) [{c['type']}]")

    try:
        choice = int(input("\nEnter the number of the class to delete: "))
        if choice < 1 or choice > len(classes):
            print("Invalid number!")
            return
    except ValueError:
        print("Please enter a valid number!")
        return

    removed_class = classes.pop(choice - 1)
    save_classes(classes)
    print(f"\nClass '{removed_class['subject']}' on {removed_class['day']} deleted successfully!")
