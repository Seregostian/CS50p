def main():

    m = int(input("Insert your mass "))
    E = m * square(m)
    print(E)


def square(c):
    c = 300000000
    return pow(c, 2)


main()