#Ruslana Zholondovksa
#11/23/2024
#P5HW
#Choose to either add or subtract random numbers and test your accuracy. 

#1 import
#2 add func
#3 subtract func
#4 main
#5





#1
import random



#2
def add_numbers():
    num1= random.randint(1,100)
    num2 = random.randint(1, 100)
    correct_answer = num1 + num2
    print(f"  {num1}")
    print(f"+ {num2}\n")

    guesses = 0


    while True:
        user_answer = int(input("Enter answer.\n"))
        guesses += 1

        if user_answer == correct_answer:
                print(f"Congradulations!!!! Your answer is correct.")
                print(f"Number of gueses: {guesses}\n")
                main_menu()
                break

        while user_answer != correct_answer:
            if user_answer < correct_answer:
                print("Sorry, guess is too low.\n")
            if user_answer > correct_answer:
                print("Sorry, guess is too high.\n")

            user_answer = int(input("Try again : "))
            guesses += 1

            if user_answer == correct_answer:
                print(f"Congradulations!!!! Your answer is correct.")
                print(f"Number of gueses: {guesses}\n")
                main_menu()
                break






#3
def subtract_numbers():
    num1= random.randint(1,100)
    num2 = random.randint(1, 100)
    correct_answer = num1 - num2
    print(f"  {num1}") 
    print(f"- {num2}\n")

    guesses = 0


    while True:
        user_answer = int(input("Enter answer.\n"))
        guesses += 1

        if user_answer == correct_answer:
                print(f"Congradulations!!!! Your answer is correct.")
                print(f"Number of gueses: {guesses}\n")
                main_menu()
                break

        while user_answer != correct_answer:
            if user_answer < correct_answer:
                print("Sorry, guess is too low.\n")
            if user_answer > correct_answer:
                print("Sorry, guess is too high.\n")

            user_answer = int(input("Try again : "))
            guesses += 1

            if user_answer == correct_answer:
                print(f"Congradulations!!!! Your answer is correct.")
                print(f"Number of gueses: {guesses}\n")
                main_menu()
                break

        
                
#4
print("Welcome to Math Quiz")      
print("")
print("")
def main_menu():
    while True:
        print("MAIN MENU")
        print("--------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit\n")


        pick = input("Please choose one of the menu options: ")

        if pick.isdigit():
            pick = int(pick)
            if pick == 1:
                add_numbers()
            elif pick == 2:
                subtract_numbers()
            elif pick == 3:
                print("Thank you for playing...")
                print("Bye!!")
                break
            else:
                print("Invalid only choose 1, 2, or 3") 

            
                

main_menu()
