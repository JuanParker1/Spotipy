import spotipy
from spotipy import SpotifyOAuth


class Basic:
    def __init__(self, mode):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='6e3550b5fd0c40689e3ebb36d7b5ada2', client_secret='c8ec0360316c43b4ac8dc4908378c2c5', redirect_uri='http://example.com', scope='user-read-currently-playing'))

        if mode == 2:
            self.current_track = self.get_currently_playing_track()

    def get_currently_playing_track(self):
        current_track = self.sp.current_user_playing_track()

        title = current_track['item']['name']
        artists = ' & '.join(artist['name'] for artist in current_track['item']['artists'])
        link = current_track['item']['external_urls']['spotify']

        current_track_info = {
            '1. title': title,
            '2. artists': artists,
            '3. link': link
        }

        return current_track_info


