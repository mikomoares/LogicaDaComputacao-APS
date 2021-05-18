from Analisador.lexica import Lexer
from Analisador.parser import Parser

text_input = "(4 + 4) * 8 > 10"

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
print(parser.parse(tokens).eval())