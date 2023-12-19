import sys

#too few first
#then too many
#then the 'py' check


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

#this try segment changed several times, got enough feedback on it to make it as short and precise as i wanted
#hope y'all appreciate it cause it costed some blood sweat & tears lmao

try:
    with open(f"{sys.argv[1]}", "r") as f:
        count = sum(1 for line in f if line.strip() and not line.strip().startswith("#"))
        print(count, end="")

except FileNotFoundError:
    sys.exit("File Does Not Exist")