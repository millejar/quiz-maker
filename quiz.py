import xlrd
import colorama
from colorama import Fore, Back, Style
colorama.init()
import helper_functions
import sys
excel_file = helper_functions.import_excel_minimalist()
print("File Path: " + excel_file)

# Open the workbook
try: 
    xl_workbook = xlrd.open_workbook(excel_file)
except: 
    print(Fore.RED + "Could not open excel file" + Fore.RESET)

# Retrieve and print the sheetnames
sheet_names = xl_workbook.sheet_names()
sheet_number = helper_functions.get_sheet(sheet_names)
# You can either open a sheet by name or by index
xl_sheet = xl_workbook.sheet_by_index(sheet_number)

# Test the sheet to make sure it has (at least) 4 valid columns and two valid rows. 
try:
    for col_number in range(0,3):
        test = xl_sheet.cell_value(1, col_number)
        print(test)
except:
    print(Fore.RED + "The provided sheet does not fit the required format. " +
    "Please use the template and fill in the rows with data." + Fore.RESET)
    sys.exit(1)

import random
print ("\n ******************************* \n")
print(Fore.CYAN + Style.BRIGHT + "Welcome to the quiz!\n" + Style.RESET_ALL)
user_continue = True
# Develop the list of available rows 
available_numbers = []
topics_to_work_on = []
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
    # if user needed a hint or quit when answering the question, add that topic to the list of topics to work on
    if (response[2]):
        for topic in response[2]:
            topics_to_work_on.append(topic)

    # If all clues have been used up, finish the game, else ask the user if they wish to continue
    if (available_numbers == []):
        print("\n" + Fore.CYAN + "You've answered every topic in the quiz." + Fore.RESET)
        break
    if (user_continue == False):
        break

if (topics_to_work_on):
    print("\n" + Fore.LIGHTYELLOW_EX + "Here are the topics you did not answer correctly " +
    "the first time and without hints:" + Fore.RESET)
    for topic in topics_to_work_on:
        print(topic)
else:
    print(Fore.LIGHTYELLOW_EX + "You answered every topic without using any hints. Nice Work!" + Fore.RESET)

print("\n" + Fore.GREEN + "Thanks for playing!")
                
