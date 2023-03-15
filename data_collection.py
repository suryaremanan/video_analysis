# Import the necessary modules
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Prompt the user to enter their API key
api_key = input("Enter your YouTube Data API key: ")

# Initialize the YouTube Data API client
youtube = build('youtube', 'v3', developerKey=api_key)

# Search for news-related videos
video_ids = []
next_page_token = None

while len(video_ids) < 1000:
    try:
        search_response = youtube.search().list(
            q='entertainment',
            type='video',
            videoDefinition='high',
            videoDuration='short',
            part='id',
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        # Extract the video IDs from the search results
        video_ids.extend([item['id']['videoId'] for item in search_response['items']])
        next_page_token = search_response.get('nextPageToken')

        if next_page_token is None:
            break

    except HttpError as e:
        print('An error occurred: %s' % e)
        break

# Download the video links and save them to a text file
with open('entertainment_videos2.txt', 'w') as f:
    for video_id in video_ids[:1000]:
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        f.write(video_url + '\n')