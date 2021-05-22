from rply import ParserGenerator
from modules.ast import Number, Sum, Sub, Div, Mult, Print, UnOp, Identifier, Atribuicao, And, Or, Maior, Menor, Igual, NoOp, Block, If, While


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'MULT', 'DIV', 'OPEN_KEY',
             'CLOSE_KEY', 'IDENTIFIER', 'RECEBE', 'NOT', 'AND', 'OR',
             'MAIOR', 'MENOR', 'IGUAL', 'IF', 'WHILE', 'ELSE']
        )

    def parse(self):

        @self.pg.production('program : OPEN_KEY CLOSE_KEY')
        @self.pg.production('program : OPEN_KEY block CLOSE_KEY')
        def program(p):
            if len(p) == 2:
                return NoOp()
            else:
                return p[1]

        @self.pg.production('block : command')
        @self.pg.production('block : block command')
        def block(p):
            if len(p) == 2:
                p[0].children += [p[1]]
                return p[0]
            else:
                return Block([p[0]])

        @self.pg.production('command : IDENTIFIER RECEBE orexpr SEMI_COLON')
        @self.pg.production('command : PRINT OPEN_PAREN orexpr CLOSE_PAREN SEMI_COLON')
        @self.pg.production('command : WHILE OPEN_PAREN orexpr CLOSE_PAREN program')
        @self.pg.production('command : IF OPEN_PAREN orexpr CLOSE_PAREN program ELSE program')
        def command(p):
            if p[0].gettokentype() == 'IDENTIFIER':
                valorOp = p[2]
                return Atribuicao(p[0].value, valorOp)
            elif p[0].gettokentype() == 'PRINT':
                return Print(p[2])
            elif p[0].gettokentype() == 'WHILE':
                return While(p[2], p[4])
            elif p[0].gettokentype() == 'IF':
                return If(p[2], p[4], p[6])

        @self.pg.production('orexpr : andexpr OR orexpr')
        @self.pg.production('orexpr : andexpr')
        def orexpr(p):
            if len(p) == 1:
                return p[0]
            elif p[1].gettokentype() == 'OR':
                return Or(p[0], p[2])

        @self.pg.production('andexpr : eqexpr AND andexpr')
        @self.pg.production('andexpr : eqexpr')
        def andexpr(p):
            if len(p) == 1:
                return p[0]
            elif p[1].gettokentype() == 'AND':
                return And(p[0], p[2])

        @self.pg.production('eqexpr : relexpr IGUAL eqexpr')
        @self.pg.production('eqexpr : relexpr')
        def eqexpr(p):
            if len(p) == 1:
                return p[0]
            elif p[1].gettokentype() == 'IGUAL':
                return Igual(p[0], p[2])

        @self.pg.production('relexpr : expression MAIOR relexpr')
        @self.pg.production('relexpr : expression MENOR relexpr')
        @self.pg.production('relexpr : expression')
        def relexpr(p):
            if len(p) == 1:
                return p[0]
            elif p[1].gettokentype() == 'MAIOR':
                return Maior(p[0], p[2])
            elif p[1].gettokentype() == 'MENOR':
                return Menor(p[0], p[2])

        @self.pg.production('expression : term SUM expression')
        @self.pg.production('expression : term SUB expression')
        @self.pg.production('expression : term')
        def expression(p):
            if len(p) == 1:
                return p[0]
            elif p[1].gettokentype() == 'SUM':
                return Sum(p[0], p[2])
            elif p[1].gettokentype() == 'SUB':
                return Sub(p[0], p[2])

        @self.pg.production('term : factor MULT term')
        @self.pg.production('term : factor DIV term')
        @self.pg.production('term : factor')
        def term(p):
            if len(p) == 1:
                return p[0]
            elif p[1].gettokentype() == 'MULT':
                return Mult(p[0], p[2])
            elif p[1].gettokentype() == 'DIV':
                return Div(p[0], p[2])

        @self.pg.production('factor : NUMBER')
        @self.pg.production('factor : IDENTIFIER')
        @self.pg.production('factor : SUM factor')
        @self.pg.production('factor : SUB factor')
        @self.pg.production('factor : NOT factor')
        @self.pg.production('factor : OPEN_PAREN orexpr CLOSE_PAREN')
        def factor(p):
            if p[0].gettokentype() == 'NUMBER':
                return Number(p[0].value)
            elif p[0].gettokentype() == 'IDENTIFIER':
                return Identifier(p[0].value)
            elif p[0].gettokentype() == 'SUM' or p[0].gettokentype() == 'SUB' or p[0].gettokentype() == 'NOT':
                return UnOp(p[0].gettokentype(), p[1])
            elif p[0].gettokentype() == "OPEN_PAREN":
                return p[1]

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
