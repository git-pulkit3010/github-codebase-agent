# utils.py
from rich.console import Console
from rich.markdown import Markdown

console = Console()

def colored_print(text, color="white"):
    styles = {
        "green": "bold green",
        "yellow": "bold yellow",
        "red": "bold red",
        "blue": "bold blue",
        "magenta": "bold magenta",
        "cyan": "bold cyan",
        "white": "white",
    }
    console.print(text, style=styles.get(color, "white"))

def pretty_print(text):
    try:
        md = Markdown(text, code_theme="monokai")  # Options: monokai, dracula, etc.
        console.print(md)
    except Exception as e:
        console.print("[bold red]Error rendering output:[/bold red]", str(e))
