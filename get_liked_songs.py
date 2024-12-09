import os
import json
import csv
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

if not client_id or not client_secret:
    raise ValueError("Missing Spotify credentials in environment variables")

# Set up authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://localhost:8888/callback",
    scope="user-library-read"
))

# Get all liked songs
tracks = []
offset = 0
while True:
    results = sp.current_user_saved_tracks(limit=50, offset=offset)
    if not results['items']:
        break

    for item in results['items']:
        track = item['track']
        track_data = {
            'name': track['name'],
            'artist': ', '.join(artist['name'] for artist in track['artists']),
            'album': track['album']['name'],
            'added_at': item['added_at'],
            'duration_ms': track['duration_ms'],
            'popularity': track['popularity'],
            'explicit': track['explicit'],
            'preview_url': track['preview_url'],
            'spotify_url': track['external_urls']['spotify']
        }
        tracks.append(track_data)
        print(f"Found: {track_data['name']} - {track_data['artist']}")

    offset += 50

# Create timestamp for filenames
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

# Save to JSON
json_filename = f'spotify_liked_songs_{timestamp}.json'
with open(json_filename, 'w', encoding='utf-8') as f:
    json.dump(tracks, f, indent=2, ensure_ascii=False)
print(f"\nSaved to JSON: {json_filename}")

# Save to CSV
csv_filename = f'spotify_liked_songs_{timestamp}.csv'
with open(csv_filename, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=tracks[0].keys())
    writer.writeheader()
    writer.writerows(tracks)
print(f"Saved to CSV: {csv_filename}")

print(f"\nTotal tracks saved: {len(tracks)}")