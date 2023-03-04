from binscript.lexer import Lexer
from binscript.parser import Parser

class Bsc:
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()

    def run(self, code):
        lexd = self.lexer.lex(code)
        out = self.parser.parse(lexd)
        return out

        
