print("===== MOBILE BANKING SYSTEM =====")

print("\nAvailable Recharge Plans:")
print("1. ₹199 - 1.5 GB/day - 28 Days")
print("2. ₹299 - 2 GB/day - 28 Days")
print("3. ₹499 - 2.5 GB/day - 56 Days")


customer_name = input("Enter customer name:")
recharge_amount = int(input("Enter the recharge amount:"))
print("Checking recharge amount...")
if recharge_amount == 199:
    print("Recharge successful !")
    print("Customer:",customer_name)
    print("Plan: ₹199 - 1.5 GB/day - 28 Days")
elif recharge_amount == 299:
    print("Recharge successful !")
    print("Customer:",customer_name)
    print("Plan: ₹299 - 2 GB/day - 28 Days")
elif recharge_amount == 499:
    print("Recharge successful !")
    print("Customer:",customer_name)
    print("plan: ₹499 - 2.5 GB/day - 56 Days")
else:
    print("Invalid Recharge Plan")


