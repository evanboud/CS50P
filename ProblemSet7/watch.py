
import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
  match  = re.search(r"(https?)://(?:www\.)?youtube\.com/embed/(.+)", s)
  if match:
    s = re.sub(r"(https?)://(?:www\.)?youtube\.com/embed/(.+)",r"\1://youtu\.be/\2",s)
    match2 = re.search(r'(?:https?)://youtu\\.be/([^<>"]+)',s)
    return match2.group(0)

if __name__ == "__main__":
    main()