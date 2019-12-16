import os
import sys
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from json.decoder import JSONDecodeError
import pprint

def albums(id):
    al = sp.artist_albums(id,album_type='album',country='MX')
    als = al['items']
    # pprint.pprint(al)
    print()
    print('Albums:')
    print()
    for x in als:
        aln = x['name']
        rdate = x['release_date']
        tracks = x['total_tracks']
        print('Name: ' + aln)
        print('Release Date: ' + rdate)
        print('Tracks: ' + str(tracks))
        print()

cid = '405ce5ec350c41f1918edcfb91662618'
secret = 'bf83bc145556490b87c78dde9905e17a'

client_credentiasl_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentiasl_manager)

# if len(sys.argv) > 1:
#     search_str = sys.argv[1]
# else:
#     search_str = 'Radiohead'

# results = sp.search(q='artist:' + search_str, type='artist')
# items = results['artists']['items']
# if len(items) > 0:
#     artist = items[0]
#     print(artist['name'], artist['images'][0]['url'])

ar = input('Give me the name of an artist: ')
print()
res = sp.search(ar, type= 'artist')
artist = res['artists']['items']
if len(artist) > 0:
    artist = artist[0]
    id = artist['id']
    name = artist['name']
    # print(artist['name'], artist['id'])
print(name + " ID: " + id )

albums(id)
# print(id)
# print(name)
# pprint.pprint(res)

# al = sp.artist_albums(id,album_type='album',country='MX')
# als = al['items']
# # pprint.pprint(al)
# print()
# print('Albums:')
# print()
# for x in als:
#     aln = x['name']
#     rdate = x['release_date']
#     tracks = x['total_tracks']
#     print('Name: ' + aln)
#     print('Release Date: ' + rdate)
#     print('Tracks: ' + str(tracks))
#     print()

# for als in len(als):
#     als = als[0]
#     alsname = als['name']
#     print(alsname)
# if len(als) > 0:
#     als = als[0]
#     alname = als['name']
#     # # print (alname)
# # pprint.pprint(al)
# print(alname)

