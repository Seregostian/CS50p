def main():
    text = convert(input("I love the way you smile!: "))
    print(text)


def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    return text


main()