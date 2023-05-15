#!/usr/bin/python3

from sys import platform
if platform == "linux" or platform == "linux2":
    print("ESTO ES pa LINUZ")
elif platform == "darwin":
    print("Aquesto pa MakOS topijo")
elif platform == "win32":
    print("Y si no, pal güindows")
