from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Iitle: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download("/Users/davidelks/Downloads")