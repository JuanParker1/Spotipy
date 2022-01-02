from pprint import pprint


def get_mode():
    mode = 0
    print("Program options:")
    print("  1. Show the user's Fantano data")
    print("  2. Show the user's currently playing track")
    mode = int(input("Enter a mode: "))

    while True:
        if (mode >= 1) and (mode <= 2):
            break
        else:
            mode = int(input("Invalid input - please try again: "))

    return mode


