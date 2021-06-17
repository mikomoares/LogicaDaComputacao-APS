dic_func = {}

class Node:
    def __init__(self):
        self.value = None
        self.children = []

    def Evaluate(self, table):
        pass

class BinOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        if (self.children[0].Evaluate(table)[1] == "string" and self.children[1].Evaluate(table)[1] == "string"):
            if(self.value == "=="):
                return (self.children[0].Evaluate(table)[0] == self.children[1].Evaluate(table)[0], "bool")
            elif(self.value == "+"):
                return (self.children[0].Evaluate(table)[0] + self.children[1].Evaluate(table)[0], "string")
            else:
                raise ValueError("ValueError exception thrown")

        
        elif (self.children[0].Evaluate(table)[1] != "string" and self.children[1].Evaluate(table)[1] != "string"):
            if self.value == '+':
                result =  self.children[0].Evaluate(table)[0] + self.children[1].Evaluate(table)[0]
            elif self.value == '-':
                result =  self.children[0].Evaluate(table)[0] - self.children[1].Evaluate(table)[0]
            elif self.value == '*':
                result =  self.children[0].Evaluate(table)[0] * self.children[1].Evaluate(table)[0]
            elif self.value == '/':
                result =  self.children[0].Evaluate(table)[0] // self.children[1].Evaluate(table)[0]
            elif(self.value == "ii"):
                result = bool((self.children[0].Evaluate(table)[0]) and bool(self.children[1].Evaluate(table)[0]))
            elif(self.value == "ow"):
                result = bool((self.children[0].Evaluate(table)[0]) or bool(self.children[1].Evaluate(table)[0]))
            elif(self.value == ">"):
                result = (self.children[0].Evaluate(table)[0] > self.children[1].Evaluate(table)[0])
            elif(self.value == "<"):
                result = (self.children[0].Evaluate(table)[0] < self.children[1].Evaluate(table)[0])
            elif(self.value == "=="):
                result = (self.children[0].Evaluate(table)[0] == self.children[1].Evaluate(table)[0])
            if (type(result) == int):
                return(result, "int")
            return (result, "bool")
        else:
            raise ValueError("ValueError exception thrown")

class UnOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        if self.value == '+':
            return (self.children[0].Evaluate(table)[0],"int")
        elif self.value == "-":
            return (-self.children[0].Evaluate(table)[0], "int")
        elif self.value == "!": 
            return (not(self.children[0].Evaluate(table)[0]), "bool")

class IntVal(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        return (self.value, "int")


class BoolVal(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        if(self.value  == "true"):
            return (True, "bool")
        elif(self.value  == "false"):
            return (False, "bool")

class StringVal(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        if type(self.value) == str:
            return (self.value, "string")
        else:
            raise ValueError("ValueError exception thrown")

class NoOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        pass

class PrintOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        if(self.children[0].Evaluate(table)[1] == "bool"):
            if(self.children[0].Evaluate(table)[0]):
                print("true")
            else:
                print("false")
        else:
            print(self.children[0].Evaluate(table)[0])

class FuncCall(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
    def Evaluate(self, table):
        func_table = SymbolTable();
        if(self.value not in dic_func):
            raise ValueError("ValueError exception thrown")
        funcDef = dic_func[self.value]
        if (len(funcDef.children[0].children)) != len(self.children):
            raise ValueError("ValueError exception thrown")
        funcDef.children[0].Evaluate(func_table)
        for i in range(len(self.children)):
            arg = self.children[i].Evaluate(table)
            if(func_table.dic_var[funcDef.children[0].children[i].value][1] == arg[1]):
                func_table.setter(funcDef.children[0].children[i].value, arg[0])
            else:
                raise ValueError("ValueError exception thrown")
        funcDef.children[1].Evaluate(func_table)

        if("ret" in func_table.dic_var):
            if funcDef.children[0].value[1] != func_table.dic_var["ret"][1]:
                raise ValueError("ValueError exception thrown")
            return func_table.dic_var["ret"]

class FuncDef(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
    def Evaluate(self, table):
        if self.value not in dic_func:
            dic_func[self.value] = self
        else:
            raise ValueError("ValueError exception thrown")

class VarDec(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
    def Evaluate(self, table):
        for i in range(len(self.children)):
            self.children[i].Evaluate(table)

class ReturnOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
    def Evaluate(self, table):
        if "ret" not in table.dic_var:
            table.dic_var["ret"] = self.children[0].Evaluate(table)

class AssignmentOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        if self.children[0] not in table.dic_var:
            return table.declare(self.children[0], self.children[1])
        else:
            raise ValueError("ValueError exception thrown")

class SetterOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        if self.children[0] in table.dic_var:
            return table.setter(self.children[0], self.children[1].Evaluate(table)[0])
        else: 
            raise ValueError("ValueError exception thrown")



class IdentifierOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        return table.getter(self.value)

class BlockOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        for f in self.children:
            f.Evaluate(table)
        
class InputOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        value = input()
        return (value, "int")

class WhileOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        while(self.children[0].Evaluate(table)[0]):
            self.children[1].Evaluate(table)

class IfOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        if self.children[0].Evaluate(table)[1] == "string":
            raise ValueError("ValueError exception thrown")
        elif self.children[0].Evaluate(table)[0]:
            self.children[1].Evaluate(table)
        elif(len(self.children) == 3):
            self.children[2].Evaluate(table)

class SymbolTable:
    def __init__(self):
        self.dic_var = {}


    def getter(self, var):
        if var in self.dic_var:
            return self.dic_var[var]
        else:
            raise ValueError("ValueError exception thrown")

    def func_getter(self, var):
        if var in self.dic_func:
            return self.dic_func[var]
        else:
            raise ValueError("ValueError exception thrown")

    def setter(self, var, value):
        if var in self.dic_var:
            if self.dic_var[var][1] == "int":
                self.dic_var[var] = (int(value), self.dic_var[var][1])
            elif self.dic_var[var][1] == "bool":
                self.dic_var[var] = (bool(value), self.dic_var[var][1])
            elif self.dic_var[var][1] == "string":
                self.dic_var[var] = (str(value), self.dic_var[var][1])
        else:
            raise ValueError("ValueError exception thrown")

    def func_setter(self, var, value):
        if var in self.dic_func:
            dic_func [var] = (var, "FUNC")
        else:
            raise ValueError("ValueError exception thrown")

    def declare(self, var, tp):
        self.dic_var[var] = (None, tp)

    def func_declare(self, var, tp):
        self.func_var[var] = (None, tp)
