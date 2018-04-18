import os
from operator import itemgetter

#from termcolor import colored

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from flask import Flask, render_template,request,url_for
app = Flask(__name__)

#import pandas


#import tabulate

#Linking to 2 new html files using jinja2 syntax.

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/keyword', methods=['POST'])
def list_artists():
    artist_name = request.form.get('artist_name')
    dirty_artists = get_artists(artist_name)
    cleaned_artists = clean_data(dirty_artists)
    names = []
    popularity = []
    genre = []
    for x in cleaned_artists:
        name_to_append = x.get('name')
        popularity_to_append = x.get('popularity')
        genre_to_append = x.get('genre')
        names.append(name_to_append)
        popularity.append(popularity_to_append)
        genre.append(genre_to_append)

    return line_chart(popularity,names,'popularity of aritsts')



   # return render_template('datapage.html', cleaned_artists=cleaned_artists)

def line_chart(value, label,legend):
    return render_template('line_chart.html', values=value, labels=label, legend=legend)




def get_artists(artist_name):
    #so we can call any artist name
    os.environ["SPOTIPY_CLIENT_ID"] = "219a05249bd64963b75f8c7d32e9532c"
    os.environ["SPOTIPY_CLIENT_SECRET"] = "bda2343aed5c4be5a06e3b5bd3582a58"

    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    response = sp.search(q=artist_name, limit=50, offset=0, type='artist', market='US')
    artists = response['artists']['items']

    artists = sorted(artists, key=itemgetter('popularity','genres'), reverse=True)
    #sort dictionary artists using itemgetter which uses popularity as sorting key

    formatted_artists = []

    for artist in artists:
        formatted_artist = {
            'name': artist['name'],
            'genres': artist['genres'],
            'popularity':artist['popularity']
        }

        formatted_artists.append(formatted_artist)
    #each artist in list is passed to the webpage formatted as a dictionary
    return formatted_artists

def clean_data(artist_list):
    data_with_genre = []
    for item in artist_list:
        value = item.get('genres')
        if value:
            data_with_genre.append(item)
    return data_with_genre

app.run(debug=True)