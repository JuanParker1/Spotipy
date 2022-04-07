import config
import spotipy
from spotipy import SpotifyOAuth


def get_currently_playing_track():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.client_id,
                                                   client_secret=config.client_secret,
                                                   redirect_uri='http://localhost:8080',
                                                   scope='user-read-currently-playing'))

    current_track = sp.current_user_playing_track()

    if current_track is None:
        print('User is not currently playing a track')
        return

    title = current_track['item']['name']
    artists = ' & '.join(artist['name'] for artist in current_track['item']['artists'])
    link = current_track['item']['external_urls']['spotify']

    print(title + ' by ' + artists + '. URL: ' + link)

    return


def get_user_top_artists():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='6e3550b5fd0c40689e3ebb36d7b5ada2',
                                                   client_secret='c8ec0360316c43b4ac8dc4908378c2c5',
                                                   redirect_uri='http://localhost:8080',
                                                   scope='user-top-read'))

    short_term = sp.current_user_top_artists(limit=10, offset=0, time_range='short_term')
    medium_term = sp.current_user_top_artists(limit=10, offset=0, time_range='medium_term')
    long_term = sp.current_user_top_artists(limit=10, offset=0, time_range='long_term')

    print('')
    print('Short term top artists: ')
    num = 1
    for i in short_term['items']:
        print(str(num) + '. ' + i['name'])
        num += 1

    print('')
    print('Medium term top artists: ')
    num = 1
    for i in medium_term['items']:
        print(str(num) + '. ' + i['name'])
        num += 1

    print('')
    print('Long term top artists: ')
    num = 1
    for i in long_term['items']:
        print(str(num) + '. ' + i['name'])
        num += 1

    return


def get_user_top_tracks():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='6e3550b5fd0c40689e3ebb36d7b5ada2',
                                                   client_secret='c8ec0360316c43b4ac8dc4908378c2c5',
                                                   redirect_uri='http://localhost:8080',
                                                   scope='user-top-read'))

    short_term = sp.current_user_top_tracks(limit=10, offset=0, time_range='short_term')
    medium_term = sp.current_user_top_tracks(limit=10, offset=0, time_range='medium_term')
    long_term = sp.current_user_top_tracks(limit=10, offset=0, time_range='long_term')

    print('')
    print('Short term top tracks: ')
    num = 1
    for i in short_term['items']:
        print(str(num) + '. ' + i['name'])
        num += 1

    print('')
    print('Medium term top tracks: ')
    num = 1
    for i in medium_term['items']:
        print(str(num) + '. ' + i['name'])
        num += 1

    print('')
    print('Long term top tracks: ')
    num = 1
    for i in long_term['items']:
        print(str(num) + '. ' + i['name'])
        num += 1

    return


