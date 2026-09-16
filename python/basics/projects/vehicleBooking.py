class Vehicle:
    def __init__(self, vehicle_id, brand, model, price):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.price = price

    def display_vehicle(self):
        print("\nVehicle ID :", self.vehicle_id)
        print("Brand      :", self.brand)
        print("Model      :", self.model)
        print("Price      : ₹", self.price)


class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, price, fuel_type):
        super().__init__(vehicle_id, brand, model, price)
        self.fuel_type = fuel_type

    def display_vehicle(self):
        super().display_vehicle()
        print("Fuel Type  :", self.fuel_type)


class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, price, engine_cc):
        super().__init__(vehicle_id, brand, model, price)
        self.engine_cc = engine_cc

    def display_vehicle(self):
        super().display_vehicle()
        print("Engine     :", self.engine_cc, "CC")


class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.__booking_status = "Not Booked"

    def book_vehicle(self):
        self.__booking_status = "Booked"

    def display_customer(self):
        print("\nCustomer Name :", self.name)
        print("Phone Number  :", self.phone)
        print("Booking Status:", self.__booking_status)


class Showroom:
    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        print("======== AVAILABLE VEHICLES ========")

        for vehicle in self.vehicles:
            vehicle.display_vehicle()

    def book_vehicle(self, vehicle_id, customer):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:

                print("========= BOOKING DETAILS =========")

                vehicle.display_vehicle()

                customer.book_vehicle()
                customer.display_customer()

                print("\nBooking Successful!")
                return

        print("\nVehicle not found!")



showroom = Showroom("City Motors")

car1 = Car(101, "Tata", "Nexon", 850000, "Petrol")
car2 = Car(102, "Hyundai", "Creta", 1200000, "Diesel")
bike1 = Bike(201, "Royal Enfield", "Classic 350", 200000, 350)
bike2 = Bike(202, "Yamaha", "MT-15", 170000, 155)


showroom.add_vehicle(car1)
showroom.add_vehicle(car2)
showroom.add_vehicle(bike1)
showroom.add_vehicle(bike2)


showroom.display_vehicles()

print("======== CUSTOMER DETAILS ========")

name = input("Enter customer name: ")
phone = input("Enter phone number: ")
vehicle_id = int(input("Enter Vehicle ID to book: "))

customer = Customer(name, phone)


showroom.book_vehicle(vehicle_id, customer)