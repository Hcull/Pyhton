employee_name = input("Enter empolyee's name:")
hours_worked = eval(input("Enter number of hours worked in a week:"))
pay_rate = eval(input("Enter hourly pay rate:"))
federal_tax = eval(input("Enter federal tax withholding rate:"))
state_tax = eval(input("Enter state tax withholding rate:"))

gross_pay = hours_worked * pay_rate
federal_withholding = gross_pay * federal_tax
state_withholding = gross_pay * state_tax
net_pay = gross_pay - (state_withholding + federal_withholding)

print("Empolyee Name:", employee_name)
print("Hours worked:", hours_worked)
print("Pay Rate:","$"+str(round(pay_rate,2)))
print("Gross Pay:","$"+str(round(gross_pay,2)))
print("Deductions:")
print("   Federal Withholding (20.0%):", format(federal_withholding,".2f"))
print("   State Withholding (9.0%):","$"+str(round(state_withholding,2)))
print("Total Deductions:",(federal_withholding)+ (state_withholding))
print("Net Pay:", "$"+ str(round(net_pay,2)))

