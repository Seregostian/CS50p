def main():

#All vanity plates must start with at least two letters.
#… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#Numbers cannot be used in the middle of a plate; they must come at the end.
#For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’
#No periods, spaces, or punctuation marks are allowed.

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if s.isalnum() == False:
        return False

    for letter in range(2):
        if s[letter].isalpha() == False:
            return False

    if s.isalpha():
        return True

    char = 0
    while len(s) > char:
        if s[char].isalpha() == False:
            if s[char] == "0":
                return False
            else:
                break
        char += 1


    for num in range(len(s)):
        if s[num].isalpha() == False:
            save_range = num
            break
    for num in range(save_range, len(s)):
        if s[num].isalpha() == True:
            return False
    return True

if __name__ == "__main__":
 main()