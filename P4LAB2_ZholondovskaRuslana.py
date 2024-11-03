# Ruslana Zholondovska
# 11/2/2024
# P4LAB2
# Multiplication Tables

#1 set varible for loop to run
#2 while loop
#3 for loop
#4 restart and handle exit of program

#1
run = True
#2
while run:
    user_input = int(input("Enter an integer: "))
    print("")
        
    if user_input < 0:
        print("This program does not handle negative number")
    else:
        for i in range(1, 13):#3
            print(f"{user_input} x {i} = {user_input * i}")
    print("")
#4
    run_again = input("Would you like to run the program again?: ")
    print("")
    if run_again == "no":
        print("Exiting program...")
        break
