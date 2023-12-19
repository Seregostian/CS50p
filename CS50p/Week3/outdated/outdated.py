def main():
    date = get_formated_date()
    print(date)

def get_formated_date():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    while True:
        try:
            user_input = input('Date: ').split('/')
            length = len(user_input)
            if(length == 3):
               month,day,year = map(int, user_input)
               if (day >= 1 and day <= 31) and (month >= 1 and month <= 12) and (year >= 1):
                   return f"{year}-{month:02}-{day:02}"
            elif length == 1:
                parts = user_input[0].split(',')
                if(len(parts) != 2):
                    raise ValueError
#this part was redone 3 times and ran through 2 AI code assistants (because i kept failing at what i wanted to achieve)
#damn i hope it's right now lol
                month,day,year = ''.join(parts).split()
                day = int(day)
                month = int(months.index(month) + 1)
                year = int(year)
                if (day >= 1 and day <= 31) and (year >= 1 ):
                   return f"{year}-{month:02}-{day:02}"
        except ValueError:
            pass
        except (KeyboardInterrupt, EOFError):
            return ''


main()