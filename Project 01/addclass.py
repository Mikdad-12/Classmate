from modules.schedule import create_class
from modules.storage import load_classes, save_classes

def add_new_class():
    classes = load_classes()

    subject = input("Course Name: ")
    
    def get_valid_day():
        valid_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        while True:
            day = input("Day: ").strip().capitalize()
            if day in valid_days:
                return day 
            else:
                print("Invalid day! Please enter a valid day (Monday-Sunday).")

    day = get_valid_day()
    
    start = input("Start Time(HH:MM): ")
    end = input("End Time(HH:MM): ")

    print("1. Regular Class")
    print("2. Extra Class")
    print("3. CT/Exam")

    c = int(input("Choose Class Type (1-3): "))

    def get_class_type(choice):
        if choice == 1:
            return "Regular Class"
        elif choice == 2:
            return "Extra Class"
        elif choice == 3:
            return "CT/Exam"
        else:
            return "Regular Class" 

    c_type = get_class_type(c)

    new_class = create_class(subject, day, start, end, c_type)

    classes.append(new_class)

    save_classes(classes)

    print("\nClass added successfully!")
