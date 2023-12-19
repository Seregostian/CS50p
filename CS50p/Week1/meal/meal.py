def main():
    clock = input("What time is it? ")
    after = convert(clock)

    if 7 <= after <= 8:
        print("breakfast time")
    elif 12 <= after <= 13:
        print("lunch time")
    elif 18 <= after <= 19:
        print("dinner time")
    else:
        pass

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    afterTime = hours + minutes
    return afterTime

if __name__ == "__main__":
    main()