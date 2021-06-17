from sys import argv
import re
from nodes import *

reserved = ["printy", "inquantu", "si", "sinaum", "imputi", "int", "bool", "string", "false", "true", "ret"]

class Token:
    def __init__(self, token_type, token_value):
        self.type = token_type
        self.value = token_value

class Tokenizer:
    def __init__(self, origin):
        self.origin = origin
        self.position = 0
        self.actual = self.selectNext()

    def selectNext(self):
        num=''
        while self.position<len(self.origin) and (self.origin[self.position]=="\n" or self.origin[self.position].isspace()):
            self.position+=1
        if self.position == len(self.origin):
            new = Token("EOF", "")
        elif self.origin[self.position] == ';':
            new = Token("LB", ";")
            self.position+=1
        elif(self.origin[self.position] == "i" and self.origin[self.position+1] == "i"):
            self.position+=2
            new = Token("AND", "ii")
        elif(self.origin[self.position] == "o" and self.origin[self.position+1] == "w"):
            self.position+=2
            new = Token("OR", "ow")
        elif(self.origin[self.position].isdigit()):
            while(self.position<len(self.origin) and self.origin[self.position].isdigit()):
                num+=self.origin[self.position]
                self.position+=1
                if (self.origin[self.position].isalpha()):
                    raise ValueError("ValueError exception thrown")
            new = Token('INT', int(num))
        elif(self.origin[self.position] == '-'):
            new = Token('MINUS','-')
            self.position+=1
        elif(self.origin[self.position] == '+'):
            new = Token('PLUS','+')
            self.position+=1
        elif(self.origin[self.position] == '!'):
            new = Token('NOT','!')
            self.position+=1
        elif(self.origin[self.position] == '*'):
            new = Token('MULT','*')
            self.position+=1
        elif(self.origin[self.position] == '/'):
            new = Token('DIV','/')
            self.position+=1
        elif(self.origin[self.position] == '('):
            new = Token('(','(')
            self.position+=1
        elif(self.origin[self.position] == ')'):
            new = Token(')',')')
            self.position+=1
        elif(self.origin[self.position] == '>'):
            new = Token('GREAT','>')
            self.position+=1
        elif(self.origin[self.position] == '<'):
            new = Token('LESS','<')
            self.position+=1
        elif(self.origin[self.position] == "=" and self.origin[self.position+1] == "="):
            self.position+=2
            new = Token("EQUAL", "==")
        elif self.origin[self.position] == '=':
            new = Token("ASSIG", "=")
            self.position+=1
        elif self.origin[self.position] == '{':
            new = Token("OPEN", "{")
            self.position+=1
        elif self.origin[self.position] == '}':
            new = Token("CLOSE", "}")
            self.position+=1
        elif self.origin[self.position] == ',':
            new = Token(",", ",")
            self.position+=1
        elif self.origin[self.position] == '"':
            self.position+=1
            while self.position<len(self.origin) and (self.origin[self.position] != '"'):
                num+=self.origin[self.position]
                self.position+=1
            self.position+=1
            new = Token("STRING", num)
        elif self.origin[self.position].isalpha():
            num+=self.origin[self.position]
            self.position+=1
            while self.position<len(self.origin) and (self.origin[self.position].isdigit() or self.origin[self.position].isalpha() or self.origin[self.position]=="_"):
                num+=self.origin[self.position]
                self.position+=1

            new = num
            if num in reserved:
                new = Token(new, new)
            else: 
                new = Token("IDENT", new)
        else:
            raise ValueError("ValueError exception thrown")

        self.actual = new
        return new

class Parser:

    def parseFuncDefBlock():
        funclists = []
        while (Parser.tokens.actual.type != 'EOF'):
            if Parser.tokens.actual.type == 'int' or Parser.tokens.actual.type == 'bool' or Parser.tokens.actual.type == 'string':
                tp = Parser.tokens.actual.type
                Parser.tokens.selectNext()
                if Parser.tokens.actual.type == 'IDENT':
                    func = Parser.tokens.actual.value
                    Parser.tokens.selectNext()
                    if (Parser.tokens.actual.type == '('):
                        assig_list = []
                        Parser.tokens.selectNext()
                        while (Parser.tokens.actual.type != ')'):
                            if Parser.tokens.actual.type == 'int' or Parser.tokens.actual.type == 'bool' or Parser.tokens.actual.type == 'string':
                                tpvar = Parser.tokens.actual.type
                                Parser.tokens.selectNext()
                                if Parser.tokens.actual.type == 'IDENT':
                                    var = Parser.tokens.actual.value
                                    assig_list.append(AssignmentOp(var, [var, tpvar]))
                                    Parser.tokens.selectNext()
                                    if Parser.tokens.actual.type == ',':
                                        Parser.tokens.selectNext()
                                        if Parser.tokens.actual.type != 'int' and Parser.tokens.actual.type != 'bool' and Parser.tokens.actual.type != 'string':
                                            raise ValueError("ValueError exception thrown")
                                    elif Parser.tokens.actual.type == ')':
                                        pass
                                    else:
                                        raise ValueError("ValueError exception thrown")
                                else:
                                    raise ValueError("ValueError exception thrown")
                            else:
                                raise ValueError("ValueError exception thrown")
                        Parser.tokens.selectNext()
                        varDec = VarDec((func, tp), assig_list)
                        block = Parser.parseCommand();
                        funcDef = FuncDef(func, [varDec, block])
                        funclists.append(funcDef)
                    else:
                        raise ValueError("ValueError exception thrown")
                else:
                    raise ValueError("ValueError exception thrown")
            else:
                raise ValueError("ValueError exception thrown")
        funcCall = FuncCall('main', [])
        funclists.append(funcCall)
        return BlockOp("block", funclists)
         

    def parseBlock():
        results=[]
        if Parser.tokens.actual.type == 'OPEN':
            Parser.tokens.selectNext()
            while Parser.tokens.actual.type != 'CLOSE':
                if Parser.tokens.actual.type == 'EOF':
                    raise ValueError("ValueError exception thrown")
                results.append(Parser.parseCommand())
            Parser.tokens.selectNext()
            return BlockOp("block", results)
        else:
            raise ValueError("ValueError exception thrown")

    def parseCommand():
        if Parser.tokens.actual.type == 'IDENT':
            var = Parser.tokens.actual.value
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == 'ASSIG':
                Parser.tokens.selectNext()
                result = SetterOp("=", [var, Parser.parseOrExpr()])
            elif (Parser.tokens.actual.type == '('):
                par_list = []
                Parser.tokens.selectNext()
                while Parser.tokens.actual.type != ')':
                    par_list.append(Parser.parseOrExpr())
                    if(Parser.tokens.actual.type == ','):
                        Parser.tokens.selectNext()
                    elif (Parser.tokens.actual.type == ')'):
                        pass
                    else:
                        raise ValueError("ValueError exception thrown")
                Parser.tokens.selectNext()
                result = FuncCall(var, par_list)
            else:
                raise ValueError("ValueError exception thrown")
            if Parser.tokens.actual.type == 'LB':
                Parser.tokens.selectNext()
            else:
                raise ValueError("ValueError exception thrown")
                
        elif Parser.tokens.actual.type == 'int' or Parser.tokens.actual.type == 'bool' or Parser.tokens.actual.type == 'string':
            tp = Parser.tokens.actual.type
            Parser.tokens.selectNext()
            var = Parser.tokens.actual.value
            result = AssignmentOp(var, [var, tp])
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == "LB":
                Parser.tokens.selectNext()
            else: 
                raise ValueError("ValueError exception thrown")

        elif Parser.tokens.actual.type == 'printy':
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == '(':
                Parser.tokens.selectNext()
                result_tmp = Parser.parseOrExpr()
                if Parser.tokens.actual.type == ')':
                    Parser.tokens.selectNext()
                else:
                    raise ValueError("ValueError exception thrown")
                if Parser.tokens.actual.type == 'LB':
                    Parser.tokens.selectNext()
                else:
                    raise ValueError("ValueError exception thrown")
            result = PrintOp("PRINTY", [result_tmp])

        elif Parser.tokens.actual.type == 'inquantu':
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == '(':
                Parser.tokens.selectNext()
                expr = Parser.parseOrExpr()
                if Parser.tokens.actual.type == ')':
                    Parser.tokens.selectNext()
                    block = Parser.parseCommand()
                else:
                    raise ValueError("ValueError exception thrown")
            else:
                raise ValueError("ValueError exception thrown")
            result = WhileOp("INQUANTU", [expr,block])

        elif Parser.tokens.actual.type == 'si':
            child = []
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == '(':
                Parser.tokens.selectNext()
                expr = Parser.parseOrExpr()
                child.append(expr)
                if Parser.tokens.actual.type == ')':
                    Parser.tokens.selectNext()
                    block = Parser.parseCommand()
                    child.append(block)
                else:
                    raise ValueError("ValueError exception thrown")
                if Parser.tokens.actual.type == 'sinaum':
                    Parser.tokens.selectNext()
                    elseExpr = Parser.parseCommand()
                    child.append(elseExpr)
            else:
                raise ValueError("ValueError exception thrown")
            result = IfOp("SI", child)

        elif Parser.tokens.actual.type =='OPEN':
            result = Parser.parseBlock()

        elif Parser.tokens.actual.type =='LB':
            result = NoOp(0, [])
            Parser.tokens.selectNext()

        elif Parser.tokens.actual.type =='ret':
            Parser.tokens.selectNext()
            var = Parser.parseOrExpr()
            result = ReturnOp("ret",[var])
            if Parser.tokens.actual.type == 'LB':
                Parser.tokens.selectNext()
                while Parser.tokens.actual.type != 'CLOSE' and Parser.tokens.actual.type != 'EOF':
                    Parser.tokens.selectNext()
                if Parser.tokens.actual.type == 'EOF':
                    raise ValueError("ValueError exception thrown")
            else:
                raise ValueError("ValueError exception thrown")
        else:
            raise ValueError("ValueError exception thrown")
            
        return result



    def parseFactor():
        if Parser.tokens.actual.type == 'PLUS':
            Parser.tokens.selectNext()
            result = UnOp('+', [Parser.parseFactor()])

        elif Parser.tokens.actual.type == 'MINUS':
            Parser.tokens.selectNext()
            result = UnOp('-', [Parser.parseFactor()])
        
        elif Parser.tokens.actual.type == 'NOT':
            Parser.tokens.selectNext()
            result = UnOp('!', [Parser.parseFactor()])

        elif Parser.tokens.actual.type == '(':
            Parser.tokens.selectNext()
            result = Parser.parseOrExpr()
            if Parser.tokens.actual.type == ')':
                Parser.tokens.selectNext()
            else:
                raise ValueError("ValueError exception thrown")

        elif Parser.tokens.actual.type == 'INT':
            result = IntVal(Parser.tokens.actual.value, [])
            Parser.tokens.selectNext()
        elif Parser.tokens.actual.type == 'false' or Parser.tokens.actual.type == 'true':
            result = BoolVal(Parser.tokens.actual.value, [])
            Parser.tokens.selectNext()
        
        elif Parser.tokens.actual.type == 'STRING':
            result = StringVal(Parser.tokens.actual.value, [])
            Parser.tokens.selectNext()

        elif Parser.tokens.actual.type == 'IDENT':
            var = Parser.tokens.actual.value
            Parser.tokens.selectNext()
            if (Parser.tokens.actual.type == '('):
                par_list = []
                Parser.tokens.selectNext()
                while Parser.tokens.actual.type != ')':
                    par_list.append(Parser.parseOrExpr())
                    if(Parser.tokens.actual.type == ','):
                        Parser.tokens.selectNext()
                    elif (Parser.tokens.actual.type == ')'):
                        pass
                    else:
                        raise ValueError("ValueError exception thrown")
                Parser.tokens.selectNext()
                result = FuncCall(var, par_list)
            else:
                result =IdentifierOp(var, [])

        elif Parser.tokens.actual.type == 'imputi':
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == '(':
                Parser.tokens.selectNext()
                if Parser.tokens.actual.type == ')':
                    Parser.tokens.selectNext()
                else:
                    raise ValueError("ValueError exception thrown")
            else:
                raise ValueError("ValueError exception thrown")
            result = InputOp('imputi', [])
        else:
            raise ValueError("ValueError exception thrown")

        return result

    def parseTerm():
        result = Parser.parseFactor()

        while Parser.tokens.actual.type == 'MULT' or Parser.tokens.actual.type == 'DIV':

            if Parser.tokens.actual.type == 'DIV':
                Parser.tokens.selectNext()
                result = BinOp('/', [result, Parser.parseFactor()])

            elif Parser.tokens.actual.type == 'MULT':
                Parser.tokens.selectNext()
                result = BinOp('*', [result, Parser.parseFactor()])

        return result

    def parseExpression():
        result = Parser.parseTerm()

        while Parser.tokens.actual.type == 'PLUS' or Parser.tokens.actual.type == 'MINUS':

            if Parser.tokens.actual.type == 'MINUS':
                Parser.tokens.selectNext()
                result = BinOp('-', [result, Parser.parseTerm()])

            elif Parser.tokens.actual.type == 'PLUS':
                Parser.tokens.selectNext()
                result = BinOp('+', [result, Parser.parseTerm()])

        return result

    def parseRelExpr():
        result = Parser.parseExpression()

        while Parser.tokens.actual.type == 'GREAT' or Parser.tokens.actual.type == 'LESS':

            if Parser.tokens.actual.type == 'GREAT':
                Parser.tokens.selectNext()
                result = BinOp('>', [result, Parser.parseExpression()])

            elif Parser.tokens.actual.type == 'LESS':
                Parser.tokens.selectNext()
                result = BinOp('<', [result, Parser.parseExpression()])

        return result

    def parseEqExpr():
        result = Parser.parseRelExpr()

        while Parser.tokens.actual.type == 'EQUAL':
            Parser.tokens.selectNext()
            result = BinOp('==', [result, Parser.parseRelExpr()])

        return result

    def parseAndExpr():
        result = Parser.parseEqExpr()

        while Parser.tokens.actual.type == 'AND':
            Parser.tokens.selectNext()
            result = BinOp('ii', [result, Parser.parseEqExpr()])

        return result

    def parseOrExpr():
        result = Parser.parseAndExpr()

        while Parser.tokens.actual.type == 'OR':
            Parser.tokens.selectNext()
            result = BinOp('ow', [result, Parser.parseAndExpr()])

        return result
    
    def run(code):
        table = SymbolTable()
        filtered_code = Preproc.filter(code)
        Parser.tokens = Tokenizer(filtered_code)
        resposta = Parser.parseFuncDefBlock()
        if Parser.tokens.actual.type == 'EOF':
            resposta.Evaluate(table)
        else:
            raise ValueError("ValueError exception thrown")

class Preproc:
    def filter(code):
        filtered_code = re.sub(r"\/\*(.*?)\*\/", "", code)
        return filtered_code

file = argv[1] 
with open (file, 'r') as file:
    entry = file.read()

Parser.run(entry)
