from tkinter import Tk, Label, Entry, Button, IntVar
from pytube import YouTube, Playlist
import os

def create_shorts_directory():
    for i in range(100):
        try:
            dir_path = os.path.join(os.getcwd(), "shorts" + str(i))
            os.mkdir(dir_path)
            os.chdir(dir_path)
            return dir_path
        except PermissionError:
            print(f"PermissionError: Could not create 'shorts{i}' directory. Trying the next one.")

def download():
    link = link_entry.get()
    is_playlist = playlist_var.get()

    directory = create_shorts_directory()

    if is_playlist:
        ytp = Playlist(link)
        for video in ytp.videos:
            download_video(video)
    else:
        yt = YouTube(link)
        download_video(yt)

def download_video(video):
    print("Started " + video.title)
    video.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download()
    print(video.title + " downloaded")

root = Tk()
root.title("YouTube Downloader")

link_label = Label(root, text="Enter video/playlist link:")
link_label.pack()

link_entry = Entry(root, width=40)
link_entry.pack()

playlist_var = IntVar()
playlist_checkbox = Button(root, text="Download Playlist", command=download)
playlist_checkbox.pack()

download_button = Button(root, text="Download", command=download)
download_button.pack()

root.mainloop()
