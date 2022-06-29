from pytube import YouTube
lnk = input("Enter the link URL ")
you = YouTube(lnk)
videos = you.streams.all()
video = list(enumerate(videos))
for i in video:
    print(i)
print("Enter the desired option to download the format")
option = int(input("Enter the Option"))
Dvideo=videos[option]
Dvideo.download()
print("Your Video Downloaded Successfully")