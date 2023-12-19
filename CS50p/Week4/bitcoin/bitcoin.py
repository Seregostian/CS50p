#made first part by watching several does do the if len(sys.argv) and if len(argv), quite straightforward
#also tried to do the second part in while True, but using a try except proved to be more useful
#keep in mind this version is way shorter and efficient than previous versions i tried both alone and with friends

import requests
from sys import argv, exit

if len(argv) != 2:
    exit("Missing command-line argument")

try:

    btc_price = requests.get(
        "insert link here dot json"
    ).json()["bpi"]["USD"]["rate_float"]

    bitcoins = float(argv[1])

except (requests.RequestException, KeyError, ValueError):
    exit("Command-line argument is not a number")

print(f"${bitcoins * btc_price:,.4f}")