crowd =[]
def add_person():
    name = input("Enter the name of person : ")
    crowd.append(name)
    print("Person added successfully")

def count_crowd():
 return len(crowd)

def check_capacity():
    current = count_crowd()

    if current < 0.8 * capacity:
        return "LOW CROWD"
    elif current < capacity:
        return "CROWD NEAR CAPACITY"
    elif current == capacity:
        return "CAPACITY FULL"
    else:
        return "OVERCROWDED"

def display_status():
    current = count_crowd()
    remaining = capacity - current
    status = check_capacity()

    print("---CROWD STATUS---")
    print("Total people:", current)
    print("Remaining capacity:",remaining)
    print("Status:",status)

capacity = int(input("Enter maximum of venue : "))

while True:
    print("===CROWD MANAGEMENT SYSTEM===")
    print("1. Add Person")
    print("2. View crowd Status")
    print("3. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        add_person()

    elif choice =="2":
        display_status()

    elif choice == "3":
        print("Final crowd count : ", count_crowd())
        print("Crowd Management System")
        break
    else:
        print("Invalid choice. Please try again")