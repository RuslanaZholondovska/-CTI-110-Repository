# Ruslana Zholondovska
# 9/27/24
# P1HW1
# Solves exponents and does addition/subtraction

class BasicCalculator:
    def __init__(self):
        self.base = 0
        self.exponent = 0
        self.starting_integer = 0
        self.addend = 0
        self.subtrahend = 0

    def collect_data(self):
        self.base = self.get_integer_input("Enter an integer as the base value: ")
        self.exponent = self.get_integer_input("Enter an integer as the exponent: ")

        # Calculate and display the exponentiation result immediately
        exp_result = self.base ** self.exponent
        print("\n")  # Double space
        print(f"{self.base} raised to the power of {self.exponent} is {exp_result} !!\n")

        # Double space before heading for addition and subtraction
        print("\n----- Addition and Subtraction -----\n")

        self.starting_integer = self.get_integer_input("Enter a starting integer: ")
        self.addend = self.get_integer_input("Enter an integer to add: ")
        self.subtrahend = self.get_integer_input("Enter an integer to subtract: ")
        print("\n")  # Double space after entering the integer to subtract

    def get_integer_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def display_arithmetic(self):
        final_result = (self.starting_integer + self.addend) - self.subtrahend
        print(f"{self.starting_integer} + {self.addend} - {self.subtrahend} is equal to {final_result}")

def main():
    calculator = BasicCalculator()

    # Print double space and heading for exponentiation
    print("\n")
    print("----- Calculating Exponents -----")
    print("\n")
    
    calculator.collect_data()
    calculator.display_arithmetic()

# Run the main function
if __name__ == "__main__":
    main()
