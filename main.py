import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

from pytube import YouTube
link = input("Enter the link:")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
print("Done")
