import time
from base64 import b64encode
from pprint import pprint
import spotipy
from spotipy.oauth2 import  SpotifyOAuth
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

MY_CLIENT_ID = os.environ['MY_CLIENT_ID']
MY_CLIENT_SECRET = os.environ['MY_CLIENT_SECRET']

date = '2000-08-12'
url = f'https://www.billboard.com/charts/hot-100/{date}/'
response=requests.get(url=url)

soup=BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
songs_title = [song.get_text().strip() for song in song_names_spans]
print(songs_title)


URL_ENDPOINT = 'https://accounts.spotify.com/api/token'
auth_str = f'{MY_CLIENT_ID}:{MY_CLIENT_SECRET}'
b64_auth_str = b64encode(auth_str.encode()).decode()


body = {
    'grant_type': 'client_credentials'
}


headers = {
    'Authorization': f'Basic {b64_auth_str}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.post(url=URL_ENDPOINT, data=body, headers=headers)
print(response.json())


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=MY_CLIENT_ID,
        client_secret=MY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=os.environ['SPOTIFY_USERNAME'],
    )
)
user_id = sp.current_user()["id"]


#date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD')
year = date.split('-')[0]
song_uris = []

for song in songs_title:
    result = sp.search(q=f'track:{song} year:{year}')
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

