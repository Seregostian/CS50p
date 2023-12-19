import questions
import options
import answers

def get_questions():
    """Returns a list of questions from the questions.py file."""
    return questions.questions

def get_options():
    """Returns a list of options from the options.py file."""
    return options.options

def get_answers():
    """Returns a list of answers from the answers.py file."""
    return answers.answers

def main():

    tries = []
    final_score = 0
    question_ammount = 0

    questions = get_questions()
    options = get_options()
    answers = get_answers()

    print("")
    print("==========================================================================")
    print(" _                  _          __   _   _             ___        _     _  ")
    print("| |    ___  _ __ __| |   ___  / _| | |_| |__   ___   / _ \ _   _(_)___| | ")
    print("| |   / _ \| '__/ _` |  / _ \| |_  | __| '_ \ / _ \ | | | | | | | |_  / | ")
    print("| |__| (_) | | | (_| | | (_) |  _| | |_| | | |  __/ | |_| | |_| | |/ /|_| ")
    print("|_____\___/|_|  \__,_|  \___/|_|    \__|_| |_|\___|  \__\_\\\__|_|_/___(_)")
    print("==========================================================================")
    print("")
    print("Will you be brave enough to face the challenge?!")
    print("")

    while question_ammount < len(answers):

        print("==========================================================================")
        print(questions[question_ammount])

        for option in options[question_ammount]:
            print(option)

        guess = input("What'll it be? (A, B, C, D): ").upper()
        tries.append(guess)

        if guess == answers[question_ammount]:
            final_score += 1
            print("")
            print("AFFIRMATIVE! Keep going!")

        else:
            print("")
            print("WRONG! But don't give up!")
            print(f"{answers[question_ammount]} was the correct answer")

        question_ammount += 1

    if final_score == 10:
        print("")
        print("=--=--=--=--=--=--=--=--=--=--=--=--==--=--=--=--=--=--=--=--=--=--=--=")
        print("°-0-o-O-o-0-°-=  You've won! You reached The One Ring!  =-°-0-o-O-o-0-°")
        print("=--=--=--=--=--=--=--=--=--=--=--=--==--=--=--=--=--=--=--=--=--=--=--=")

    else:
        print("")
        print("=--=--=--=--=--=--=--=--=--=--=--=--==--=--=--=--=--=--=--=--=--=--=--=")
        print("°-0-o-O-o-0-°-=    You've lost! But keep on trying!     =-°-0-o-O-o-0-°")
        print("=--=--=--=--=--=--=--=--=--=--=--=--==--=--=--=--=--=--=--=--=--=--=--=")

    print("")
    print("==========================================================================")
    print("II                        THE GAME IS OVER !!                           II")
    print("==========================================================================")

    print("")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    print("II                        Thanks for playing!!!!                        II")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")


if __name__ == "__main__":
    main()
