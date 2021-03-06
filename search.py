import os
from operator import itemgetter

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_artists(artist_name):
    #so we can call any artist name
    os.environ["SPOTIPY_CLIENT_ID"] = "219a05249bd64963b75f8c7d32e9532c"
    os.environ["SPOTIPY_CLIENT_SECRET"] = "bda2343aed5c4be5a06e3b5bd3582a58"

    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    response = sp.search(q=artist_name, limit=10, offset=0, type='artist', market='US')
    artists = response['artists']['items']

    artists = sorted(artists, key=itemgetter('popularity'), reverse=True)
    #sort dictionary artists using itemgetter which uses popularity as sorting key

    formatted_artists = []

    for artist in artists:
        formatted_artist = {
            'name': artist['name'],
            'popularity': artist['popularity'],
        }

        formatted_artists.append(formatted_artist)
#each artist in list is passed to the webpage formatted as a dictionary
    return formatted_artists


print(get_artists('Muse'))
