from rply import ParserGenerator
from .ast import Sum, Sub, Div, Mult, Int, Equal, Great, Less

class Parser:
    def __init__(self):
        self.pg = ParserGenerator(
            ['INT', 'PRINTLN', 'WHILE',
            '=', 'EQUAL', 'LESS', 'GREAT', 'SUM', 'SUB', 'IF',
            'ELSE', 'MULT', 'DIV', ';', '(', ')', '{',
            '}', 'NOT'
            ],

            precedence=[
                ('left', ['SUM', 'SUB']),
                ('left', ['MULT', 'DIV'])
            ]
        )

    def parse(self):
        @self.pg.production('expr : INT')
        def expr_number(p):
            return Int(int(p[0].getstr()))

        @self.pg.production('expr : ( expr )')
        def expr_parens(p):
            return p[1]

        @self.pg.production('expr : expr SUM expr')
        @self.pg.production('expr : expr SUB expr')
        @self.pg.production('expr : expr MULT expr')
        @self.pg.production('expr : expr DIV expr')
        @self.pg.production('expr : expr EQUAL expr')
        @self.pg.production('expr : expr GREAT expr')
        @self.pg.production('expr : expr LESS expr')
        def expr_binop(p):
            left = p[0]
            right = p[2]
            if p[1].gettokentype() == 'SUM':
                return Sum(left, right)
            elif p[1].gettokentype() == 'SUB':
                return Sub(left, right)
            elif p[1].gettokentype() == 'MULT':
                return Mult(left, right)
            elif p[1].gettokentype() == 'DIV':
                return Div(left, right)
            elif p[1].gettokentype() == 'EQUAL':
                return Equal(left, right)
            elif p[1].gettokentype() == 'GREAT':
                return Great(left, right)
            elif p[1].gettokentype() == 'LESS':
                return Less(left, right)
            else:
                raise AssertionError('Algo deu errado!')

    def get_parser(self):
        return self.pg.build()