import sys, termios, tty, os

"""Solution by Jon Witt http://www.jonwitts.co.uk/archives/896"""
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

loop = True

while loop:
    char = getch()

    if (char == "p"):
        print("Stop!")
        exit(0)

    if (char == "a"):
        print("Left pressed")

    elif (char == "d"):
        print("Right pressed")

    elif (char == "w"):
        print("Up pressed")

    elif (char == "s"):
        print("Down pressed")

    elif (char == "1"):
        print("Number 1 pressed")

    elif (char == "0"):
        loop = False

    else:
        print("\n" + char + "\n")
