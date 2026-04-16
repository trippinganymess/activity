from rich.console import Console
from rich.theme import Theme


custom_theme = Theme(
    {  
      "enter" : "bold green",
      "pull" : "bold blue",
      "release" : "bold yellow",
      "error" : "bold red"
        
    }
)


console = Console(theme=custom_theme)

