import os
import time
from base64 import b64encode
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
MY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
REDIRECT_URI = os.environ.get('SPOTIPY_REDIRECT_URI', 'http://example.com')
SPOTIFY_USERNAME = os.environ['SPOTIFY_USERNAME']

def fetch_billboard_songs(date):
    url = f'https://www.billboard.com/charts/hot-100/{date}/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    song_names_spans = soup.select("li ul li h3")
    songs_title = [song.get_text().strip() for song in song_names_spans]
    return songs_title

def authenticate_spotify(client_id, client_secret, redirect_uri, username):
    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri=redirect_uri,
            client_id=client_id,
            client_secret=client_secret,
            show_dialog=True,
            cache_path="token.txt",
            username=username,
        )
    )

def create_playlist(sp, user_id, date):
    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
    return playlist

def search_song_uris(sp, songs_title, year):
    song_uris = []
    for song in songs_title:
        result = sp.search(q=f'track:{song} year:{year}')
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")
    return song_uris

def add_songs_to_playlist(sp, playlist_id, song_uris):
    sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)

def main():
    date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD')
    songs_title = fetch_billboard_songs(date)
    print(songs_title)
    
    sp = authenticate_spotify(MY_CLIENT_ID, MY_CLIENT_SECRET, REDIRECT_URI, SPOTIFY_USERNAME)
    user_id = sp.current_user()["id"]
    
    year = date.split('-')[0]
    song_uris = search_song_uris(sp, songs_title, year)
    print(song_uris)
    
    playlist = create_playlist(sp, user_id, date)
    print(playlist)
    
    add_songs_to_playlist(sp, playlist["id"], song_uris)

if __name__ == "__main__":
    main()
