from helpers import *
from basic import *
from fantano import *


def main():
    mode = get_mode()

    if mode == 1:
        user = Fantano()
        print(str(user.total_albums) + ' albums in total')
        print(str(len(user.eligible_albums)) + ' albums are eligible')
        print(str(len(user.scored_albums)) + ' albums with a score')
        print('ALL SCORES: ')
        print_results(user.scored_albums)
        print('')
        print('------------------------------------------------------------------------------------')
        print('')
        print('AVERAGE SCORE: ')
        print_avg_score(user.scored_albums)
    elif mode == 2:
        user = Basic(mode)
        pprint(user.current_track)
    else:
        pprint('Invalid mode')

2
if __name__ == "__main__":
    main()