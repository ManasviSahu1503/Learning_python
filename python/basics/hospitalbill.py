patient_name = input("Enter the patient name:")
consultation_fee = float(input("Enter the consultation fee:"))
medicine_cost = float(input("Enter medicine cost:"))
test_cost = float(input("Enter test cost:"))

Total_Bill = consultation_fee + medicine_cost + test_cost

if Total_Bill >= 10000:
    discount = 10 / 100 * Total_Bill
elif Total_Bill >= 5000:
    discount = 5 / 100 *  Total_Bill
else:
    discount = 0

final_bill = Total_Bill - discount 

print("Final Bill is:", final_bill)
    