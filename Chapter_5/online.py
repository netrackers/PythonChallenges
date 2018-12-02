# Lab 4 - Exercice 1
# Convert Kilometers to Miles
# CCIS 1505-51 - Jerry Covington
# Student: Regis Kouatcho
    
def kilo(kilometers):
    milesInKilo = kilometers * 0.6214 # Convert the kilometers to miles.
    print()
    print ('That converts to ', format(milesInKilo, '.2f',) + ' miles.') # Prints the output of the operation, and format the output
    print()

def main():
    print()
    kilometers = float(input('Enter the distance in kilometers: ')) # Get the distance in Kilometers from the user
    kilo(kilometers) # Executes the kilo() function with the new value of kilometers

main() # Runs the program