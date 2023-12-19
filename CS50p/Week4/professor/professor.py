import contextlib
import random


def main():
  level = get_level()
  generate_integer(level)


def get_level():
  while True:
    with contextlib.suppress(ValueError):
      level = int(input("Level: "))
      if level in {1, 2, 3}:
        return level
      else:
        raise ValueError

#had to add a contextlib since i saw it in a few other examples, and it proved to be very very useful
#had to check how it worked, i kept missplacing the ValueError raise, i guess one learns something new everyday

def generate_integer(level):
  user_score = 0
  for _ in range(1, 11):
    if level == 1:
      X = random.randint(0, 9)
      Y = random.randint(0, 9)
    elif level == 2:
      X = random.randint(10, 99)
      Y = random.randint(10, 99)
    else:
      X = random.randint(100, 999)
      Y = random.randint(100, 999)

#tried a def sum_error(x, y, z) and failed misserably
#tried yet another def generate_integer(level): also failed
# using a for _ in range proved to be useful but a bit longer than i expected

    user_tries = 1
    while user_tries <= 3:
      try:
        user_answer = int(input(f"{X} + {Y} = "))
      except ValueError:
        print("EEE")
        user_tries += 1
        continue
      else:
        real_answer = X + Y
        if user_answer == real_answer:
          user_score += 1
          break
        else:
          print("EEE")
          if user_tries == 3:
            print(f"{X} + {Y} = {real_answer}")
          user_tries += 1
  print()
  print(f"Score: {user_score}")

#checked my results with 3 other friends, we all did something quite similar, only i made it a bit longer but more readable, and they made it way shorter and precise

if __name__ == "__main__":
  main()