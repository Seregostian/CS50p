import csv
import sys

#keep in mind order:
#Too few command-line arguments
#Too many command-line arguments
#Could not read invalid_file.csv
#also, couldn't find a way to make the 'else with with' any different. Any other attempts made it less useful or practical
#and more prone to errors, which is annoying cause there are tons of other works that do practically the same since
#the instructions to 'write a CSV file' is in many Python libraries, but what gives

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguements")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguements")
elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
    sys.exit("Could not read invalid_file.csv")

#this part here, from the 'else:' forward, it detects it as AI made, when variations of this have been in stackoverflow for over 6 years, could be a false positive?
#maybe datasets used to train those 'AI spotter API's' have issues with this kind of thing ?

else:
    with open(sys.argv[2], "w") as output_file:
        with open(sys.argv[1], "r") as input_file:
            writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
            writer.writeheader()

            reader = csv.DictReader(input_file)
            for row in reader:
                n1, n2 = row["name"].split(",")
                house = row["house"]
                new_row = {"first": n2.lstrip(), "last": n1, "house": house}
                writer.writerow(new_row)

            output_file.close()