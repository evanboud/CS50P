import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"^(\b(?:\d|1[0-2]):[0-5]\d (?:AM|PM)?|(?:(?:1[0-2]|\d)\s(?:(?:AM)|(?:PM)))\b) to (\b(?:\d|1[0-2]):[0-5]\d (?:AM|PM)?|(?:(?:1[0-2]|\d)\s?(?:(?:AM)|(?:PM)))\b)$",s):
            time1 = match.group(1)
            time2 = match.group(2)
            if "PM" in time1:
                time1 = time1.replace("PM",""). replace(":",".")
                time1 = float(time1)
                time1 = time1 + 12
                time1 = str(f"{time1:.2f}").replace(".",":")
            elif "AM" in time1:
                time1 = time1.replace("AM","").replace(":",".")
                time1 = float(time1)
                time1 = str(f"{time1:.2f}").replace(".",":")
                time1 = f"{time1:02}".zfill(5)
            if "PM" in time2:
                time2 = time2.replace("PM","").replace(":",".")
                time2 = float(time2)
                time2 = time2 + 12
                time2 = str(f"{time2:.2f}").replace(".",":")
            elif "AM" in time2:
                time2 = time2.replace("AM","").replace(":",".")
                time2 = float(time2)
                time2 = str(f"{time2:.2f}").replace(".",":")
                time2 = f"{time2:02}".zfill(5)
            if time1 == "12:00":
                time1 = "00:00"
            if time2 == "24:00":
                time2 = "12:00"
            return time1 + " to " + time2
    else:
        raise ValueError
        
        


if __name__ == "__main__":
    main()