from pytube import YouTube

link = input("Link: ")
yt = YouTube(link)

video = yt.streams.get_highest_resolution()
video.download()
print("here is an example https://www.youtube.com/watch?v=dQw4w9WgXcQ")
