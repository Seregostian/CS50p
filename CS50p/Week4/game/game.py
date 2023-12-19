import random

def guessing_game(level):

  number = random.randint(1, level)

  try:
    guess = int(input("Guess a number!! between 1 and {}: ".format(level)))
  except ValueError:
    print("Invalid guess.")
    guess = int(input("Guess a number!! between 1 and {}: ".format(level)))
#had to add literally the same line but with a value error, kept getting a 'game.py rejects non-numeric guess. expected program to rreject input, but it did not' otherwise'
#the rest is kind of the same, i even checked mine with 2 AI's, and other people's works, practically most of us do a while, if, elif, try, except.
  while guess != number:
    if guess < number:
      print("Too small!")
    else:
      print("Too large!")

    try:
      guess = int(input("Guess again!: "))
    except ValueError:
      print("Invalid guess.")
      guess = int(input("Guess again!: "))

  print("Just right!")

try:
  level = int(input("Enter a level: "))
except ValueError:
  print("Invalid level.")
  level = int(input("Enter a level: "))

while level <= 0:
  print("Invalid level.")
  level = int(input("Enter a level: "))

guessing_game(level)