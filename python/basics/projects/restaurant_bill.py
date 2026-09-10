customer_name = input("Enter the customer name:")
print("Enter the price of food items:")
Item1 = float(input("Enter price of 1st item:"))
Item2 = float(input("Enter the price of 2nd item:"))
Item3 = float(input("Enter the price of 3rd item:"))
Subtotal = Item1 + Item2 + Item3 
if Subtotal >= 2000:
 discount = 10/100 * Subtotal
elif Subtotal >= 1000:
 discount = 5/100 * Subtotal
else:
 discount = 0
Bill = Subtotal - discount
GST = Bill* 5/100 
FinalBill = Bill + GST
print("Customer name is :",customer_name)
print("Subtotal is:",Subtotal)
print("Discount is:",discount)
print("GST is:",GST)
print("Final bill is:",FinalBill)
