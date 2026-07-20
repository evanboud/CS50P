from datetime import datetime
from datetime import date
import inflect
import sys
p = inflect.engine()
class Date_convert:
    def __init__(self, Date_Of_Birth, today):
        self.Date_Of_Birth = Date_Of_Birth
        self.today = today
        delta  = self.today - self._Date_Of_Birth
        self.delta = delta.days * 24 * 60
    def __str__(self):
        return f"{p.number_to_words(self.delta, andword="").capitalize()} minutes"
#Neeed to convert into minutes then used the sub overload to subtract then spit out could use a class method maybe?
    @property
    def Date_Of_Birth(self):
        return self._Date_Of_Birth
    @Date_Of_Birth.setter 
    def Date_Of_Birth(self, Date_Of_Birth):
        if not Date_Of_Birth:
            sys.exit(ValueError)
        elif not "-" in Date_Of_Birth:
            sys.exit(ValueError)
        format = "%Y-%m-%d"
        self._Date_Of_Birth = datetime.strptime(Date_Of_Birth, format).date()
        
def main():
    converted = convert()
    print(converted)
def convert():
    Date_Of_Birth = input("Date Of Birth: ")
    today = date.today()
    
    return Date_convert(Date_Of_Birth, today)

if __name__ == "__main__":
    main()