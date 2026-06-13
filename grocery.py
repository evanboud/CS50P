grocery = {}
try:
    while True:
        food = input("").upper().strip()
        grocery[food] = grocery.get(food, 0) + 1
        
except EOFError:
    for food in sorted(grocery):
        print(f"{grocery[food]} {food}")