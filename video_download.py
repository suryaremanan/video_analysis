from pytube import YouTube

# Read the video links from file
with open('news_videos2.txt', 'r') as f:
    video_links = f.read().splitlines()

# Download the videos
for link in video_links:
    try:
        yt = YouTube(link)
        video = yt.streams.get_highest_resolution()
        video.download(output_path='news2')
    except Exception as e:
        print(f'An error occurred while downloading {link}: {e}')