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

    if (char == "0" or char == "000"):
        loop = False
    else:
        # print("", type(ord(char)))
        print("", char)
        # compare = "\x1b[A"
        compare = "A"
        # print(compare)

        if char == compare:
            print("Key matched!")



