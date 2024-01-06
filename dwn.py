from pytube import YouTube, Playlist
import os, shutil

con = 1
dir = "shorts"
if os.path.isdir("shorts"):
  for i in range(100):
    if os.path.isdir("shorts" + str(i)):
      continue
    dir = "shorts" + str(i)
    os.mkdir(dir)
    break
else:
  dir = "shorts"
  os.mkdir(dir)

cwd = os.getcwd()
print(cwd)
print(dir)
os.chdir(str(dir))
cwd = os.getcwd()
print(cwd)
playlistflag = input("enter 1 if playlist or 0 for video: ")

while (True):

  if playlistflag == 1:
    link = input("enter playlist link: ")
    ytp = Playlist(str(link))

    for video in ytp.videos:
      print("started " + video.title)
      try:
       video.streams.filter(progressive=True, file_extension='mp4').order_by(
           'resolution').desc().first().download()
       print(video.title + " downloaded")
      except Exception as e:
       print("age restricted")
  else:
    link = input("enter video link: ")
    yt = YouTube(link)
    print("started " + yt.title)
    try:
     yt.streams.filter(
         progressive=True,
         file_extension='mp4').order_by('resolution').desc().first().download()
     print(yt.title + " downloaded")
    except Exception as e:
     print("age restricted")
  print("Download(s) complete")

  print("####################")
