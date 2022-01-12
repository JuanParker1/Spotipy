from helpers import *
from basic import *
from fantano import *


def main():
    mode = get_mode()

    if mode == 1:
        user = Fantano()
        pprint(str(user.total_albums) + " albums in total")
        pprint("ELIGIBLE ALBUMS (" + str(len(user.eligible_albums['title'])) + "):")
        print_albums(user.eligible_albums)
        # pprint("")
        # pprint("INELIGIBLE ALBUMS (" + str(len(user.ineligible_albums['title'])) + "):")
        # print_albums(user.ineligible_albums)
        pprint("temp debugging")
    elif mode == 2:
        user = Basic(mode)
        pprint(user.current_track)
    else:
        pprint("Invalid mode - how did you even get here?")


if __name__ == "__main__":
    main()