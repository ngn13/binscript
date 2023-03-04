class Lexer:
    def lex(self, code):
        lexd = []
        scode = code.split("\n")
        for inss in scode:
            if inss == "":
                continue
            if inss.startswith("!"):
                continue
            ins = inss.split(".")
            lexd.append(ins)

        return lexd