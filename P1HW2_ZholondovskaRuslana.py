# Ruslana Zholondovska
# 9/29/2024
# P1HW2
# calculates your remaining budget after several factors are taken out

# Pseudocode comment block
# 1. Tells you what this app does
# 2. Gathers your budget,destination,gas,acomadation,and food expenses
# 3. Adds everything from 2. into a total expense 
# 4. Subtracts the total expense from the budget
# 5. Displays gathered and processed information
# 6. Calls the function


def main():
    # 1
    print("This program calculates and displays travel expenses\n")
    
    # 2
    budget = float(input("Enter budget: "))
    print()
    destination = input("Enter your travel destination: ")
    print()
    gas_expense = float(input("How much do you think you will spend on gas? "))
    print()
    accommodation_expense = float(input("Approximately, how much will you need for accommodation/hotel? "))
    print()
    food_expense = float(input("Last, how much do you need for food? "))
    
    
    print() 

    # 3
    total_expenses = gas_expense + accommodation_expense + food_expense

    # 4
    remaining_budget = budget - total_expenses

    # 5
    print("\n------------Travel Expenses------------")
    print(f"Location: {destination}")
    print(f"Initial Budget: ${budget:.2f}\n")
    print(f"Fuel: ${gas_expense:.2f}")
    print(f"Accommodation: ${accommodation_expense:.2f}")
    print(f"Food: ${food_expense:.2f}")
    print()
    print(f"Remaining Balance: ${remaining_budget:.2f}")

# 6
if __name__ == "__main__":
    main()
