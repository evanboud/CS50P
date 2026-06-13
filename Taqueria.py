def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    menu = {food.lower(): value for food, value in menu.items()}

    x = 0
    while True: 
        try: 
            ordered = input("Item: ").strip().lower()
            value = menu.get(ordered)
            if value is not None:
                total = x + value
                x = total
                print(f"${total:.2f}")
            else:
                continue
        except KeyError:
            pass
        except EOFError:
            break
        


main()