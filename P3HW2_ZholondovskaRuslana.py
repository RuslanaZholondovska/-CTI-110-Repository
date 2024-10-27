# Ruslana Zholondovska
# 10/24/2024
# P3HW2
# calculates pay and overtime pay 


#1 define varibles
#2 gather user input
#3 if else statement
#4 calculation
#5 results


#1
RegularHours = 40
Rate = 1.5

#2
Name = input("Enter employee's name: ")
WorkHours = float(input("Enter number of hours worked: "))
PayRate = float(input("Enter employee's pay rate: "))


print("-------------------------------------")
print(f" Employee name:{Name} ")
print("")

#3
if WorkHours > RegularHours:
    OverTime = WorkHours - RegularHours
    WorkHours = RegularHours
else:
    OverTime = 0
    

#4    
RegularHour_Pay = WorkHours * PayRate
RegularPay = WorkHours * PayRate
OverPay = OverTime * (PayRate * Rate)
Gross = RegularPay + OverPay

#5
print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
print("--------------------------------------------------------------------------------------")
print(f"{WorkHours + OverTime:<15}{PayRate:<15}{OverTime:<15}{OverPay:<15}{RegularHour_Pay:<15}{Gross:<15}")


