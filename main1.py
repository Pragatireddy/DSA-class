#attendence tracking system
#dictionary to store attendence 
attendence = {}
def show_menu():
    print("Attendence Tracker")
    print("1. Add Attendence")
    print("2. View Attendence")
    print("3. Exit")   
def add_attendence():
    name = input("Enter the name of the student: ")
    status = input("Enter attendence status (Present/Absent): ")
    attendence[name] = status
    print("Attendence added successfully!")
def view_attendence():
    if not attendence:
        print("No attendence records found.")
    else:
        print("Attendence Records:")
        for name, status in attendence.items():
            print(f"{name}: {status}")
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            add_attendence()
        elif choice == '2':
            view_attendence()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
     