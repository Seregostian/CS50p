greetings = input("Greetings valued customer: ").strip()

#would also love to add 'What's shakin bacon' as a greeting, definitely professional

if greetings.startswith("Hello"):
    print("$0")
elif greetings.startswith("H"):
    print("$20")
else:
    print("$100")