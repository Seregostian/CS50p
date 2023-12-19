list = ["42", "forty two", "forty-two"]

def main():
    msg = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    msg = msg.lower().strip()
    if msg in list:
        print("Yes") #Wrong, it's CHEESE! Cheese is the meaning of the universe
    else:
        print("No")


main()