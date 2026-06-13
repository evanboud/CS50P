#Prompts the user for a fraction x/y (x non negative int, y postiive int)
#Outputs percent left in tank
def main():
        while True:
            try:   
                x,y = (input("Fraction: ")).split("/")
                x = int(x) 
                y = int(y)
                x_is_valid = x >= 0
                y_is_valid = y > 0 
                z_is_valid = x <= y
                
                if x_is_valid and y_is_valid and z_is_valid:
                    fuel_left = fuel_convert(x,y)
                    print(f"{fuel_left}")
                    break
            except(ValueError, ZeroDivisionError):
                continue


#reprompted if give an error
    

#Converts fraction to a percent
def fuel_convert(x,y):
    fuel_left = (x/y) * 100
    fuel_left = int(fuel_left)
    if fuel_left <= 1:
        return "E"
    elif fuel_left >= 99 and fuel_left <= 100:
        return "F"
    return (f"{fuel_left}%")

main()