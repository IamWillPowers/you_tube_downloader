"""
I watched the below video on how to make a python youtube downloader with pytube
The video did not show how to download a high quality video so changed the code to do that.
The video also did not show how to download all videos in a playlist, which was much
more useful for what I wanted to do, so I added a new button and line option to do that,
which took quite a while because the documentation for playlist implementation from
pytube did not work, I had to modify the youtube tutorial code to do that, but now it works!
I also changed the code to be PEP8 / Google layout compliant.
https://www.youtube.com/watch?v=fbv8QoCpMz8
https://pypi.org/project/pytube3/#quick-start

Future upgrades:
1) make a progress bar so its not just a spinning wheel (especially useful for big playlists)
2) why does the first instance of notif and notifp have an error?
3) Can I change the pytube code to download my Udemy class videos?
"""
from tkinter import *
from tkinter import Label
import pytube
from pytube import Playlist
# Functions


def download_video():
    video_url = v_url.get()
    try:
        pytube.YouTube(video_url).streams.get_highest_resolution().download("G:/Downloads")
        notif.config(fg="green", text="Success!")
    except Exception as e:
        print(e)
        notif.config(fg="red", text="Error")


def download_playlist():
    try:
        playlist_url = p_url.get()
        playlist = Playlist(playlist_url)
        for video in playlist:
            # video.streams.get_highest_resolution().download("G:/Downloads")
            # ABOVE IS WHAT THE DOCS SAID TO DO BUT IT DIDNT WORK, below is correct
            pytube.YouTube(video).streams.get_highest_resolution().download("G:/Downloads")
        notifp.config(fg="green", text="Success!")
    except Exception as e:
        print(e)
        notifp.config(fg="red", text="Playlist Error")


# main screen
master = Tk()
master.title("Youtube Video Downloader")

# Labels
Label(master, text="Youtube Video Converter", fg="red",
      font=("Calibri", 15)).grid(sticky=N, padx=100, row=0)
Label(master, text="Enter Video Link: ",
      font=("Calibri", 12)).grid(sticky=N, pady=10, row=1)
Label(master, text="Enter Playlist Link: ",
      font=("Calibri", 12)).grid(sticky=N, pady=10, row=5)
notif = Label(master, font=("Calibri", 12))
notif.grid(sticky=N, pady=1, row=4)
notifp = Label(master, font=("Calibri", 12))
notifp.grid(sticky=N, pady=1, row=8)

# Variables
v_url = StringVar()
p_url = StringVar()

# Entry
Entry(master, width=60, textvariable=v_url).grid(sticky=N, row=2)
Entry(master, width=60, textvariable=p_url).grid(sticky=N, row=6)

# Button
Button(master, width=20, text="Download Video", font=("Calibri", 12),
       command=download_video).grid(sticky=N, row=3, pady=10)
Button(master, width=20, text="Download Playlist", font=("Calibri", 12),
       command=download_playlist).grid(sticky=N, row=7, pady=10)

master.mainloop()

