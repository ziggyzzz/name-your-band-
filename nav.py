import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

os.environ["SPOTIPY_CLIENT_ID"] = "219a05249bd64963b75f8c7d32e9532c"
os.environ["SPOTIPY_CLIENT_SECRET"] = "bda2343aed5c4be5a06e3b5bd3582a58"

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)