#inputs a name in camel case
def main():
   camel = input("camelCase: ")
   Snake = snake_case(camel)
   print(f"snake_case: {Snake}")

   

#converts a name into snake case

def snake_case(camel):
    x ="" 
    for i in camel: 
        if i.isupper():
            x = x + "_" + i
        else: 
            x = x + i
    return x 
    
main()
        
        


#prints the name in snake case