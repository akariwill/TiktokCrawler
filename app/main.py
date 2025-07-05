import typer
import datetime
import platform
import os
from app import downloader
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

console = Console()

def main(
    proxy: str = typer.Option(None, "--proxy", "-p", help="Proxy server to use (e.g., http://user:pass@host:port).")
):
    """
    TikTok Video Downloader CLI.
    Enter a TikTok video URL to download.
    """
    today_date = datetime.date.today().strftime("%A, %d %B %Y")
    operating_system = platform.system()
    current_directory = os.getcwd()

    cli_info = f"""Today's date is: {today_date}
My operating system is: {operating_system}
I'm currently working in the directory: {current_directory}"""

    welcome_message = Panel(
        Text(f"Welcome to TiktokCrawler!\n\n{cli_info}\n\nEnter 'exit' to quit.", justify="left"),
        title="[bold green]TiktokCrawler CLI[/bold green]",
        border_style="blue"
    )
    console.print(welcome_message)

    # Display available commands
    console.print("\n[bold yellow]Available Commands:[/bold yellow]")
    console.print("  - [cyan]download <url>[/cyan]: Download a TikTok video.")
    console.print("  - [cyan]info <url>[/cyan]: Get information about a TikTok video.")
    console.print("  - [cyan]user-videos <user_url>[/cyan]: Download all videos from a TikTok user.")
    console.print("  - [cyan]--proxy <proxy_address>[/cyan]: Use a proxy for any command.")
    console.print("\n[bold yellow]Example Usage:[/bold yellow]")
    console.print("  - [green]python -m app.cli download \"https://www.tiktok.com/@user/video/123\"[/green]")
    console.print("  - [green]python -m app.cli info \"https://www.tiktok.com/@user/video/123\" -p \"http://proxy:port\"[/green]")
    console.print("  - [green]python -m app.cli user-videos \"https://www.tiktok.com/@user\"[/green]")
    console.print("\n[bold yellow]Interactive Mode:[/bold yellow]")
    console.print("  - Just type a TikTok video URL to download it directly.")
    console.print("  - Type 'exit' to quit.")
    while True:
        video_url = Prompt.ask("[bold cyan]Enter TikTok video URL[/bold cyan]")
        if video_url.lower() == 'exit':
            break

        with console.status("[bold green]Downloading...[/bold green]") as status:
            success, message = downloader.download_video(video_url, proxy)
            if not success and message == "IP_BLOCKED":
                console.print(Panel(
                    Text("Your IP address seems to be blocked by TikTok. Please try again with a proxy.", 
                         "Example: [yellow]python main.py --proxy \"socks4://your_proxy_address:port\"[/yellow]",
                         justify="center"
                    ),
                    title="Download Failed",
                    border_style="red"
                ))
            elif not success:
                console.print(Panel(
                    Text(f"Download failed: {message}", justify="center"),
                    title="Download Failed",
                    border_style="red"
                ))
            else:
                console.print(Panel(
                    Text(f"{message}", justify="center"),
                    title="Download Successful",
                    border_style="green"
                ))

if __name__ == "__main__":
    typer.run(main)

