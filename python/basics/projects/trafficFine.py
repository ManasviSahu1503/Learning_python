driver_name = input("Enter the name of driver :")
speed = float(input("Enter the vehicle speed :"))
if speed <= 50:
    fine = 0
elif speed <= 70:
    fine = 500
elif speed <= 100:
    fine = 1000
else:
    fine = 2000
print("Driver is :",driver_name)
print("Vehicle speed :",speed, "km/h")
print("Fine amount:",fine)
