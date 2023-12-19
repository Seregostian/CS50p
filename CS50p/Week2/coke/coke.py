due = 50
print("Amount Due:", due)

while due > 0:
    coin = int(input("Insert a coin: "))
    if coin not in [5, 10, 25]:
        print("Amount Due:", due)
    else:
        due -= coin
        if due < 0:
            change_owed = abs(due)
            print("Change Owed:", change_owed)
            break
        elif due == 0:
            print("Change Owed:", due)
            break
        else:
            print("Amount Due:", due)