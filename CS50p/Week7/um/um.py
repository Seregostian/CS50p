import re
import sys

def main():
    print(count(input("Text: ").strip()))


def count(s):
    count=re.findall(r'\bum\b', s, re.IGNORECASE) #had ot add an IGNORECASE, and shorten the original re.findall(r"/b/W*um/W:", s) because it was too buggy otherwise
    return len(count)


if __name__ == "__main__":
    main()