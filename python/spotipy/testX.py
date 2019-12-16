import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = '405ce5ec350c41f1918edcfb91662618'
secret = 'bf83bc145556490b87c78dde9905e17a'

client_credentiasl_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentiasl_manager)

# if len(sys.argv) > 1:
#     name = ' '.join(sys.argv[1:])
# else:
#     name = 'LP'

#     results = sp.search(q='artist:' + name, type='artist')
#     items = results['artists']['items']
#     if len(items) > 0:
#         artist = items[0]
#         print(artist['name'], artist['images'][0]['url'])

# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

# lp = 'spotify:artist:0J7U24vlOOIeMpuaO6Q85A'
fm = 'spotify:artist:08GQAI4eElDnROBrJRGE0X'
results = sp.artist_albums(fm, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])