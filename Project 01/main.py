from addclass import add_new_class 
from view import view_todays_classes, view_tomorrows_classes
from delete import delete_class

def show_menu():
    print("\nClassmate App")
    print("1. Add new class to schedule")
    print("2. View today's classes")
    print("3. View tomorrow's classes")
    print("4. Delete Class")
    print("5. Exit")


while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_new_class()
    elif choice == "2":
        view_todays_classes()
    elif choice == "3":
        view_tomorrows_classes()
    elif choice == "4":
        delete_class()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")

