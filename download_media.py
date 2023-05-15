from instagrapi import Client 
from pytube import YouTube

media_url = str(input("Paste URL : ")

#Instagram
def instagram_download():
    cl = Client()
    #cl.login(username='', password='')
    pk = cl.media_pk_from_url(media_url)
    download_path = "path_to_images_folder"

    match cl.media_info(pk).media_type:
        case 1: 
            cl.photo_download(pk, folder=download_path)
        case 8:
            cl.album_download(pk, folder=download_path)
        case _:
            cl.video_download(pk, folder=download_path)
                
#Youtube
def youtube_video_download():
    yt = YouTube(media_url)
    yt.streams.get_highest_resolution().download("/home/spark/Videos/YouTube")

def youtube_audio_download():
    yt = YouTube(media_url)
    yt.streams.get_by_itag(140).download("/home/spark/Music")

if "youtu.be" in media_url:
    if input("audio or video\n") == "audio":
        youtube_audio_download()
    else:
        youtube_video_download()
elif "instagram.com" in media_url:
    instagram_download()
