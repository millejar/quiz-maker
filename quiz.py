import xlrd
import colorama
from colorama import Fore, Back, Style
colorama.init()
import helper_functions
excel_file = (r'D:\Documents\Quiz Data Files\Greece.xlsx')
# Open the workbook
try: 
    xl_workbook = xlrd.open_workbook(excel_file)
except: 
    print(Fore.RED + "Could not open excel file" + Fore.RESET)

# Retrieve and print the sheetnames
sheet_names = xl_workbook.sheet_names()
sheet_number = helper_functions.get_sheet(sheet_names)

# You can either open a sheet by name or by index
xl_sheet = xl_workbook.sheet_by_index(sheet_number - 1)

# Print the first column
first_column = xl_sheet.col(0)

import random
print ("\n ******************************* \n")
print(Fore.CYAN + Style.BRIGHT + "Welcome to the quiz!\n" + Style.RESET_ALL)
user_continue = True
# Develop the list of available rows 
available_numbers = []
for number in range(1, xl_sheet.nrows):
    available_numbers.append(number)
while (user_continue == True): 
    print("\n ******* \n")
    # Pick a random row from available_numbers, then remove it
    row_number = random.choice(available_numbers)
    available_numbers.remove(row_number)
    # Print the correct answer
    correct_answer = xl_sheet.cell_value(row_number, 0)
    # Print the description
    helper_functions.give_description(xl_sheet.row_values(row_number))
    # Ask for the answer 
    response = helper_functions.test_user(xl_sheet.row_values(row_number), row_number, available_numbers)
    available_numbers = response[0]
    user_continue = response[1]
    # If all clues have been used up, finish the game, else ask the user if they wish to continue
    if (available_numbers == []):
        print(Fore.YELLOW + "You've answered every clue! Congratulations!" + Fore.RESET)
        break
    if (user_continue == False):
        break

print("Thanks for playing!")
                
