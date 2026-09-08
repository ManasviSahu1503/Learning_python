name = input("Enter the employee name:")
Monthly_Salary = float(input("Enter the monthly salary:"))
Annual_Salary = Monthly_Salary * 12
print("Annual Salary is :",Annual_Salary) 
if Annual_Salary <= 300000:
    tax = 0;
elif Annual_Salary <= 600000:
    tax = 5 / 100 * Annual_Salary;
elif Annual_Salary <= 1000000:
    tax = 10 / 100 * Annual_Salary;
else:
    tax = 20 / 100 * Annual_Salary;

Net_Salary = Annual_Salary - tax;
print("tax is:", tax)
print("Net Annual Salary:",Net_Salary)

