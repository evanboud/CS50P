import inflect
p = inflect.engine()
  
adieu = []
while True:
    try:
        names = input("Name: ")
        adieu.append(names)
    except EOFError:
        z = p.join(adieu)
        print(f"Adieu, adieu, to {z}")
        break