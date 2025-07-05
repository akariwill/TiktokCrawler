import typer
from app import downloader
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

app = typer.Typer()
console = Console()

@app.command()
def download(
    url: str = typer.Argument(..., help="The TikTok video URL to download."),
    proxy: str = typer.Option(None, "--proxy", "-p", help="Proxy server to use (e.g., http://user:pass@host:port).")
):
    """Download a TikTok video from the given URL."""
    console.print(f"Starting download for: {url}")
    with console.status("[bold green]Downloading...[/bold green]"):
        success, message = downloader.download_video(url, proxy)
        if not success and message == "IP_BLOCKED":
            console.print(Panel(
                Text("Your IP address seems to be blocked by TikTok. Please try again with a proxy.\n" \
                     "Example: [yellow]python main.py --proxy \"socks4://your_proxy_address:port\"[/yellow]",
                     justify="center"
                ),
                title="[bold red]Download Failed[/bold red]",
                border_style="red"
            ))
        elif not success:
            console.print(Panel(
                Text(f"Download failed: {message}", justify="center"),
                title="[bold red]Download Failed[/bold red]",
                border_style="red"
            ))
        else:
            console.print(Panel(
                Text(f"[bold green]{message}[/bold green]", justify="center"),
                title="[bold green]Download Successful[/bold green]",
                border_style="green"
            ))

@app.command()
def info(
    url: str = typer.Argument(..., help="The TikTok video URL to get information from."),
    proxy: str = typer.Option(None, "--proxy", "-p", help="Proxy server to use (e.g., http://user:pass@host:port).")
):
    """Get information about a TikTok video without downloading it."""
    console.print(f"Getting info for: {url}")
    with console.status("[bold green]Fetching info...[/bold green]"):
        success, message = downloader.get_video_info(url, proxy)
        if not success:
            console.print(Panel(
                Text(f"Failed to get info: {message}", justify="center"),
                title="[bold red]Info Retrieval Failed[/bold red]",
                border_style="red"
            ))

@app.command()
def user_videos(
    user_url: str = typer.Argument(..., help="The TikTok user URL to download all videos from."),
    proxy: str = typer.Option(None, "--proxy", "-p", help="Proxy server to use (e.g., http://user:pass@host:port).")
):
    """Download all videos from a given TikTok user URL."""
    console.print(f"Starting download for user videos from: {user_url}")
    with console.status("[bold green]Downloading user videos...[/bold green]"):
        success, message = downloader.download_user_videos(user_url, proxy)
        if not success and message == "IP_BLOCKED":
            console.print(Panel(
                Text("Your IP address seems to be blocked by TikTok. Please try again with a proxy.\n" \
                     "Example: [yellow]python main.py --proxy \"socks4://your_proxy_address:port\"[/yellow]",
                     justify="center"
                ),
                title="[bold red]Download Failed[/bold red]",
                border_style="red"
            ))
        elif not success:
            console.print(Panel(
                Text(f"Download failed: {message}", justify="center"),
                title="[bold red]Download Failed[/bold red]",
                border_style="red"
            ))
        else:
            console.print(Panel(
                Text(f"[bold green]{message}[/bold green]", justify="center"),
                title="[bold green]Download Successful[/bold green]",
                border_style="green"
            ))