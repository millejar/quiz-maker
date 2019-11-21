
from tkinter import filedialog
import colorama
from colorama import Fore, Back, Style
colorama.init()
from PIL import Image
from math import floor
from os import path

def import_excel():
    # if there is a save file, use the path from the file and ask the user
    #   if they want to use that file or open a new file
    if (path.exists("save_file.txt")):
        file = open("save_file.txt", "r")
        excel_file = file.read()
        # if the file is empty, open a new file
        if (excel_file == ""):
            excel_file = filedialog.askopenfilename()
        else:
            response = input("The current file is " + Fore.YELLOW + excel_file + "\n" + 
            Fore.CYAN + 'Hit Enter to use this file or "F" to use another' + Fore.RESET)
            if (response.upper() == 'F'):
                excel_file = filedialog.askopenfilename()
    # else if there is no save file, open a new file 
    else:
        excel_file = filedialog.askopenfilename()
    # save the file 
    file = open("save_file.txt", "w+")
    file.write(excel_file)
    file.close()
    return excel_file

def test_user(row_values, row_number, available_numbers):
    user_continue = True
    reappend = False
    topics_need_work = []
    # if the keyword is a number convert to string to avoid errors
    if (type(row_values[0]) is float):
        str(row_values[0])
     # extract all possible correct answers (diliminated by ";" into a list)
    correct_answers = row_values[0].split(";")     
    # If an artist is listed, ask for it
    if (row_values[3] != ""):
        response = get_answer(row_values[3].split(";"), row_number, available_numbers, "artist", reappend)
        available_numbers = response[0]
        user_continue = response[1]
        reappend = response[2]
        if (response[3]):
            help_string = ("The artist of " + Style.DIM + Fore.GREEN + 
            correct_answers[0] + Style.RESET_ALL + " is " + Fore.YELLOW + row_values[3] + Fore.RESET)
            topics_need_work.append(help_string)
    # If they haven't quit, ask them for the name of the piece
    if (user_continue and row_values[2] != ""):
        response = get_answer(correct_answers, row_number, available_numbers, "name of the piece", reappend)
        available_numbers = response[0]
        user_continue = response[1]
        reappend = response[2]
        if (response[3]):
            help_string = ("Name of this piece: " + Fore.YELLOW + correct_answers[0] + Fore.RESET)
            topics_need_work.append(help_string)
    # Else if not an art piece and user wants to continue, ask for the keyword
    elif (user_continue):
        response = get_answer(correct_answers, row_number, available_numbers, "answer", reappend)
        available_numbers = response[0]
        user_continue = response[1]
        reappend = response[2]
        if (response[3]):
            help_string = ("The keyword: " + Fore.YELLOW + correct_answers[0] + Fore.RESET)
            topics_need_work.append(help_string)
    if (reappend or user_continue == False):
        available_numbers.append(row_number)
    
    return [available_numbers, user_continue, topics_need_work]

def get_answer(correct_answers, row_number, available_numbers, answer_type, reappend):
    user_continue = True
    hint_levels = 0
    keep_guessing = True
    needed_help = False
    while (keep_guessing == True):
        while True:
            # Ask for and validate user input
            try: 
                answer = input(Fore.CYAN + "What is the " + answer_type + "?" + Fore.RESET
                + Style.DIM + " (or enter H for a Hint, S to Skip, or Q to Quit): " 
                + Style.RESET_ALL + "\n")
                break
            except: 
                print(Fore.RED + "Please enter a valid response" + Fore.RESET)
                continue
        # First check if a user wants to skip, get a hint, or quit
        if (answer.upper() == "S" or answer.upper() == "SKIP"):     # If user skips, add the row back into the pool of options
            keep_guessing = False
            reappend = True
        elif (answer.upper() == "H" or answer.upper() == "HINT"):
            hint_levels = give_hint(correct_answers[0], hint_levels)
            needed_help = True
        elif (answer.upper() == "Q" or answer.upper() == "QUIT"):
            keep_guessing = False
            user_continue = False
            needed_help = True
        # Else if a guess is given, check for accuracy
        else:
            correct_response = False
            for correct_answer in correct_answers:
                correct_answer = correct_answer.strip()              # remove whitespace from beginning and end
                if (answer.upper() == correct_answer.upper()):
                    correct_response = True
            if (correct_response):
                print("\n" + Fore.GREEN + correct_answers[0] + Fore.RESET)
                print(Fore.GREEN + "That is correct" + Fore.RESET)
                keep_guessing = False
            else:
                print(Fore.RED + "Sorry, that is incorrect" + Fore.RESET)
                needed_help = True
    return [available_numbers, user_continue, reappend, needed_help]

def give_hint(correct_answer, hint_levels):
    if (hint_levels % 2 == 0):
        if (hint_levels <= (len(correct_answer)/2)):
            hint_levels += 1
    else:
        if (hint_levels <= floor((len(correct_answer)/2))):
            hint_levels += 1
    unmasked_positions = []
    for hint_level in range(hint_levels):
        if (hint_level % 2 == 0):
            unmasked_positions.append(hint_level)
            unmasked_positions.append(hint_level + 1)
        else:
            unmasked_positions.append(len(correct_answer) - hint_level)
            unmasked_positions.append(len(correct_answer) - hint_level - 1)

    hint = list(correct_answer)
    for index in range(len(correct_answer)):
        if index not in unmasked_positions:
            hint[index] = "*"
    print(''.join(hint))

    return hint_levels

def get_sheet(sheet_names):
    sheet_number = 1
    if (len(sheet_names) > 1):
        print("Sheet Names: ")
        idx = 1
        for sheet_name in sheet_names:
            print("Number: ", Fore.GREEN, idx, Fore.RESET, " Name: ", Fore.GREEN, 
            sheet_name, Fore.RESET)
            idx += 1
        while True: 
            try: 
                sheet_number = int(input((Fore.CYAN + "Enter the number of the sheet you" +
                " would like to use: " + Fore.RESET)))
            except:
                print(Fore.RED + "Please enter an integer" + Fore.RESET)
                continue
            if (sheet_number < 1 or sheet_number > len(sheet_names)):
                print(Fore.RED + "Please an integer between 1 and " + str(len(sheet_names)) + Fore.RESET)
                continue
            else:
                break
    else:
        sheet_number = 1
    sheet_number -= 1 
    return sheet_number

def give_description(row_values):
    # if there is a picture, display it
    if (row_values[2] != ""):
        print("Here is the picture: ")
        Image.open(row_values[2]).show()
    # if there is a text description, display it
    if (row_values[1] != ""):
        print(Fore.CYAN + "Here is the description:" + Fore.RESET)
        print(row_values[1])
    return
