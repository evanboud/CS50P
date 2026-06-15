import inflect
p = inflect.engine()
  
list = []
while True:
    try:
        names = input("Name: ")
        list.append(names)
    except EOFError:
        z = p.join(list)
        
        print(f"Adieu, adieu, to {z}")
        break