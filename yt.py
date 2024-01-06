from pytube import YouTube, Playlist
import os, shutil
import google.auth
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.auth.transport.requests import AuthorizedSession
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Load credentials from the JSON file
#credentials = Credentials.from_authorized_user_file(
 #   'C:\Users\User\Desktop\py\client_secret_64333543398-i3tgpet9rma9apum7r3nh68ivsr7ul9r.apps.googleusercontent.com.json',
#    scopes=['https://www.googleapis.com/auth/youtube.upload']
#)
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Set the path to your client secrets file
client_secrets_file = 'client_secret_64333543398-i3tgpet9rma9apum7r3nh68ivsr7ul9r.apps.googleusercontent.com.json'

# Define the scopes
scopes = ['https://www.googleapis.com/auth/youtube.upload']

# Set up the OAuth2.0 flow
#flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes=scopes)
flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes=scopes, redirect_uri='http://localhost:8080/')


# Run the flow and authorize the user if not already authorized
# Run the flow and authorize the user if not already authorized
credentials = flow.run_local_server()



# Create a YouTube API client
youtube = build('youtube', 'v3', credentials=credentials)


if os.path.isdir("shorts"):
  shutil.rmtree("shorts")

cwd = os.getcwd()
print(cwd)

dir = "shorts"
os.mkdir(dir)

os.chdir('shorts')
cwd = os.getcwd()
print(cwd)

playlistflag=False

if playlistflag:
  ytp = Playlist(
    'https://www.youtube.com/playlist?list=PLPPomK5QKeyWV7PYC9s-PxrDhVIDpt4Oe')


  for video in ytp.videos:
    print("started " + video.title)
    video.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download()
    print(video.title + " downloaded")
    
else:
  yt = YouTube('https://www.youtube.com/shorts/9K3k0Yinlbo')
  print("started " + yt.title)
  yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download()
  print(yt.title + " downloaded")

print("Download(s) complete")

        
def upload_video(file_path, title, description, tags=None, category_id='22', is_made_for_kids=False):
    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': category_id
        },
        'status': {
            'privacyStatus': 'private'  # Set this to 'public' or 'private' as needed
        }
    }

    if is_made_for_kids:
        request_body['contentDetails'] = {
            'madeForKids': is_made_for_kids
        }

    # Upload the video
    videos_insert_request = youtube.videos().insert(
        part='snippet,status,contentDetails',
        body=request_body,
        media_body=file_path
    )

    response = videos_insert_request.execute()
    video_id = response['id']

    print(f'Video uploaded successfully! Video ID: {video_id}')


# Example usage

files = [f for f in os.listdir() if os.path.isfile(f)]

for file in files:
  if file.endswith('.mp4'):

    video_file_path = str(file)
    video_title = "Dont disturb me #shorts"
    video_description = 'fight movie shorts'
    video_tags = ['shorts', 'movie', 'series']
    is_made_for_kids=False
    print(video_file_path)
    print(video_title)
    upload_video(video_file_path, video_title, video_description, video_tags, is_made_for_kids=is_made_for_kids)  