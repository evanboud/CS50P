import validators

def main():
        try:
            user_input = input("What's your email address: ")
            validated_email = validating(user_input)
            print(validated_email)
        except AssertionError:
            print("Invlaid")

            
    
def validating(user_input):
        validated_email = validators.email(user_input)
        if validated_email == True:
            return "Valid"
        else:
            raise AssertionError
   
    

if __name__ == "__main__":
    main()