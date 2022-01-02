from helpers import *
from basic import *
from fantano import *


def main():
    mode = get_mode()

    if mode == 1:
        user = Fantano()
        pprint(user.saved_albums)
    elif mode == 2:
        user = Basic(mode)
        pprint(user.current_track)
    else:
        pprint("Invalid mode - how did you even get here?")


if __name__ == "__main__":
    main()