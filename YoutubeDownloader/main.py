import customtkinter
from PIL import Image
from pytube import YouTube
from tkinter import filedialog

root = customtkinter.CTk()
root.iconbitmap("D:\\My Projects\\Python Project\\YoutubeDownload\\Data\\icon_YT.ico")
root.title(" YT Downloader ")
root.geometry('600x600')

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    progress_var.set(percentage)
    progress_label.configure(text=f"Downloading: {int(percentage)}%")

def Download_Youtube_video():
    global download_path
    url = URL_Youtube.get()  # Get the URL from the entry field
    if url and download_path:  # Ensure both URL and download path are provided
        yt = YouTube(url,on_progress_callback=on_progress)
        stream = yt.streams.get_highest_resolution()
        stream.download(download_path)
        result_label.configure(text=f"Video downloaded to: {download_path}")
    else:
        result_label.configure(text="Please provide both a URL and a download location.")

img = customtkinter.CTkImage(
    dark_image=Image.open("D:\\My Projects\\Python Project\\YoutubeDownload\\Data\\YT Downloader By Yossef Ibrahim.png"),
    size=(400, 200))
img_folder = customtkinter.CTkImage(
    dark_image=Image.open("D:\\My Projects\\Python Project\\YoutubeDownload\\Data\\folder.png"),
    size=(25, 25))

result_label = customtkinter.CTkLabel(master=root, text="")
result_label.place(relx=0.1,rely=0.65)

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
customtkinter.CTkLabel(master=root, text=' URL ', font=customtkinter.CTkFont('Bold', 15)).place(relx=0.05, rely=0.4)
URL_Youtube = customtkinter.CTkEntry(master=root, width=450, text_color='green')
URL_Youtube.place(relx=0.15, rely=0.4)
Dwn_vid = customtkinter.CTkButton(master=root, text=' Download Video ', text_color='black', fg_color='#efb723',
                                  hover_color='#e0ab21', cursor='hand2', width=200,command=Download_Youtube_video).place(relx=0.10, rely=0.55)
save_place=customtkinter.CTkButton(master=root,image=img_folder,text='',
                                   fg_color='transparent',width=30,cursor='hand2',command=Path_download).place(relx=0.50, rely=0.55)
root.mainloop()
