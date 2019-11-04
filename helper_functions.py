import colorama
from colorama import Fore, Back, Style
colorama.init()

def user_answer(correct_answer, random_row, available_numbers):
    user_continue = True
    keep_guessing = True
    hint_level = 0
    while (keep_guessing == True):
        while True:
            try: 
                answer = input(Fore.CYAN + "What is the answer?" + Fore.RESET 
                + Style.DIM + " (or enter H for a Hint, S to Skip, or Q to Quit): " 
                + Style.RESET_ALL + "\n")
                break
            except: 
                print(Fore.RED + "Please enter a valid response" + Fore.RESET)
                continue
        if (answer.upper() == "S" or answer.upper() == "SKIP"):
            keep_guessing = False
            available_numbers.append(random_row)
        elif (answer.upper() == "H" or answer.upper() == "HINT"):
            hint_level = produce_hint(correct_answer, hint_level)
        elif (answer.upper() == "Q" or answer.upper() == "QUIT"):
            keep_guessing = False
            user_continue = False
        elif (answer.upper() == correct_answer.upper()):
            print(Fore.GREEN + "That is correct" + Fore.RESET)
            keep_guessing = False
        else:
            print(Fore.RED + "Sorry, that is incorrect" + Fore.RESET)
    return [available_numbers, user_continue]

def produce_hint(correct_answer, hint_level):
    if (hint_level < len(correct_answer)):
        hint_level += 1
    hint = list(correct_answer)
    for index in range(hint_level, len(correct_answer)):
        hint[index] = "*"
    print(''.join(hint))
    return hint_level
