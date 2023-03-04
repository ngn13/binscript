from rich.console import Console
from rich.theme import Theme
import readline

class Cli:
    def __init__(self, bsc):
        self.bsc = bsc
        self.console = Console(theme=Theme({"success":"green", "error":"bold red", "banner": "bold blue"}))

    def start(self):
        self.banner()
        while True:
            try:
                code = input("bsc >>> ")
            except:
                self.exit()
            
            if code == "":
                continue
            out = self.bsc.run(code)
            if out == True:
                self.err("Parser error")

    def banner(self):
        self.console.print("welcome to [link=https://github.com/ngn13/binscript]binscript[/link], have fun!", style="banner")

    def err(self, text):
        self.console.print("[error][-][/error] "+text)
    
    def info(self, text):
        self.console.print("[success][+][/success] "+text)
    
    def exit(self):
        self.console.print("\r")
        exit()
