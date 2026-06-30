import re
import sys


def main():
    print(count(input("Text: ").lower()))


def count(s):
    s = s.lower()
    ums = re.findall(r"\bum\b", s, flags= re.IGNORECASE)
    ums = ums.count("um")

    return ums


...


if __name__ == "__main__":
    main()