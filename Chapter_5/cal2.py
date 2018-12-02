# Chapter 5 - Exercice 6
# 

# Calculate the Calories from Fat
def fatCalc(fatGrams):
    caloriesFromFat = fatGrams * 9
    return caloriesFromFat

# Calculate the Calories from Carbs
def carbsCalc(carbGrams):
    caloriesFromCarbs = carbGrams * 4
    return caloriesFromCarbs

def main():
    print()
    userFatGrams = float( input( 'Enter the amount of fat in grams: ') ) # Get the amount of fat from the user
    userCarbGrams = float( input( 'Enter the amount of carbohydrates in grams: ') )  # Get the amount of carbohydrates from the user
    
    caloriesFromFat = fatCalc(userFatGrams) # Use the function fatCalc to get the amount of Calories form fat
    caloriesFromCarbs = carbsCalc(userCarbGrams) # Call the function carbsCalc to get the amount of Calories from Carbohydrates

    print()
    print('Calories from fat: ', caloriesFromFat)
    print('Calories from Carbs: ', caloriesFromCarbs)

main()