import tkinter
import customtkinter
from yt_dlp import YoutubeDL

def download_video():

    # Path to FFmpeg in the dependencies folder
    ffmpeg_path = "D:\Python Projects\Video Downloader and Converter\\backend\dependencies\\ffmpeg.exe" 
    

    if quality == "best":
        format_option = "bestvideo+bestaudio/best"
    elif quality == "1080p":
        format_option = "bestvideo[height=1080]+bestaudio/best"
    elif quality == "720p":
        format_option = "bestvideo[height=720]+bestaudio/best"
    elif quality == "480p":
        format_option = "bestvideo[height=480]+bestaudio/best"
    elif quality == "audio":
        format_option = "bestaudio/best"  # Audio only
    else:
        format_option = "bestvideo+bestaudio/best"  # Default to best if invalid input

    # Base options
    ydl_opts = {
        'format': format_option,
        'outtmpl': f'{"downloads"}/%(title)s.%(ext)s',
        'ffmpeg_location': ffmpeg_path,  # Set path to FFmpeg
    }

    # Add MP3 conversion for audio downloads
    if quality == "audio":
        # audioQuality = input("Enter the quality of the audio: ")
        ydl_opts.update({
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': "192",
            }]
        })
    else:
        ydl_opts['merge_output_format'] = 'mp4'   # Only apply for video downloads

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([urlVar.get()])
        print("Download complete!")


# Set appearance mode and default color theme
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Create the main window
app = customtkinter.CTk()
app.title("YouTube Downloader")
app.geometry("800x600")

# Create the widgets

# URL Label
urlLabel = customtkinter.CTkLabel(app, text="Enter YouTube video URL:")
urlLabel.pack(padx=10, pady=20)

# URL Input field
urlVar = tkinter.StringVar()
urlInput = customtkinter.CTkEntry(app, width=350, height=40, textvariable=urlVar)
urlInput.pack()

# Quality Label
qualityLabel = customtkinter.CTkLabel(app, text="Enter the quality:")
qualityLabel.pack(padx=10, pady=20)

# Quality Input field
quality = tkinter.StringVar()
qualityInput = customtkinter.CTkEntry(app , textvariable=quality)
qualityInput.pack()

download_button = customtkinter.CTkButton(app, text="Download", command=download_video)
download_button.pack(pady=20)
 
# Run the main loop
app.mainloop() 