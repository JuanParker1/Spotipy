from helpers import *
from basic import *
from fantano import *
import os

def main():
    mode = get_mode()
    print('')

    if mode == 1:
        user = Fantano()
        user.get_eligible_albums()
        user.get_scores_2020s()
        user.get_user_scores()
        print(str(user.total_albums) + ' albums in total')
        print(str(len(user.eligible_albums)) + ' albums are eligible')
        print(str(len(user.scored_albums)) + ' albums with a score')
        print('')
        print('ALL SCORES: ')
        print_results(user.scored_albums)
        print('')
        print('------------------------------------------------------------------------------------')
        print('')
        print_score_data(user.scored_albums)
        print('')
        print('------------------------------------------------------------------------------------')
        print('')
        # print('UNSCORED: ')
        # print_unscored_albums(user.eligible_albums)
    elif mode == 2:
        get_currently_playing_track()
    elif mode == 3:
        get_user_top_artists()
    elif mode == 4:
        get_user_top_tracks()
    else:
        print('Invalid mode')

    # remove user permissions
    if os.path.exists('.cache'):
        os.remove('.cache')

    return


if __name__ == "__main__":
    main()
