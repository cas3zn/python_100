from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = ""
SPOTIPY_CLIENT_SECRET = ""
REDIRECT_URI = "http://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

str_date = input("Which year do you want to travel to? Enter the date in the format YYYY-MM-DD: ")
BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{str_date}"
response = requests.get(BILLBOARD_URL)

soup = BeautifulSoup(response.text, "html.parser")
allSongs = soup.find_all('h3', id="title-of-a-story")
songNames = [x.get_text().replace("\n", "").replace("\t", "") for x in allSongs]
songNames = list(dict.fromkeys(songNames))
songNames.remove('Songwriter(s):')
songNames.remove('Producer(s):')
songNames.remove('Imprint/Promotion Label:')

list_uri = []
for song in songNames[3:103]:
    result = sp.search(type="track", q=f"track:{song} year: {str_date.split('-')[0]}")
    try:
        uri = result['tracks']['items'][0]['uri']
        list_uri.append(uri)
    except IndexError:
        print(f"Not found. {song} skipped.")

new_playlist = sp.user_playlist_create(
    user=user_id,
    public=False,
    name=f"{str_date} Billboard 100"
)
print(new_playlist)
add_songs_to_playlist = sp.playlist_add_items(playlist_id=new_playlist['id'], items=list_uri)
