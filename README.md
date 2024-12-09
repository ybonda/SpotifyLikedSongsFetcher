# Spotify Liked Songs Exporter

A simple Python script that exports your Spotify liked songs to CSV and JSON files. The script fetches all your liked songs along with detailed information about each track.

## Features

- Exports all your Spotify liked songs
- Saves data in both CSV and JSON formats
- Includes detailed track information:
  - Song name
  - Artist(s)
  - Album name
  - Date added to liked songs
  - Duration
  - Popularity score
  - Explicit flag
  - Preview URL
  - Spotify URL
- Uses environment variables for secure credential management

## Prerequisites

- Python 3.6 or higher
- A Spotify account
- Spotify Developer credentials

## Installation

1. Clone this repository or download the script
2. Install required packages:
```bash
pip install spotipy python-dotenv
```

## Setting up Spotify credentials

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Log in with your Spotify account
3. Click "Create app"
4. Fill in the app creation form:
   - App name: Choose any name (e.g., "Liked Songs Exporter")
   - App description: Brief description of your app
   - Redirect URI: Enter `http://localhost:8888/callback`
   - Select any appropriate category
5. Click "Save"
6. On the app's dashboard, you'll find your Client ID
7. Click "View client secret" to reveal your Client Secret
8. Create a `.env` file in the same directory as the script with the following content:
```
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
```

Replace `your_client_id_here` and `your_client_secret_here` with your actual Spotify credentials.

## Usage

Run the script:
```bash
python spotify_liked_songs.py
```

On first run, it will:
1. Open your web browser
2. Ask you to log in to Spotify
3. Request permission to access your liked songs
4. Redirect you back to the application

The script will then:
- Fetch all your liked songs
- Show progress while fetching
- Create two files with timestamps in their names:
  - `spotify_liked_songs_YYYYMMDD_HHMMSS.json`
  - `spotify_liked_songs_YYYYMMDD_HHMMSS.csv`

## Output Files

### CSV File
- Can be opened in Excel, Google Sheets, or any spreadsheet software
- Useful for data analysis and manipulation

### JSON File
- Contains the same data in JSON format
- Preserves all data types
- Useful for programmatic processing

## Security Notes

- Never commit your `.env` file to version control
- Add `.env` to your `.gitignore` file
- Keep your Spotify credentials secure and private

## Troubleshooting

1. **"Missing Spotify credentials in environment variables"**
   - Check if your `.env` file exists and contains the correct credentials
   - Verify the variable names match exactly: `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET`

2. **Authentication Failed**
   - Verify your Spotify credentials are correct
   - Check if the redirect URI in your code matches the one in your Spotify app settings

3. **Rate Limiting**
   - The script handles Spotify's rate limits automatically
   - If you experience issues, try running the script again

## License

This project is open source and available under the MIT License.