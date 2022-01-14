import re
from pytube import Playlist

DOWNLOAD_DIR = 'C:\\Users\\tomia\\Documents\\PythonYoutubeDownloader\\Downloads'
global pl 
pl = "N/A"
global destination
destination  = 1

print("Initializing...")

def showMenu():
    global pl
    global destination
    print("+-----------------------------------+")
    print("+ Playlist URL:" + pl)
    print("+-----------------------------------+")
    print("OPTIONS: setPlaylist, execute, exit")

    optn = input()
    if(optn == "setPlaylist"):
        setPlaylist()
    elif(optn == "execute"):
        execute()
    elif(optn == "exit"):
        exit()
    else:
        print("Command unclear, please read options (cap sensitive)")
        showMenu()


def setPlaylist():
    global pl
    print("Please enter the playlist url:")
    pl = input()
    showMenu()

def setTarget():
    global destination
    print("Enter your desired download folder (1-3)")
    destination = input()
    showMenu()


def execute():
    global pl
    global destination
    playlist = Playlist(pl)   

    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")    
    print(len(playlist.video_urls))    
    for url in playlist.video_urls:
        print(url)    
    for video in playlist.videos:
        print('downloading : {} with url : {}'.format(video.title, video.watch_url))
        video.streams.\
            filter(type='video', progressive=True, file_extension='mp4').\
            order_by('resolution').\
            desc().\
            first().\
            download(DOWNLOAD_DIR)

showMenu()





