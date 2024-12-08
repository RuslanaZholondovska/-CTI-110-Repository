# Ruslana Zholondovska
# 11/10/2024
# P4HW1
# collects grades, calculates, and displays grade

#1 capture scores
#2 gather input
#3 loop data collection
#4 calculations
#5 print statement
#6 calculate grade

#1
scores = []


#2
Scores = int(input("How many scores do you want to enter?: "))

#3
for i in range(Scores):
    while True:
        grade = float(input(f"Enter score #{i + 1}: ")) 
        if 0 <= grade <= 100:
            scores.append(grade)
            break 
        else:
            print("")
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")
        if 0 <= grade <= 100:
            grade = float(input(f"Enter score #{i + 1} again: "))
            scores.append(grade)
            break
            
print("")

print('------------Results------------')
#4
if len(scores) > 0:
    low = min(scores)
    scores.remove(low)
    sum_scores = sum(scores)
    avg = sum_scores / len(scores)
#5
print(f"Lowest Score{":":>3} {low:>1.1f}")
print(f"Modified List{":":>2} {scores}") 
print(f"Scores Average: {avg:>1.2f}")

#6
if avg >= 90:
    letter = 'A'
else:
    if avg >= 80:
        letter = 'B'
    else:
        if avg >= 70:
            letter = 'C'
        else:
            if avg >=60:
                letter = 'D'
            else:
                letter = 'F'
print(f'Grade{":":>10} {letter}')
print("----------------------------------------")

