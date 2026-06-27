import sys
#input 

#open input file scan how many lines of code than close it



if len(sys.argv) == 1:
    sys.exit("To few command-line arguments")
elif len(sys.argv) > 2: 
    sys.exit("To many command-line arguments")
elif "py" not in sys.argv[1]:
    sys.exit("Not a Python file")
elif len(sys.argv) == 2:
    while True:
        try:
            with open(str(sys.argv[1])) as file:
                lines = file.readlines()
                clean = []
                for line in lines:
                    cleaned = line.lstrip()
                    if cleaned != "":
                        clean.append(cleaned)
                    else:
                        continue
            filetered_lines = [c for c in clean if not c.startswith("#")]
            break
        except FileNotFoundError:
            sys.exit("File does not Exist")

x = len(filetered_lines)
print(x)
    


