applicant_name = input("Enter the applicant name : ")
applicant_age = int(input("Enter the applicant age : "))
monthly_salary = int(input("Enter the monthly salary : "))
credit_score = float(input("Enter credic score : "))

if 21 <= applicant_age <= 60:
#if valid 
    if monthly_salary >= 30000:
        
#if valid
        if credit_score >=  700:
            status = "Loan Eligible"
        else:
            status = "Loan Not Eligible"
    else:
        status = "Loan Not Eligible"
else:
    status = "Loan Not Eligible"

print("Applicant age : ",applicant_name)
print("Loan status : ",status)