<div align="center">
<a href="https://akariwill.github.io/TiktokCrawler/">
  <img src="https://github.com/akariwill/Otaku/blob/main/assets/images/akari.jpg" alt="logo" width="180" style="border-radius: 50%;"/>
</a>
</div>

<h1 align="center">
  <a href="https://akariwill.github.io/TiktokCrawler/">TiktokCrawler - TikTok Video Downloader CLI</a>
</h1>

# Preview Tiktok Crawler

<p align="center">
 <img src="https://akariwill.github.io/TiktokCrawler/assets/cli.png/" alt="main" width="100%">
 This is a command-line interface (CLI) tool for downloading TikTok videos and retrieving video information.
</p>

## Features

-   Download individual TikTok videos.
-   Get detailed information about a TikTok video without downloading it.
-   Download all videos from a specific TikTok user.
-   Proxy support for all commands.

## Installation

1.  **Prerequisites**:
    -   Python 3.x
    -   `ffmpeg` (required by `yt-dlp` for video processing). Make sure `ffmpeg` is installed and accessible in your system's PATH.

2.  **Clone the repository (if you haven't already)**:
    ```bash
    git clone https://github.com/akariwill/TiktokCrawler.git 
    cd TiktokCrawler
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

This tool uses `typer` for its command-line interface. You can run commands directly from the `app/cli.py` module.

## Access Command Line Interface

This tool uses `typer` for its command-line interface. You can run commands directly from the `app/cli.py` module.

```bash
python -m app.main"
```

### Download a single video

To download a TikTok video, use the `download` command followed by the video URL:

```bash
python -m app.cli download "https://www.tiktok.com/@alalten/video/7401851105526828295?lang=id-ID&q=kaori%20waguri&t=1751721831935"
```

### Get video information

To get information about a video without downloading it, use the `info` command:

```bash
python -m app.cli info "https://www.tiktok.com/@alalten/video/7401851105526828295?lang=id-ID&q=kaori%20waguri&t=1751721831935"
```

### Download all videos from a user

To download all publicly available videos from a TikTok user, use the `user-videos` command:

```bash
python -m app.cli user-videos "https://www.tiktok.com/@alalten/video/"
```

### Using a Proxy

You can specify a proxy for any command using the `--proxy` or `-p` option:

```bash
python -m app.cli download "https://www.tiktok.com/@alalten/video/1234567890" --proxy "http://user:pass@host:port"
python -m app.cli info "https://www.tiktok.com/@alalten/video/1234567890" -p "socks5://127.0.0.1:9050"
python -m app.cli user-videos "https://www.tiktok.com/@alalten" --proxy "http://your.proxy.com:8080"
```

## Project Structure
```
TiktokCrawler/
├── LICENSE
├── README.md
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── cli.py
│   ├── downloader.py
│   ├── main.py
│   └── __pycache__/
│       ├── __init__.cpython-313.pyc
│       ├── cli.cpython-313.pyc
│       ├── downloader.cpython-313.pyc
│       └── main.cpython-313.pyc
└── downloads/
    ├── 7401851105526828295.mp4
    └── 7439977461644840208.mp4
```

## License
This project is licensed under the MIT License.

## Contact

Thank You for passing by!!
If you have any questions or feedback, please reach out to us at [contact@akariwill.id](mailto:mwildjrs23@gmail.com?subject=[TiktokCrawler]%20-%20Your%20Subject).
<br>
or you can DM me on Discord `wildanjr_` or Instagram `akariwill`. (just contact me on one of these account)

## Contributing

Feel free to contribute to this project by submitting pull requests or opening issues in the repository.

---