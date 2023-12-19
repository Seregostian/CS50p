camelCase = input("camelCase: ")
print("snake_case: ", end="")
#https://www.youtube.com/watch?v=xvFZjo5PgG0&ab_channel=Duran
for letter in camelCase:
    if letter.isupper():
        print("_" + letter.lower(), end="")
    else:
        print(letter, end="")