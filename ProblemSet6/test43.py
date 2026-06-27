import os
import sys
from PIL import Image, ImageOps

shirt = Image.open("shirt.png")
before = Image.open("before1.jpg")
size = shirt.size
print(size)