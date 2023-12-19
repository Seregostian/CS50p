groceries = {}
#yet again another while true, i forgot to add the .upper, i had a dude point it out for me
#also keep in mind this is tremendously basic, as my original code was somewhere around 25 lines long, which it shouldn't, this one is way faster and precise
while True:
    try:
        item = input().upper()
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1
    except EOFError:
        for item in sorted(groceries):
            print(groceries[item], item)
        break