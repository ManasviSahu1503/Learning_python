def get_driver_details():
    driver_name = input("Enter driver's name: ")
    vehicle_number = input("Enter vehicle number: ")
    vehicle_type = input("Enter vehicle type (Car/Bike/Truck/Bus): ")

    return driver_name, vehicle_number, vehicle_type


def calculate_speed_fine(speed):
    if speed <= 50:
        fine = 0
        violation = "No violation"
    elif speed <= 70:
        fine = 500
        violation = "Over Speeding - Level 1"
    elif speed <= 100:
        fine = 1000
        violation = "Over Speeding - Level 2"
    else:
        fine = 2000
        violation = "Over Speeding - Level 3"

    return fine, violation


def check_documents():
    license = input("Does the driver have a valid license? (yes/no): ")
    insurance = input("Does the vehicle have valid insurance? (yes/no): ")

    extra_fine = 0

    if license.lower() == "no":
        extra_fine += 1000

    if insurance.lower() == "no":
        extra_fine += 500

    return extra_fine


def display_report(name, vehicle, vehicle_type, speed, fine, violation, extra_fine):
    total_fine = fine + extra_fine

    print("\n========== TRAFFIC REPORT ==========")
    print("Driver Name       :", name)
    print("Vehicle Number    :", vehicle)
    print("Vehicle Type      :", vehicle_type)
    print("Vehicle Speed     :", speed, "km/h")
    print("Violation         :", violation)
    print("Speed Fine        : ₹", fine)
    print("Document Fine     : ₹", extra_fine)
    print("Total Fine        : ₹", total_fine)

    if total_fine == 0:
        print("Status            : No Fine")
    else:
        print("Status            : Fine Issued")

    print("====================================")


# Main Program

print("===== TRAFFIC FINE MANAGEMENT SYSTEM =====")

driver_name, vehicle_number, vehicle_type = get_driver_details()

speed = float(input("Enter vehicle speed (km/h): "))

fine, violation = calculate_speed_fine(speed)

extra_fine = check_documents()

display_report(
    driver_name,
    vehicle_number,
    vehicle_type,
    speed,
    fine,
    violation,
    extra_fine
)