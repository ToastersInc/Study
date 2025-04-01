import sys
from pyfiglet import Figlet


def main():
    # check for command line arguements
    if len(sys.argv) == 1:
        f = Figlet()
        print(f.renderText(input("Input: ")))
    elif len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("second argument must be -f or --font")

        available_fonts = Figlet().getFonts()

        if sys.argv[2] not in available_fonts:
            sys.exit(f"{sys.argv[2]} is not a valid font")
        f = Figlet(font=sys.argv[2])
        print(f.renderText(input("Input: ")))
    else:
        sys.exit("arguements must be: figlet.py -f desired-font")


if __name__ == "__main__":
    main()
