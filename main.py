import customtkinter
from PIL import Image
from pytubefix import YouTube
from tkinter import filedialog
from tkinter import messagebox
import os
import time
from moviepy.editor import AudioFileClip
from urllib.error import HTTPError
import yt_dlp
from yt_dlp import YoutubeDL

root = customtkinter.CTk()
root.iconbitmap(r"D:\My Projects\Pycharm\Youtube-Downloader-By-Yossef-Ibrahim\Data\icon_YT.ico")
root.title(" YT Downloader ")
root.geometry('600x600')

download_path = ""  # Initialize download_path globally

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    progress_var.set(percentage)
    progress_label.configure(text=f"Downloading: {int(percentage)}%")

result_label = customtkinter.CTkLabel(master=root, text="")
result_label.place(relx=0.1, rely=0.65)

def download_video_as_mp3():
    global download_path
    result_label.configure(text=f"Save location selected: {download_path}")
    url = URL_Youtube.get()
    if url and download_path:
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'{download_path}/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            for i in range(101):
                time.sleep(0.05)
                progress_var.set(i)
                progress_label.configure(text=f"Converting: {i}%")
                progress_label.update_idletasks()

            result_label.configure(text="Downloaded and converted to MP3 successfully!")
            messagebox.showinfo("", "Converted Completed!")
        except Exception as e:
            result_label.configure(text=f"An error occurred: {e}")
            print(f"An error occurred: {e}")
    else:
        result_label.configure(text="Please provide both a URL and a download location.")

def convert_to_mp3(audio_file):
    global download_path

    try:
        print(f"Audio file: {audio_file}")
        print(f"Download path: {download_path}")

        mp3_file = os.path.join(download_path, os.path.splitext(os.path.basename(audio_file))[0] + '.mp3')
        print(f"MP3 file will be saved to: {mp3_file}")

        audio_clip = AudioFileClip(audio_file)
        if audio_clip is None:
            raise ValueError("Failed to create AudioFileClip. The file might be corrupted or unsupported.")

        for i in range(101):
            time.sleep(0.05)
            progress_var.set(i)
            progress_label.configure(text=f"Converting: {i}%")
            progress_label.update_idletasks()

        audio_clip.write_audiofile(mp3_file)
        audio_clip.close()
        os.remove(audio_file)

        # Use root.after to update the result_label safely in the main thread
        root.after(0, result_label.configure, {"text": f"Downloaded and converted to MP3: {mp3_file}"})
        root.after(0, messagebox.showinfo, "", "Completed ")
    except Exception as e:
        root.after(0, result_label.configure, {"text": f"An error occurred: {e}"})

        print(f"Error: {e}")


def Download_Youtube_video():

    global download_path
    if not URL_Youtube.get() or not download_path:
        result_label.configure(text="Please provide both a URL and a download location.")
        return
    if not URL_Youtube.get().startswith("https://www.youtube.com/watch"):
        result_label.configure(text="Invalid YouTube URL.")
        return
    if not os.path.isdir(download_path):
        result_label.configure(text="Invalid download path.")
        return

    try:
        yt = YouTube(URL_Youtube.get(), on_progress_callback=on_progress, use_po_token=True)
        # Debugging information
        print(f"Video Title: {yt.title}")
        print(f"Video Author: {yt.author}")
        stream = yt.streams.get_highest_resolution()
        print(f"Stream details: {stream}")
        stream.download(output_path=download_path)
        result_label.configure(text=f"Video downloaded to: {download_path}")
        messagebox.showinfo("", "Download Completed!")

    except HTTPError as e:
        result_label.configure(text=f"HTTP error occurred: {e}")
        print(f"HTTP Error: {e}")

    except Exception as e:
        result_label.configure(text=f"An error occurred: {e}")
        print(f"Error: {e}")

def download_youtube_playlist():
    try:
        url = URL_Youtube.get()  # URL input from the user
        save_path = download_path  # Path where videos will be saved

        # Define options for YoutubeDL
        options = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(save_path, '%(playlist_index)s - %(title)s.%(ext)s'),
            'noplaylist': True,
        }

        # Initialize total count of videos
        total_videos = 0

        # Download playlist videos
        with YoutubeDL(options) as ydl:
            playlist_info = ydl.extract_info(url, download=False)
            if 'entries' in playlist_info:  # If it's a playlist
                total_videos = len(playlist_info['entries'])
                for video in playlist_info['entries']:
                    ydl.download([video['webpage_url']])
            else:  # Single video
                total_videos = 1
                ydl.download([url])

        # Show success message after all videos are downloaded
        messagebox.showinfo("", f"Download {total_videos} videos successfully!")

    except Exception as e:
        messagebox.showerror("", f"Download failed: {str(e)}")
img = customtkinter.CTkImage(
    dark_image=Image.open(r"D:\My Projects\Pycharm\Youtube-Downloader-By-Yossef-Ibrahim\Data\YT Downloader By Yossef Ibrahim.png"),
    size=(400, 200))
img_folder = customtkinter.CTkImage(
    dark_image=Image.open(r"D:\My Projects\Pycharm\Youtube-Downloader-By-Yossef-Ibrahim\Data\folder.png"),
    size=(25, 25))

def Path_download():
    global download_path
    download_path = filedialog.askdirectory()
    if download_path:
        result_label.configure(text=f"Save location selected: {download_path}")
    else:
        result_label.configure(text="Save location selection cancelled.")

progress_var = customtkinter.IntVar()
progress_bar = customtkinter.CTkProgressBar(master=root, variable=progress_var, width=400)
progress_bar.place(relx=0.1, rely=0.75)
progress_label = customtkinter.CTkLabel(master=root, text="Downloading: 0%")
progress_label.place(relx=0.1, rely=0.80)

customtkinter.CTkLabel(master=root, image=img, text='').place(relx=0.1, rely=0.01)
customtkinter.CTkLabel(master=root, text=' URL ', font=customtkinter.CTkFont('Bold', 15)).place(relx=0.05, rely=0.35)
URL_Youtube = customtkinter.CTkEntry(master=root, width=450, text_color='green')
URL_Youtube.place(relx=0.15, rely=0.35)

Dwn_vid = customtkinter.CTkButton(master=root, text=' Download Video ', text_color='black', fg_color='#efb723',
                                  hover_color='#e0ab21', cursor='hand2', width=200,
                                  command=Download_Youtube_video).place(relx=0.10, rely=0.5)

Dwn_pl = customtkinter.CTkButton(master=root, text=' Download as Playlist ', text_color='black', fg_color='#efb723',
                                  hover_color='#e0ab21', cursor='hand2', width=200,
                                  command=download_youtube_playlist).place(relx=0.45, rely=0.5)

Convert_mp3 = customtkinter.CTkButton(master=root, text=' Convert to mp3 ', text_color='black', fg_color='#efb723',
                                      hover_color='#e0ab21', cursor='hand2', width=200,
                                      command=download_video_as_mp3).place(relx=0.10, rely=0.58)

save_place = customtkinter.CTkButton(master=root, image=img_folder, text='',
                                     fg_color='transparent', width=30, cursor='hand2', command=Path_download).place(
    relx=0.80, rely=0.5)
customtkinter.CTkLabel(master=root, text="version 3", text_color="gray", fg_color="transparent", font=customtkinter.CTkFont("bold", 10)).place(relx=0.1, rely=0.9)

root.mainloop()
