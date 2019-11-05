import colorama
from colorama import Fore, Back, Style
colorama.init()
from PIL import Image

def test_user(row_values, row_number, available_numbers):
    user_continue = True
    reappend = False
    # If an artist is listed, ask for it
    if (row_values[3] != ""):
        response = get_answer(row_values[3], row_number, available_numbers, "artist", reappend)
        available_numbers = response[0]
        user_continue = response[1]
        reappend = response[2]
        # If they haven't quit, ask them for the name of the piece
    if (user_continue and row_values[2] != ""):
        response = get_answer(row_values[0], row_number, available_numbers, "name of the piece", reappend)
        available_numbers = response[0]
        user_continue = response[1]
        reappend = response[2]
    # Else if not an art piece, ask for the keyword
    elif (user_continue):
        response = get_answer(row_values[0], row_number, available_numbers, "answer", reappend)
        available_numbers = response[0]
        user_continue = response[1]
        reappend = response[2]
    if (reappend or user_continue == False):
        available_numbers.append(row_number)
    return [available_numbers, user_continue]

def get_answer(correct_answer, row_number, available_numbers, answer_type, reappend):
    user_continue = True
    hint_level = 0
    keep_guessing = True
    correct_answers = correct_answer.split(";")
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
        # If user skips, add the row back into the pool of options
        if (answer.upper() == "S" or answer.upper() == "SKIP"):
            keep_guessing = False
            reappend = True
        elif (answer.upper() == "H" or answer.upper() == "HINT"):
            hint_level = produce_hint(correct_answers[0], hint_level)
        elif (answer.upper() == "Q" or answer.upper() == "QUIT"):
            keep_guessing = False
            user_continue = False
        else:
            correct_response = False
            for correct_answer in correct_answers:
                correct_answer = correct_answer.strip()              # remove whitespace from beginning and end
                print("Answer: " + correct_answer)
                if (answer.upper() == correct_answer.upper()):
                    correct_response = True
            if (correct_response):
                print(Fore.GREEN + "That is correct" + Fore.RESET)
                keep_guessing = False
            else:
                print(Fore.RED + "Sorry, that is incorrect" + Fore.RESET)
    return [available_numbers, user_continue, reappend]

def produce_hint(correct_answer, hint_level):
    if (hint_level < len(correct_answer)):
        hint_level += 1
    hint = list(correct_answer)
    for index in range(hint_level, len(correct_answer)):
        hint[index] = "*"
    print(''.join(hint))
    return hint_level

def get_sheet(sheet_names):
    print("Number of Sheets: ", len(sheet_names))
    sheet_number = 0
    if (len(sheet_names) > 1):
        print("Sheet Names: ")
        idx = 0
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
            if (sheet_number < 0 or sheet_number > len(sheet_names)-1):
                print(Fore.RED + "Please an integer between 0 and " + str(len(sheet_names)-1) + Fore.RESET)
                continue
            else:
                break
    else:
        sheet_number = 0
    return sheet_number

def give_description(row_values):
    # if there is a picture, display it
    if (row_values[2] != ""):
        picture_description(row_values[2])
    # if there is a text description, display it
    if (row_values[1] != ""):
        text_description(row_values[1])
    return

def picture_description(image_link):
    print("Here is the picture: ")
    Image.open(image_link).show()
    return

def text_description(text):
    print(Fore.CYAN + "Here is the description:" + Fore.RESET)
    print(text)
    return