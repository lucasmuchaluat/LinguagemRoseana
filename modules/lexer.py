from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'escancarar')
        # If
        self.lexer.add('IF', r'bispar')
        self.lexer.add('ELSE', r'borra')
        # While
        self.lexer.add('WHILE', r'ramerrao')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MULT', r'\*')
        self.lexer.add('DIV', r'\/')
        self.lexer.add('AND', r'\&&')
        self.lexer.add('OR', r'\|')
        self.lexer.add('MAIOR', r'\>')
        self.lexer.add('MENOR', r'\<')
        self.lexer.add('IGUAL', r'\==')
        self.lexer.add('RECEBE', r'\=')
        self.lexer.add('NOT', r'\!')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # Keys
        self.lexer.add('OPEN_KEY', r'\{')
        self.lexer.add('CLOSE_KEY', r'\}')
        # Identifier
        self.lexer.add('IDENTIFIER', r'[a-zA-Z][a-zA-Z0-9_]*')
        # Ignore spaces
        self.lexer.ignore(r'\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
