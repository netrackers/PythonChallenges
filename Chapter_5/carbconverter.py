# Exercice 6 - Calories from fat and Carbohydrates

def calculateCaloriesFromFat(fatGrams):
   # fatGrams = float(input('Enter the amount of fat in grams: '))
    caloriesFromFat = fatGrams * 9
    return caloriesFromFat


def calculateCaloriesFromCarbs(carbsGrams):
    calculateCaloriesFromCarbs = carbsGrams * 4
    return caloriesFromCarbs

def main():
    fatGrams = float(input('Enter the amount of fat in grams: '))
    carbsGrams = float(input('Enter the amount of carbohydrates in grams: '))
    calFat = calculateCaloriesFromFat(fatGrams)
    calCarbs = calculateCaloriesFromCarbs(carbsGrams)

    print('Colories from Fat: ', format(calFat, '.2f' ) + "\n")
    print('Colories from Carbs: ', format(calCarbs, '.2f' ) + "\n")

#caloriesFromFat = fatGrams * 9
#caloriesFromCarbs = carbGrams * 4

main()