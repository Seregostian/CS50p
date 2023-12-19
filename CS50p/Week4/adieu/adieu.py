list=[]

result = " "

while True:

    try:
        message=input().title().strip()

    except (KeyboardInterrupt, EOFError):
        break

    list.append(message)

for i, item in enumerate(list):

    if len(list) > 2:

        if i==len(list) - 1:
            result += "and " + item

        elif i==len(list) - 2:
            result += item + ", "

        else:
            result += item + ", "

#This code is both uncomfortably long and needlessly extended. not very sure why it won't comply if i do it like this :
#result = ", ".join(list[:-1]) + (f" and {list[-1]}" if len(list) > 1 else ""), it reprompts into an error and won't add the new names, only
#the adieu adieu without the names (luisa, liesl, friedrich, etc) which is quite annoying

    elif len(list) == 2:

        if i==len(list) - 1:
            result += "and " + item

        else:
            result += item + " "

    else:
        result += item


print(f"Adieu, adieu, to{result}")