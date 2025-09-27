# math      = 68.98
# physics   = 89.67
# biology   = 55.56
# chemistry = 78.54
# english   = 71.53 
# marathi   = 91.78

# totalMakers = math + physics + biology + chemistry + english + marathi

# calculatePercentage = (totalMakers / 600) * 100

# print(calculatePercentage)

def calculatePercentage():

    math = int(input("Mathematics - "))
    physics = int(input("Physics - "))
    biology = int(input("Biology - "))
    chemistry = int(input("Chemistry - "))
    english = int(input("English - "))
    marathi = int(input("Marathi - "))

    calculateTotalMarks = math + physics + biology + chemistry + english + marathi

    calcPercentage = (calculateTotalMarks / 600) * 100

    if (calcPercentage >= 90):
        print("🌟 Outstanding Performance!")
    elif (calcPercentage >= 75):
        print("👏 Excellent Work!")
    elif (calcPercentage >= 60):
        print("👍 Good Job, Keep Improving.")
    elif calcPercentage >= 50:
        print("🙂 Fair, but needs more effort.")
    else:
        print("⚠️ Needs Improvement. Work Harder!")
        
    return float(calcPercentage)

print("Your Total % Are - ",calculatePercentage(), "%")
