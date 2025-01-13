import yt_dlp

link = input("Paste Link : ")

ydl_opts = {
    'format': 'best',  # Download the best quality available
    'outtmpl': '%(title)s.%(ext)s'  # Output file template
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    print("Downloading...")
    ydl.download([link])
    print("Done!!!")
