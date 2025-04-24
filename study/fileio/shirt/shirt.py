



import sys
import os
from PIL import Image, ImageOps

def main():
    # check for correct # of arguments and correct file types
    if len(sys.argv) != 3:
        sys.exit("program needs three arguments")
    if not os.path.exists(sys.argv[1]):
        sys.exit("file does not exist")
    if not sys.argv[1].endswith((".jpg", ".jpeg", ".png")):
        sys.exit("extension must be .jpg .jpeg or .png")

    shirt = Image.open("shirt.png")
    size = (150, 100)
    # open image with Image.open()
    with Image.open(sys.argv[1]) as im:
    # crop the input with ImageOps.fit using default values for method, bleed, and centering
        ImageOps.fit(im, size) 
        im.paste(shirt)
        im.save(sys.argv[2])
    # overlay the shirt with Image.paste

    # save the result with Image.save


if __name__ == "__main__":
    main()
