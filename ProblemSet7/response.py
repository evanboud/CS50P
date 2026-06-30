import validators

user_input = input("What's your email address: ")
validated_email = validators.email(user_input)
if validated_email == True:
    print("Valid")
else:
    print("Invalid")
