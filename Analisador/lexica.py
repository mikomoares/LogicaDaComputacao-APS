from rply import LexerGenerator

class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add("INT", r"\d+")
        self.lexer.add("PRINTLN", r"imputi")
        self.lexer.add("WHILE", r"inquantu")
        self.lexer.add("=", r"=")
        self.lexer.add("==", r"==")
        self.lexer.add("LESS", r"<")
        self.lexer.add("GREAT", r">")
        self.lexer.add("SUM", r"\+")
        self.lexer.add("SUB", r"-")
        self.lexer.add("IF", r"si")
        self.lexer.add("ELSE", r"sinaum")
        self.lexer.add("MULT", r"\*")
        self.lexer.add("DIV", r"\/")
        self.lexer.add(";", r";")
        self.lexer.add("(", r"\(")
        self.lexer.add(")", r"\)")
        self.lexer.add("{", r"\{")
        self.lexer.add("}", r"\}")
        self.lexer.add("NOT", r"!")
        self.lexer.add("READLN", r"imputi")

        self.lexer.ignore(r"\s+")

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()