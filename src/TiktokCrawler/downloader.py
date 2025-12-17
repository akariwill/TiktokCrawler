import os
import yt_dlp
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

DOWNLOADS_DIR = "downloads"
console = Console()

def _get_ydl_opts(proxy: str = None, output_template: str = None):
    if not output_template:
        output_template = os.path.join(DOWNLOADS_DIR, '%(id)s.%(ext)s')

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': output_template,
        'noplaylist': True,
        'writedescription': False,
        'writeinfojson': False,
        'writesubtitles': False,
        'writeannotations': False,
        'quiet': True,
        'no_warnings': True,
        'ignoreerrors': True,
        'postprocessors': [{
            'key': 'FFmpegVideoRemuxer',
            'preferedformat': 'mp4',
        }],
    }
    if proxy:
        ydl_opts['proxy'] = proxy
    return ydl_opts

def download_video_to_temp(url: str, task_id: str, proxy: str = None) -> tuple[bool, str, str]:
    """
    Downloads a TikTok video to a temporary file based on the task_id.
    Returns (True, "filepath", "video_title") on success, or (False, "error_code", None) on failure.
    """
    if not os.path.exists(DOWNLOADS_DIR):
        os.makedirs(DOWNLOADS_DIR)
    
    # Define a unique filepath for this task
    output_template = os.path.join(DOWNLOADS_DIR, f'{task_id}.%(ext)s')

    try:
        ydl_opts = _get_ydl_opts(proxy=proxy, output_template=output_template)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            if info:
                # The file has been downloaded, now find its exact name
                filename = ydl.prepare_filename(info)
                video_title = info.get('title', 'video')
                console.print(f"Successfully downloaded to: {filename}", style="green")
                return True, filename, video_title
            else:
                msg = "Could not extract video information for download."
                console.print(msg, style="red")
                return False, msg, None

    except yt_dlp.utils.DownloadError as e:
        error_msg = str(e)
        console.print(f"Download failed: {error_msg}", style="red")
        if "Your IP address is blocked" in error_msg or "timed out" in error_msg:
            return False, "IP_BLOCKED", None
        return False, error_msg, None
    except Exception as e:
        msg = f"An unexpected error occurred: {e}"
        console.print(msg, style="red")
        return False, msg, None


def get_video_info(url: str, proxy: str = None) -> tuple[bool, str]:
    """
    Mendapatkan informasi video TikTok tanpa mengunduhnya.
    """
    try:
        console.print(f"Attempting to get video info using yt-dlp: {url}")
        if proxy:
            console.print(f"Using proxy: {proxy}")

        ydl_opts = {'quiet': True, 'no_warnings': True, 'ignoreerrors': True, 'simulate': True, 'skip_download': True}
        if proxy:
            ydl_opts['proxy'] = proxy

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if info:
                console.print(Panel(
                    Text(
                        f"  Title: {info.get('title', 'N/A')}\n"
                        f"  Uploader: {info.get('uploader', 'N/A')}\n"
                        f"  Upload Date: {info.get('upload_date', 'N/A')}\n"
                        f"  Duration: {info.get('duration_string', 'N/A')}\n"
                        f"  View Count: {info.get('view_count', 'N/A')}\n"
                        f"  Like Count: {info.get('like_count', 'N/A')}\n"
                        f"  Comment Count: {info.get('comment_count', 'N/A')}\n"
                        f"  URL: {info.get('webpage_url', 'N/A')}",
                        justify="left"
                    ),
                    title="[bold blue]Video Information[/bold blue]",
                    border_style="blue"
                ))
                return True, "Info retrieved successfully."
            else:
                msg = "Could not extract video information."
                console.print(msg, style="red")
                return False, msg

    except yt_dlp.utils.DownloadError as e:
        error_msg = str(e)
        console.print(f"Failed to get info: {error_msg}", style="red")
        if "Your IP address is blocked" in error_msg or "timed out" in error_msg:
            return False, "IP_BLOCKED"
        return False, error_msg
    except Exception as e:
        msg = f"An unexpected error occurred: {e}"
        console.print(msg, style="red")
        return False, msg

def download_user_videos(user_url: str, proxy: str = None) -> tuple[bool, str]:
    """
    Attempting to download all videos from user
    """
    if not os.path.exists(DOWNLOADS_DIR):
        os.makedirs(DOWNLOADS_DIR)

    try:
        console.print(f"Attempting to download all videos from user: {user_url}")
        if proxy:
            console.print(f"Using proxy: {proxy}")

        ydl_opts = _get_ydl_opts(proxy=proxy)
        ydl_opts['noplaylist'] = False
        ydl_opts['extract_flat'] = True

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(user_url, download=False)
            if info and 'entries' in info:
                console.print(f"Found {len(info['entries'])} videos for user {info.get('uploader', 'N/A')}. Starting download...", style="blue")
                ydl_opts['extract_flat'] = False
                with yt_dlp.YoutubeDL(ydl_opts) as ydl_download:
                    ydl_download.download([user_url])
                console.print(f"Successfully downloaded all available videos from {user_url} to {DOWNLOADS_DIR}", style="green")
                return True, "User videos downloaded successfully."
            else:
                msg = "Could not find any videos for this user or extract user information."
                console.print(msg, style="red")
                return False, msg

    except yt_dlp.utils.DownloadError as e:
        error_msg = str(e)
        console.print(f"Failed to download user videos: {error_msg}", style="red")
        if "Your IP address is blocked" in error_msg or "timed out" in error_msg:
            return False, "IP_BLOCKED"
        return False, error_msg
    except Exception as e:
        msg = f"An unexpected error occurred: {e}"
        console.print(msg, style="red")
        return False, msg