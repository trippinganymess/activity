from rich.console import Console
from rich.theme import Theme


custom_theme = Theme(
    {  
      "enter" : "italic green",
      "pull" : "italic blue",
      "release" : "italic yellow",
      "error" : "bold red"
        
    }
)


console = Console(theme=custom_theme)

