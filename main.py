import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint

if len(sys.argv) > 1:
    #if artist gives an eror
    search_str = sys.argv[1]
else:
    #the artist or band you want to see its top 10 songs
    search_str = 'Artist or band here'

#The Client_Id given by spotify Api
client_id = "Client_Id here"
#the client_secret # given by spotify api
client_secret = "client_secret here"

#creates credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#prints the result to console
result = sp.search(search_str)
pprint.pprint(result)