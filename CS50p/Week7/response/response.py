from validator_collection import validators, errors

email = input("Insert e-mail address: ")

try:
    email_address = validators.email(email, allow_empty = False)  # literally just made a validators.email
    print("Valid")                                                # print
except errors.InvalidEmailError:                                  # then invalidemailerrror
    print("Invalid")                                              # print. no idea how to make it shorter, its just 9 lines as it is lmao