# Write a program that reads the contents of the file charge_accounts.txt
# into a list. The program should then ask the user to enter a charge account number. 
# The program should determine whether the number is valid by searching
# for it in the list. If the number is in the list, the program should
# display a message indicating the number is valid. If the number is not
# in the list, theprogram should display a message indicating the number
# is invalid.

# Define the name of the file that contains the accounts numbers
ACCOUNT_FILE = "charge_accounts.txt"

# Get an account number from the user
def getUserChargeAccountNumber():
    userChargeAccountNumber = input('\nEnter a charge account to look up: ')
    return userChargeAccountNumber

# Read the number in the file,  remove the '\n' at the end of each number
# and put them sequentially in the list
def readChargeAccountsToList (chargeAccountsfile):
    chargeAccountList = []
    chargeAccountNumber = chargeAccountsfile.readline()

    while chargeAccountNumber != '':
        chargeAccountNumber = chargeAccountNumber.rstrip('\n')
        chargeAccountList.append(chargeAccountNumber)
        chargeAccountNumber = chargeAccountsfile.readline()

    return chargeAccountList

# Verify if the number exists in the list
def userChargeAccountNumberExists(userChargeAccountNumber, chargeAccountList):

    if userChargeAccountNumber in chargeAccountList:
        return True
    else:
        return False

# Define the main function to run all the other functions and print the 
# appropriate message
def main():
    
    chargeAccountsfile = open(ACCOUNT_FILE, 'r') # Opens charge_accounts.txt
    chargeAccountsList = readChargeAccountsToList(chargeAccountsfile)
    userChargeAccountNumber = getUserChargeAccountNumber()

    if userChargeAccountNumberExists(userChargeAccountNumber, chargeAccountsList):
        print( '\n' + userChargeAccountNumber, 'exists in', ACCOUNT_FILE + '\n')
    else:
        print( '\n' + userChargeAccountNumber, 'does not exist in', ACCOUNT_FILE + '\n')

main()