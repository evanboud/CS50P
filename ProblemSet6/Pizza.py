import sys
from tabulate import tabulate
import csv
#input

#open input file scan how many lines of code than close it

user_input = (sys.argv)

if len(sys.argv) == 1:
    sys.exit("To few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("To many command-line arguments")
elif "csv" not in sys.argv[1]:
    sys.exit("Not a Python file")
elif len(sys.argv) == 2:
    pizzas = []
    try:
        if "lar" in user_input[1]:
            with open(str(user_input[1])) as csvfile:
                csv_read = csv.DictReader(csvfile)
                for row in csv_read:
                    pizzas.append({"Regular Pizza": row["Regular Pizza"], "Small": row["Small"], "Large": row["Large"]})
                print(tabulate(pizzas, headers="keys", tablefmt="grid"))
        else:
            with open(str(user_input[1])) as csvfile:
                csv_read = csv.DictReader(csvfile)
                for row in csv_read:
                    pizzas.append({"Sicilian Pizza": row["Sicilian Pizza"], "Small": row["Small"], "Large": row["Large"]})
                print(tabulate(pizzas, headers="keys", tablefmt="grid"))
    except Exception as e:
        print(e)
        sys.exit("File not found")
