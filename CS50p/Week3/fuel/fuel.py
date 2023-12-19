def get_valid_input():
    while True:
        fuel = input("Fraction: ")

        try:
            x, y = fuel.split("/")
            int_x = int(x)
            int_y = int(y)

            if int_y == 0:
                raise ZeroDivisionError()
#https://www.youtube.com/watch?v=NKmGVE85GUU&ab_channel=TED-Ed quick video for explanation lmao
            if int_x > int_y:
                raise ValueError("The denominator must be greater than or equal to the numerator.")
#https://www.youtube.com/watch?v=8hWnezlQ_lk&ab_channel=ehow and another one
            return int_x, int_y

        except ValueError:
            print("Invalid input. Please enter a valid fraction.")

        except ZeroDivisionError:
            print("Division by zero is not allowed. Please enter a valid fraction.")

int_x, int_y = get_valid_input()

decimal_fuel = int_x / int_y

if decimal_fuel <= 0.01:
    print("E")
elif decimal_fuel >= 0.99 and decimal_fuel <= 1:
    print("F")
elif decimal_fuel > 1:
    print("Invalid input.")
else:
    percentage_fuel = decimal_fuel * 100
    round_p_fuel = round(percentage_fuel)
    print(f"{round_p_fuel}%")
    exit()