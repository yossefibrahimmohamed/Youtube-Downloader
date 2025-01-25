# Youtube-Downloader-By-Yossef-Ibrahim
is a tool Maded By Eng Yossef Ibrahim using Python language and library customtkinter 

Playlist Youtube Download 


![Image](https://github.com/user-attachments/assets/cfe83b41-36a3-4c35-a445-7666e7165ccf)

version 3

when it complete it calculate all video in Playlist 

<img width="1080" alt="Image" src="https://github.com/user-attachments/assets/7a06239a-e1f6-40cc-8484-d1aaff2cc825" />


To install and use these libraries on Windows, you'll need to ensure a few system and Python-related requirements are met. Here's a breakdown:
System Requirements

    Operating System: Windows 10 or newer (64-bit recommended).
    Python Version: Python 3.8 or newer (64-bit recommended for compatibility and performance).
    Package Manager: Ensure pip (Python's package manager) is installed and up-to-date:

    python -m pip install --upgrade pip

Required Libraries and Their Installation

    CustomTkinter
        Installation:

    pip install customtkinter

    Requirement: No additional system dependencies.

Pillow (PIL)

    Installation:

    pip install pillow

    Requirement: None.

pytubefix

    Installation:

    pip install pytubefix

    Requirement: Internet access to fetch video data. It is a fork of pytube.

tkinter (Built into Python)

    Already included with Python. No installation needed.

OS (Built-in Python Module)

    No installation required.

time (Built-in Python Module)

    No installation required.

moviepy

    Installation:

    pip install moviepy

    Requirement: Requires FFmpeg for handling video/audio files.
        Install FFmpeg on Windows:
            Download FFmpeg from FFmpeg official website.
            Add the FFmpeg bin folder to your system's PATH.

urllib.error (Built-in Python Module)

    No installation required.

yt-dlp

    Installation:

pip install yt-dlp

Requirement: Internet access for fetching video data.
Optional Recommendation: Add yt-dlp executable to PATH for standalone use:

        yt-dlp --version

Optional Dependencies

    FFmpeg Configuration: If using moviepy, ensure FFmpeg is correctly set up by testing:

ffmpeg -version

PyInstaller (For creating executables):

    Installation:

pip install pyinstaller
