import random
import time
from colorama import init, Fore, Style

init(autoreset=True)

questions = ["Should I go for pizza tonight?", "Will it rain tomorrow?", "Should I take a vacation soon?"]
answers = [Fore.GREEN + "Yes, definitely!", Fore.CYAN + "It is decidedly so.", Fore.MAGENTA + "Without a doubt!", Fore.YELLOW + "Reply hazy, try again.", Fore.YELLOW + "Ask again later.", Fore.RED + "My sources say no.", Fore.RED + "Outlook not so good.", Fore.RED + "Better not tell you now.", Fore.RED + "Very doubtful."]

def ask_question():
    question = input("Ask me a yes/no question: ")
    return question

def get_answer():
    return random.choice(answers)

while True:
    user_input = input("Do you want to ask a question? (yes/no): ")
    if user_input.lower() == "yes":
        question = ask_question()
        print("Thinking...")
        time.sleep(2)
        print("The answer is:")
        print(get_answer())
    elif user_input.lower() == "no":
        print(Fore.BLUE + "Okay, see you later!")
        break
    else:
        print(Fore.RED + "Invalid input. Please enter 'yes' or 'no'.")
