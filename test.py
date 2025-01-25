import os
from yt_dlp import YoutubeDL

def download_youtube_playlist(playlist_url, save_path="C:\\Users\\yosse\\Desktop\\New_folder"):
    options = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'noplaylist': False,
    }
    with YoutubeDL(options) as ydl:
        ydl.download([playlist_url])

# Example usage
if __name__ == "__main__":
    playlist_url = r"https://youtube.com/playlist?list=PLqRE85iBYcVC4v7qj7jLVUdfgFG4_PB5k&si=M4wp-8rGgfo51W2L"
    save_path = "C:\\Users\\yosse\\Desktop\\New_folder"
    download_youtube_playlist(playlist_url, save_path)
