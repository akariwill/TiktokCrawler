<div align="center">
<a href="https://akariwill.github.io/TiktokCrawler/">
  <img src="https://github.com/akariwill/Otaku/blob/main/assets/images/akari.jpg" alt="logo" width="180" style="border-radius: 50%;"/>
</a>
</div>

<h1 align="center">
  <a href="https://akariwill.github.io/TiktokCrawler/">TiktokCrawler - TikTok Video Downloader CLI & Web</a>
</h1>

# Preview Tiktok Crawler

<p align="center">
 <img src="https://github.com/akariwill/TiktokCrawler/blob/main/assets/cli.png" alt="main" width="100%">
 This is a command-line interface (CLI) tool for downloading TikTok videos and retrieving video information.
 We also provide a web interface for easier access and functionality.
</p>

## Features

-   Download individual TikTok videos.
-   Get detailed information about a TikTok video without downloading it.
-   Download all videos from a specific TikTok user.
-   Proxy support for all commands.
-   **Web Interface**: Access download functionality via a web browser.

## Installation

TiktokCrawler can be easily installed using `pip` or `pipx`. `pipx` is recommended for installing Python CLI applications as it installs them into isolated environments and makes them directly available in your shell.

1.  **Prerequisites**:
    -   Python 3.x
    -   `ffmpeg` (required by `yt-dlp` for video processing). Make sure `ffmpeg` is installed and accessible in your system's PATH.

2.  **Install `pipx` (if you don't have it)**:
    ```bash
    pip install pipx
    pipx ensurepath
    ```
    *Note: You might need to restart your terminal after running `pipx ensurepath` for the changes to take effect.*

3.  **Install TiktokCrawler**:

    **Recommended (using `pipx`)**:
    ```bash
    pipx install tiktokcrawler
    ```

    **Alternative (using `pip`)**:
    ```bash
    pip install tiktokcrawler
    ```
    *Note: If you install with `pip`, you might need to manually add Python's user scripts directory to your system's PATH environment variable if the `tiktok-crawler` command is not found.*

## Usage (CLI)

Once installed, you can run `tiktok-crawler` directly from your terminal.

### Access Command Line Interface

```bash
tiktok-crawler --help
```

### Download a single video

To download a TikTok video, use the `download` command followed by the video URL:

```bash
tiktok-crawler download "https://www.tiktok.com/@alalten/video/7401851105526828295?lang=id-ID&q=kaori%20waguri&t=1751721831935"
```

### Get video information

To get information about a video without downloading it, use the `info` command:

```bash
tiktok-crawler info "https://www.tiktok.com/@alalten/video/7401851105526828295?lang=id-ID&q=kaori%20waguri&t=1751721831935"
```

### Download all videos from a user

To download all publicly available videos from a TikTok user, use the `user-videos` command:

```bash
tiktok-crawler user-videos "https://www.tiktok.com/@alalten/video/"
```

### Using a Proxy

You can specify a proxy for any command using the `--proxy` or `-p` option:

```bash
tiktok-crawler download "https://www.tiktok.com/@alalten/video/1234567890" --proxy "http://user:pass@host:port"
tiktok-crawler info "https://www.tiktok.com/@alalten/video/1234567890" -p "socks5://127.0.0.1:9050"
tiktok-crawler user-videos "https://www.tiktok.com/@alalten" --proxy "http://your.proxy.com:8080"
```

## Web Interface

For a more user-friendly experience, TiktokCrawler now includes a web interface.

### Running the Web Interface Locally

1.  **Install Web Dependencies**: Ensure you have installed all dependencies, including `fastapi`, `uvicorn`, and `Jinja2`. If you cloned the repository, these are in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
    *(Ensure your `venv` is active if you're using one.)*

2.  **Start the Web Server**: Navigate to the root of the project and run:
    ```bash
    uvicorn web.main:app --reload
    ```
    The web application will typically be accessible at `http://127.0.0.1:8000`. If deployed on a VPS and exposed (e.g., via `ngrok`), it might be accessible at an address like `http://160.25.222.84:8000/`.

3.  **Usage**: Open your web browser, navigate to the provided address, paste a TikTok video URL into the input field, and click "Download Video". The server will process the request in the background, and once ready, a download link will appear.

### Deploying the Web Interface to a VPS

For instructions on how to deploy and run the web interface 24/7 on a Virtual Private Server (VPS) using `ngrok`, please refer to the dedicated `DEPLOYMENT.md` file in the project root.

## Project Structure
```
TiktokCrawler/
├── LICENSE
├── README.md
├── pyproject.toml
├── src/
│   └── TiktokCrawler/
│       ├── __init__.py
│       ├── cli.py
│       └── downloader.py
├── web/
│   ├── main.py
│   ├── static/
│   │   └── style.css
│   └── templates/
│       └── index.html
└── downloads/
    ├── 7401851105526828295.mp4
    └── ...
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