# Chapter 5 - Exercice 6
# 

# Calculate the Calories from Fat
def calculateCaloriesFromFat(fatGrams):
    caloriesFromFat = fatGrams * 9
    return caloriesFromFat

# Calculate the Calories from Carbs
def calculateCaloriesFromCarbs(carbGrams):
    caloriesFromCarbs = carbGrams * 4
    return caloriesFromCarbs

def main():
    userFatGrams = float( input( 'Enter the amount of fat in grams: ') ) # Get the amount of fat from the user
    userCarbGrams = float( input( 'Enter the amount of carbohydrates in grams: ') )  # Get the amount of carbohydrates from the user
    
    caloriesFromFat = calculateCaloriesFromFat(userFatGrams) #
    caloriesFromCarbs = calculateCaloriesFromCarbs(userCarbGrams)

    print('Calories from fat: ', caloriesFromFat)
    print('Calories from Carbs: ', caloriesFromCarbs)

main()