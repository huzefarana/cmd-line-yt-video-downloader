import yt_dlp

url = input("Enter the URL of the video: ")

# Set the output folder for downloads
output_folder = "downloads/"

ydl_opts = {
    'outtmpl': output_folder + '%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
    print("Video downloaded successfully!")
