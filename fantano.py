import spotipy
from spotipy import SpotifyOAuth
from pprint import pprint


class Fantano:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='6e3550b5fd0c40689e3ebb36d7b5ada2', client_secret='c8ec0360316c43b4ac8dc4908378c2c5', redirect_uri='http://example.com', scope='user-library-read'))
        self.saved_albums = self.get_saved_albums()

    def get_saved_albums(self):

        saved_albums = self.sp.current_user_saved_albums(limit=50, offset=0)['items']
        total = 451

        offset = int(50)
        while offset < (total + 50):
            saved_albums.extend(self.sp.current_user_saved_albums(limit=50, offset=offset)['items'])
            offset = offset + 50

        albums = {
            'title': [],
            'artists': [],
            'score': [],
            'id': []
        }

        for i in saved_albums:
            release_year = int((i['album']['release_date'])[0:4])

            if (release_year >= 2010) and (i['album']['album_type'] == 'album'):
                albums['title'].append(i['album']['name'])
                albums['artists'].append(' & '.join(artist['name'] for artist in i['album']['artists']))
                albums['score'].append(-1)
                albums['id'].append(i['album']['external_urls']['spotify'])

                # contains every album that has the potential to have a Fantano score
        return albums

    def get_fantano_scores(self):
        print("WIP")


