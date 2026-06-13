#Input in a 9/8/1636 or September 8, 1636 format
month = [
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
        month_day_year = input("Date:")
        if "/" in month_day_year:
            parts = month_day_year.split("/")
            if len(parts) != 3:
                continue
            else:
                parts[1] = int(parts[1])
                parts[0] = int(parts[0])
                Part1_valid = parts[1] > 0 and parts[1] < 32
                Part0_valid = parts[0] > 0 and parts[0] < 13
                if Part1_valid and Part0_valid: 
                    parts[1] = str(parts[1])
                    parts[0] = str(parts[0])
                    parts[1] = (parts[1]).zfill(2)
                    parts[0] = (parts[0]).zfill(2)
                    rejoined = "-".join([parts[2], parts[0], parts[1]])
                    print(rejoined)
                    break
        else:
            parts2 = month_day_year.split(", ")
            if len(parts2) != 2:
                continue 
            else:
                x,y = parts2[0].split(" ")
                x = month.index(x) + 1
                y = int(y)
                x = int(x)
                x_valid = x < 13 and x > 0
                y_valid = y > 0 and y < 32
                if x_valid and y_valid:
                    x = str(x).zfill(2)
                    y = str(y).zfill(2)
                    listss = [parts2[1], x, y]
                    refurbished = "-".join([listss[0], listss[1], listss[2]])
                    print(refurbished)
                    break
    except: 
        continue 
    
    
    



#output said input in YYYY-MM-DD