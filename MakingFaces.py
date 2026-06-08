
#converts emojis to text and text to emojis
conversions = { ":)": "😊", ":(": "😢" }

text= input()

for key, value in conversions.items():
    text = text.replace(key, value)
#Sottext = input()in a variable and prints it

print(text)