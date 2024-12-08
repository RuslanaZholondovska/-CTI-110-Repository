# P5LAB_Ruslana Zholondovska
# 2024/11/17
# simulate a customer using a self-checkout machine with random numbers

#pseudocode
#1 Import random
#2 define disperse
#3 if else block
#4 main function

#1
import random


#2
def disperse_change(change):
    cents = int(round(change * 100))

    Dollars = cents // 100
    cents %= 100
    Quarters = cents // 25
    cents %= 25
    Dimes = cents // 10
    cents %= 10
    Nickels = cents // 5
    cents %= 5
    Pennies = cents
    
# 
    if Dollars > 0:
        print(f"{Dollars} Dollar{'s' if Dollars > 1 else ''}")
    if Quarters > 0:
        print(f"{Quarters} Quarter{'s' if Quarters > 1 else ''}")
    if Dimes > 0:
        print(f"{Dimes} Dime{'s' if Dimes > 1 else ''}")
    if Nickels > 0:
        print(f"{Nickels} Nickel{'s' if Nickels > 1 else ''}")
    if Pennies > 0:
        print(f"{Pennies} Pennie{'s' if Pennies > 1 else 'y'}")
    else:
        print('No Change')

#4
def main():
    total = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total}")
    amount_paid = float(input("How much cash will you put in the self-checkout? "))

    if amount_paid >= total:
        change = amount_paid - total
        print(f"Change is: ${change:.2f}")
        disperse_change(change)

if __name__ == "__main__":
    main()
