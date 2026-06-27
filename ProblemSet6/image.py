import os
import sys
from PIL import Image, ImageOps

user_input = (sys.argv)
shirt = Image.open("shirt.png")
x,y = os.path.splitext(sys.argv[1])
z,t = os.path.splitext(sys.argv[2])

if t != y:
    sys.exit("Input and output have different extensions")
elif len(sys.argv) < 2:
    sys.exit("To few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("To many command-line arguments")
elif y not in [".png", ".jpg", ".jpgs"]:
    sys.exit("Invalid file type")
elif len(sys.argv) == 3:
    try:
        with Image.open(sys.argv[1]) as img:
                upper_left = (0,0)
                img2 = ImageOps.fit(img, (600, 600))
                img2.paste(shirt, upper_left, mask=shirt)
                img2.save(sys.argv[2])
                print(img2)
    except Exception as e:
            print(e)
            sys.exit("File not found")
            
     