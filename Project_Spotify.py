#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install spotipy flask requests


# In[1]:


pip install spotipy


# In[ ]:


# Refresh Access Token (if expired)
token_info = sp_oauth.get_cached_token()
if not token_info or sp_oauth.is_token_expired(token_info):
    token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])

access_token = token_info['access_token']


# In[4]:


# Create Spotipy Client
sp = spotipy.Spotify(auth=access_token)

# Fetch and Display User's Playlists
playlists = sp.current_user_playlists()
print("Your Playlists:")
for playlist in playlists['items']:
    print(f"- {playlist['name']} ({playlist['tracks']['total']} tracks)")


# In[1]:


# You can get access token even here

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify App Credentials
CLIENT_ID = '9f59eeb81f2f48f2a7ae456aa19e40f1'         # Replace with your Spotify Client ID
CLIENT_SECRET = '25704918fcd74b52be3df24250b26c3d' # Replace with your Spotify Client Secret
REDIRECT_URI = 'http://localhost:8080/callback'  # Replace with your Redirect URI

# Authentication Manager
sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        redirect_uri=REDIRECT_URI,
                        scope="playlist-read-private user-modify-playback-state")

# Get Access Token
try:
    token_info = sp_oauth.get_access_token()
    access_token = token_info
    print("Access Token:", access_token)

except Exception as e:
    print("Error during authentication:", e)
    print("Try re-running the authentication process.")

# Set up Spotipy instance with the token
sp = spotipy.Spotify(auth=access_token)


# In[ ]:


import spotipy

# Extract Access Token
access_token = 'BQAs6g-ScV5wHdjcBnBEXWABOO0csKGYtVviVYsEkoldoRt-GXZTISeMQkL9LLFLsX6-_pjBdFMOiKEXqIDyDoeiLh5LHququwmBXu9AVdjCYqv8jeeVFa0mADb4kn5d1FZuC8KV4-YiSRd8wF9PMgHJ5JP3pe3rw3SBs0BXA-H2RDpkncXheTzcmDeMmoIw9yrfWN0hnIs28mJLXgSJw_-fi3MCKKD0'

# Initialize Spotipy client
sp = spotipy.Spotify(auth=access_token)

print("Spotify client initialized successfully!")


# In[ ]:


# We can get access token from this

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify App Credentials
CLIENT_ID = '9f59eeb81f2f48f2a7ae456aa19e40f1'         # Replace with your Spotify Client ID
CLIENT_SECRET = '25704918fcd74b52be3df24250b26c3d' # Replace with your Spotify Client Secret
REDIRECT_URI = 'http://localhost:8080/callback'  # Redirect URI from Spotify Dashboard

# Authentication Manager
sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        redirect_uri=REDIRECT_URI,
                        scope="playlist-read-private user-modify-playback-state")

# Get or Refresh Access Token
token_info = sp_oauth.get_cached_token()
if token_info is None:
    # If no cached token, perform authorization
    auth_url = sp_oauth.get_authorize_url()
    print("Please go to this URL to authorize:", auth_url)
    response = input("Paste the URL you were redirected to: ")
    code = sp_oauth.parse_response_code(response)
    token_info = sp_oauth.get_access_token(code, as_dict=True)

elif sp_oauth.is_token_expired(token_info):
    # Refresh the token if expired
    token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])

access_token = token_info['access_token']
sp = spotipy.Spotify(auth=access_token)

# Track Playback
track_uri = "spotify:track:6EQVXaIi22Ilmkt1Coi9gZ?si=fd988e8dae384855"  # Replace with your track URI
sp.start_playback(uris=[track_uri])
print("Playing track:", track_uri)

# Playlist Playback
playlist_uri = "spotify:playlist:31ELYZyhSwqzRI89rfdiFq?si=rTGctt2_T9-sQ1iDvQjZ_g"  # Replace with your playlist URI
sp.start_playback(context_uri=playlist_uri)
print("Playing playlist:", playlist_uri)


# In[4]:


import spotipy

# Access token received after authentication
access_token = "BQChvOk5FoMhiM0IWQOkjq02ywHpQXuTWytMmDZm573ENKmUpzpnTBaKiOaIc5875ol8emYBFSttmhdIWWB5pXVDzTOEF8a5kD6VhFqgMnsWBYVrSFGEeegPvMNheVEKVSs61Kp-FCvPZEsZfb_ruquetzQ3TUGKbBh83Wuyhq59fKGjBLiavejdq5-t_jyXLkkfe5unLA1cnWzCNR4NJYeSQhV01_Rm"  # Replace with the token you received

# Initialize the Spotify client
sp = spotipy.Spotify(auth=access_token)

# Example Track URI (replace with a real track URI)
track_uri = "spotify:track:6EQVXaIi22Ilmkt1Coi9gZ?si=fd988e8dae384855"  # Replace with your track URI

# Start playback
sp.start_playback(uris=[track_uri])
print("Playing track:", track_uri)


# In[31]:


# Example Playlist URI (replace with a real playlist URI)
playlist_uri = "spotify:playlist:31ELYZyhSwqzRI89rfdiFq?si=rTGctt2_T9-sQ1iDvQjZ_g"  # Replace with your playlist URI

# Start playback from playlist
sp.start_playback(context_uri=playlist_uri)
print("Playing playlist:", playlist_uri)


# In[5]:


# Replace with the correct playlist URI
playlist_uri = "spotify:playlist:31ELYZyhSwqzRI89rfdiFq"   # Correct format without additional parameters

# Now, call the function with the correct URI
play_mirrored_pairing(playlist_uri)


# In[4]:


import spotipy

# Access token received after authentication
access_token = "BQBNzL50YCCTzXJCKo_lnPZUPP5G6__WmJWY5jcL-NxAcLK7zROXOPefovwsn8Bjt3drQ_EIXr99pTxD-ucR98Fr_iplRJp_HVb0M96bW8r7PyRkdQo_GT9r5q0NlkWT2e8anx-xtnpF9L5wIBBNTlRHgLnMVr0zT0GyLHBVRfFfJnP-fAqZPginvSlgZXYCMpgKdJ_aO-lfZrYgN2JI4FIgTEAzp53O"  # Replace with the token you received

# Initialize the Spotify client
sp = spotipy.Spotify(auth=access_token)

def play_mirrored_pairing(playlist_uri):
    """Play playlist in mirrored pairing order"""
    results = sp.playlist_tracks(playlist_uri)
    tracks = results['items']
    track_uris = []
    
    # Mirrored Pairing Logic: 1 → N → 2 → N-1 → 3 → N-2 → ...
    left = 0
    right = len(tracks) - 1
    while left <= right:
        track_uris.append(tracks[left]['track']['uri'])
        if left != right:
            track_uris.append(tracks[right]['track']['uri'])
        left += 1
        right -= 1
    
    # Start playback with the mirrored order (use uris for custom order)
    sp.start_playback(uris=track_uris)  # This plays the tracks in mirrored order
    print("Playing playlist in Mirrored Pairing order:", track_uris)

def play_odd_even_split(playlist_uri):
    """Play playlist with odd-even split order"""
    results = sp.playlist_tracks(playlist_uri)
    tracks = results['items']
    track_uris = []
    
    # Odd-Even Split Logic: 1, 3, 5, 7, 9, ... (odd indexed) → 2, 4, 6, 8, 10, ... (even indexed)
    odd_tracks = [tracks[i]['track']['uri'] for i in range(0, len(tracks), 2)]  # Odd indices: 0, 2, 4...
    even_tracks = [tracks[i]['track']['uri'] for i in range(1, len(tracks), 2)]  # Even indices: 1, 3, 5...
    
    track_uris = odd_tracks + even_tracks
    
    # Start playback with the odd-even split order (use uris for custom order)
    sp.start_playback(uris=track_uris)  # This plays the tracks in odd-even order
    print("Playing playlist in Odd-Even Split order:", track_uris)


# Example usage:

# Play Mirrored Pairing Playback
playlist_uri = "spotify:playlist:31ELYZyhSwqzRI89rfdiFq"  # Correct URI without query parameter
play_mirrored_pairing(playlist_uri)

# Play Odd-Even Split Playback
#play_odd_even_split(playlist_uri)


# In[2]:


import spotipy

# Access token received after authentication
access_token = "BQAlh3SMNfeUMXg7j8D6V0fboAT1PPPcOlGCKND3B4bxrvAvEOmoIVmkRl6YAkuFjB1EDO1h_jKbfV3KPxtevLAySdj-upacRiYsTWJtBZIHNSPkg9BanB0daC7mDSMthRYjldJ06qjbxpIj2Dr28mJh4BiqY8okVQzWdwm5wxz0bTIKZ2kcxVHSf8MoesTcpFPspvpN4-9x-F5x_Rokl8-_jIl50K3_"  # Replace with the token you received

# Initialize the Spotify client
sp = spotipy.Spotify(auth=access_token)

# Example Track URI (replace with a real track URI)
track_uri = "spotify:track:6EQVXaIi22Ilmkt1Coi9gZ?si=fd988e8dae384855"  # Replace with your track URI

# Start playback
sp.start_playback(uris=[track_uri])
print("Playing track:", track_uri)


# In[ ]:




