import yt_dlp

link = input("Paste Link : ")

ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    print("Downloading...")
    ydl.download([link])
    print("Done!!!")
