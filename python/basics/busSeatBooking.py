class Bus:
    def __init__(self, bus_no, total_seats):
        self.bus_no = bus_no
        self.total_seats = total_seats
        self.seats = [None] * total_seats

    def show_seats(self):
        print("\nSeat Status:")
        for i in range(self.total_seats):
            if self.seats[i] is None:
                print(f"Seat {i + 1}: Available")
            else:
                print(f"Seat {i + 1}: Booked by {self.seats[i]}")

    def book_seat(self, seat_no, passenger_name):
        if seat_no < 1 or seat_no > self.total_seats:
            print("Invalid seat number!")
        elif self.seats[seat_no - 1] is not None:
            print("Seat already booked!")
        else:
            self.seats[seat_no - 1] = passenger_name
            print(f"Seat {seat_no} booked successfully for {passenger_name}.")

    def cancel_seat(self, seat_no):
        if seat_no < 1 or seat_no > self.total_seats:
            print("Invalid seat number!")
        elif self.seats[seat_no - 1] is None:
            print("Seat is already available!")
        else:
            print(f"Booking cancelled for {self.seats[seat_no - 1]}.")
            self.seats[seat_no - 1] = None



bus = Bus("MH12-AB-1234", 10)

while True:
    print("\n===== BUS SEAT BOOKING =====")
    print("1. Show Seats")
    print("2. Book Seat")
    print("3. Cancel Seat")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        bus.show_seats()

    elif choice == 2:
        seat_no = int(input("Enter seat number: "))
        name = input("Enter passenger name: ")
        bus.book_seat(seat_no, name)

    elif choice == 3:
        seat_no = int(input("Enter seat number: "))
        bus.cancel_seat(seat_no)

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")