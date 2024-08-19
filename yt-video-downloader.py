from pytube import YouTube

def data_yd(url):
    
    yt = YouTube(url)

    print(f"Title: {yt.title}")
    print(f"Views: {yt.views}")
    print(f"Publish Date: {yt.publish_date}")
    print(f"Author: {yt.author}")
    print(f"Channel URL: {yt.channel_url}")
    print(f"Length : {yt.length} seconds")
    print(f"Rating: {yt.rating}")
    print(f"Description: {yt.description}")
    #  print(f"Description: {yt.captions.get_by_language_code('en')}")
    print(f"Thumbnail URL: {yt.thumbnail_url}")

    # yd = yt.streams.get_highest_resolution()
    # yd.download()

url = 'https://youtu.be/Wukb2io92DY'
# data_yd(url)


# Interacting with a playlist
from pytube import Playlist

def playlist_data(url):
    p = Playlist(url)
    print(f'Playlist Title: {p.title}')
    i=1
    for url in p.video_urls:
        print(i, url)
        i= i+1
    
    # for video in p.videos:
    #     video.streams.first().download()

link = 'https://youtube.com/playlist?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&si=zOsGDq23BZMRlh5Q'
playlist_data(link)
        
# Interacting with a Channel
from pytube import Channel

def Channel_data(url):
    c = Channel(url)
    print(f'Channel Title: {c.channel_name}')
    
    for url in c.video_urls[:3]:
        print(url)
    
    # for video in c.videos:
        # video.streams.first().download()

link = 'https://www.youtube.com/@geekyshows'
# Channel_data(link)
        

# Interacting with Search
from pytube import Search

def Channel_data(word):
    s = Search(word)
    print(f'Search Length: {len(s.results)}')
    s.get_next_results()
    print(f'Next Search Length: {len(s.results)}')

word = 'Python'
# Channel_data(word)