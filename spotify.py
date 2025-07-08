import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
))

def get_playlists_by_mood(mood):
    try:
        results = sp.search(q=mood + " playlist", type="playlist", limit=3)
        items = results.get('playlists', {}).get('items', [])
        playlists = []
        for item in items:
            if item:
                playlists.append({
                    'name': item.get('name', 'No Name'),
                    'url': item.get('external_urls', {}).get('spotify', '#')
                })
        return playlists
    except Exception as e:
        print(f"Spotify API error: {e}")
        return []

