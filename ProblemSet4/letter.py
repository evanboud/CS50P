from pyfiglet import Figlet
import sys
import random 
figlet = Figlet()
fonts = figlet.getFonts()
if len(sys.argv) not in [1, 3]:
   sys.exit("Invalid Usage")
else:
    if len(sys.argv) == 1:
        user_input = input("Input: ")
        x =random.choice(fonts)
        figlet.setFont(font=x)
        print(f"Output: \n{figlet.renderText(user_input)}", end="")
    elif len(sys.argv) == 3 and sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid Usage")
    else:
        y = sys.argv[2]
        if y not in fonts:
            sys.exit("Invalid Usage")
        else:
            user_input = input("Input: ")
            figlet.setFont(font=y)
            print(f"Output: \n{figlet.renderText(user_input)}")

