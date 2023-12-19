input_user = input("Input:")
new_string = ""

for character in input_user:
    if character not in "aeiouAEIOU":
        new_string += character

print("Output:", new_string)