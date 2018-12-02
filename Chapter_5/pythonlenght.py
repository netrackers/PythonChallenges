#              Maximum length a line of code should have              #
# Function to collect user information and store it in variables

def get_user_information():
    user_firstname = input('Enter your first name: ')
    user_lastname = input('Enter your last name: ')
    user_streetname = input('Enter your street address: ')
    user_city = input('Enter your city: ')
    user_state = input('Enter your state: ')
    user_zip = int(input('Enter your zip code: '))
    print('Thank you ', user_firstname, "!")
    print()
    print('Please verify your information below: ')
    print()
    print(user_firstname, user_lastname + '\n', user_streetname, '\n', 
    user_city + ',', user_state + ',', user_zip)
    
get_user_information()