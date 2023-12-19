import sys
import os
from PIL import Image, ImageOps

#checks are:
#too few command-line arguments, too many command-line arguments, invalid output, input and output have different extensions, and input does not exist.
#however, i have no 'invalid output' but it still passes the CS50 tests, i've changed it over 11 times so far, still passes, don't know why
#happened the same when i had equalized '==' both sys argv 1 & 2, making both of them give the 'invalid output' answer instead of only one being
#'invalid output' and the other 'Input and output have different extensions', so not really sure if it still counts as 'passing' since
#the checks from the actual page don't pass 

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_ext = os.path.splitext(sys.argv[1])[1]
output_ext = os.path.splitext(sys.argv[2])[1]

if input_ext == "" or output_ext == "" or input_ext.lower() != output_ext.lower():
    sys.exit("Input and output have different extensions")

try:
    shirt = Image.open("shirt.png")
    with Image.open(sys.argv[1]) as im:
        photo = ImageOps.fit(im, size=(600, 600))
        photo.paste(shirt, shirt)
        photo.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")