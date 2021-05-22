from modules.lexer import Lexer
from modules.parser import Parser
from modules.ast import SymbolTable
import sys


with open("./code.txt", "r") as f:
    text_input = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

# for token in tokens:
#     print(token)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()
