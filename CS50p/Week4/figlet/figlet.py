import sys
from pyfiglet import Figlet
import random

figlet = Figlet()


if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandomFont = False
else:
    print("Invalid use")
    sys.exit(1)

a = figlet.getFonts()
b = random.choice(a)
#code was redone three times, one was way shorter but had output errors on slanted text.
if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid use")
        sys.exit(1)
else:
    figlet.setFont(font=(b))
#ran a little fix on AI to check for typos and miss-concatenated arguments, just to make sure, and it got fixed pretty fast.
msg = input("Input: ")

print("Output:")
print(figlet.renderText(msg))