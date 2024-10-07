# Ruslana Zholondovska
# 10/6/2024
# Assignment Name: P2LAB2
# After naming a vehicle will display MPG then can calculate Gallons per mile driven

# Dictionary
my_dict = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}


keys = my_dict.keys()


print("dict_keys(['Camaro', 'Prius', 'Model S', 'Silverado'])")
print()

# select Vehicle
selected_vehicle = input("Enter a vehicle to see it's mpg: ")
print()


#enter miles
mpg = my_dict[selected_vehicle]
print(f"The {selected_vehicle} gets: {mpg} mpg.")
print()

#state distance
miles = float(input(f"How many miles will you drive the {selected_vehicle}?: "))
print()


gallons_needed = miles / mpg


print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {selected_vehicle} {miles} miles.")
print()
