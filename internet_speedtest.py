import speedtest

def bytestomb(bytes):
    KB = 1024
    MB = KB * 1024
    return int(bytes / MB)

st = speedtest.Speedtest()

input("Press Enter to Start Speed Test")

download_speed = bytestomb(st.download())
upload_speed = bytestomb(st.upload())
ping = st.results.ping

print(f"Download speed: {download_speed} MB/s")
print(f"Upload speed: {upload_speed} MB/s")
print(f"Ping: {ping} ms")