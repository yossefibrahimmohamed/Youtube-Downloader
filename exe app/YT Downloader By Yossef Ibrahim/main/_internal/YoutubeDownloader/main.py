import customtkinter
from PIL import Image
from pytubefix import YouTube
from tkinter import filedialog
import threading
from tkinter import messagebox
import os
import time
from moviepy.editor import AudioFileClip

root = customtkinter.CTk()
root.iconbitmap(r"D:\My Projects\Pycharm\YoutubeDownloader\Data\icon_YT.ico")
root.title(" YT Downloader ")
root.geometry('600x600')


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
        yt = YouTube(url, on_progress_callback=on_progress)
        video = yt.streams.filter(only_audio=True).first()
        audio_file = video.download(output_path=download_path)

        # Update UI to show conversion process
        progress_label.configure(text="Converting to MP3...")
        progress_var.set(0)

        # Conversion to MP3 in a separate thread to avoid blocking the UI
        threading.Thread(target=convert_to_mp3, args=(audio_file,)).start()
    else:
        result_label.configure(text="Please provide both a URL and a download location.")




# If ffmpeg is not found, you can set it manually
# change_settings({"FFMPEG_BINARY": "path_to_ffmpeg_executable"})

def convert_to_mp3(audio_file):
    global download_path

    try:
        # Ensure the paths are correct
        print(f"Audio file: {audio_file}")
        print(f"Download path: {download_path}")

        # Generate the MP3 file path in the download directory
        mp3_file = os.path.join(download_path, os.path.splitext(os.path.basename(audio_file))[0] + '.mp3')
        print(f"MP3 file will be saved to: {mp3_file}")

        # Create AudioFileClip
        audio_clip = AudioFileClip(audio_file)

        if audio_clip is None:
            raise ValueError("Failed to create AudioFileClip. The file might be corrupted or unsupported.")

        # Simulate progress (since moviepy doesn't provide a callback)
        for i in range(101):
            time.sleep(0.05)  # Simulate some processing time
            progress_var.set(i)
            progress_label.configure(text=f"Converting: {i}%")
            progress_label.update_idletasks()

        # Write the audio file as MP3
        audio_clip.write_audiofile(mp3_file)
        audio_clip.close()

        # Remove the original file
        os.remove(audio_file)

        # Update result label
        result_label.configure(text=f"Downloaded and converted to MP3: {mp3_file}")
        messagebox.showinfo("", "Completed ")
    except Exception as e:
        result_label.configure(text=f"An error occurred: {e}")
        print(f"Error: {e}")



def Download_Youtube_video():
    global download_path
    url = URL_Youtube.get()  # Get the URL from the entry field
    if url and download_path:  # Ensure both URL and download path are provided
        yt = YouTube(url,on_progress_callback=on_progress)
        stream = yt.streams.get_highest_resolution()
        stream.download(download_path)
        result_label.configure(text=f"Video downloaded to: {download_path}")
        messagebox.showinfo("", "Completed ")
    else:
        result_label.configure(text="Please provide both a URL and a download location.")


img = customtkinter.CTkImage(
    dark_image=Image.open(
        r"D:\My Projects\Pycharm\YoutubeDownloader\Data\YT Downloader By Yossef Ibrahim.png",),
    size=(400, 200))
img_folder = customtkinter.CTkImage(
    dark_image=Image.open(r"D:\My Projects\Pycharm\YoutubeDownloader\Data\folder.png"),
    size=(25, 25))



def Path_download():
    global download_path
    download_path = filedialog.askdirectory()  # Prompt the user to select a directory
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
Convert_mp3 = customtkinter.CTkButton(master=root, text=' Convert to mp3 ', text_color='black', fg_color='#efb723',
                                  hover_color='#e0ab21', cursor='hand2', width=200,command=download_video_as_mp3).place(relx=0.10, rely=0.58)

save_place = customtkinter.CTkButton(master=root, image=img_folder, text='',
                                     fg_color='transparent', width=30, cursor='hand2', command=Path_download).place(
    relx=0.50, rely=0.5)
customtkinter.CTkLabel(master=root,text="version 2.1",text_color="gray",fg_color="transparent",font=customtkinter.CTkFont("bold",10)).place(relx=0.1,rely=0.9)
root.mainloop()
