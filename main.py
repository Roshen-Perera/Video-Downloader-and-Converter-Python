
from yt_dlp import YoutubeDL

def download_video(url, quality="best", output_path="downloads"):
    """Download video or audio with the selected quality."""

    # Path to FFmpeg in the dependencies folder
    ffmpeg_path = "dependencies\\windows\\ffmpeg.exe" 

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
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'ffmpeg_location': ffmpeg_path,  # Set path to FFmpeg
    }

    # Add MP3 conversion for audio downloads
    if quality == "audio":
        audioQuality = input("Enter the quality of the audio: ")
        ydl_opts.update({
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': audioQuality,
            }]
        })
    else:
        ydl_opts['merge_output_format'] = 'mp4'   # Only apply for video downloads

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    quality = input("Enter quality (best, 1080p, 720p, 480p, audio): ").strip().lower()
    download_video(video_url, quality)
    print("Download complete!")
