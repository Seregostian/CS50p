import emoji

try:
    user_answer = input("Input: ")
    output = emoji.emojize('Output ' + user_answer, language='alias')

    if user_answer == output:
        print("Invalid emoji code.")
    else:
        print("Output:", output)

except Exception as e:
    print("An error occurred:", e)