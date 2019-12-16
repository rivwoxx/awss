import sys
import spotipy
import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from json.decoder import JSONDecodeError
import pprint
''' shows the albums and tracks for a given artist.
'''
cid = '405ce5ec350c41f1918edcfb91662618'
secret = 'bf83bc145556490b87c78dde9905e17a'

client_credentiasl_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentiasl_manager)

def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None

def show_artist_albums(artist):
    albums = []
    results = sp.artist_albums(artist['id'], album_type='album')
    albums.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
    seen = set() # to avoid dups
    albums.sort(key=lambda album:album['name'].lower())
    for album in albums:
        name = album['name']
        if name not in seen:
            print((' ' + name))
            seen.add(name)

if __name__ == '__main__':
    sp = spotipy.Spotify()

    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:])
    else:
        artist = 'LP'
        if artist:
            show_artist_albums(artist)
        else:
            print("Can't find that artist")