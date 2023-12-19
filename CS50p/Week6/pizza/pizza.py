import sys
import argparse
import os.path
from tabulate import tabulate

#the more i checked this code with AI, the more imports i added
#ended up adding a os.path to change a prefix, suffix line
#also editing the 'Check if CSV' will break the code, so approach with caution

def main():
    parser = argparse.ArgumentParser(description='Check if CSV')
    parser.add_argument('filename')
    args = parser.parse_args()

    filename = args.filename
    file_extension = os.path.splitext(filename)[1]

    if file_extension != '.csv':
        sys.exit('Not a CSV file')

    try:
        with open(filename) as file:
            lines = file.readlines()
            print(tabulateFile(lines))
    except FileNotFoundError:
        sys.exit('File does not exist')


def tabulateFile(lines):
    x = []
    for line in lines:
        item = line.rstrip().split(',')
        x.append(item)
    return tabulate(x, headers='firstrow', tablefmt='grid')


if __name__ == '__main__':
    main()