dictGlobal = {}


class SymbolTable():
    @staticmethod
    def getter(key):
        return dictGlobal[key]

    @staticmethod
    def setter(key, value):
        dictGlobal[key] = value


class Identifier():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return SymbolTable.getter(self.value)


class While():
    def __init__(self, condition, command1):
        self.condition = condition
        self.command1 = command1

    def eval(self):
        while self.condition.eval():
            self.command1.eval()


class If():
    def __init__(self, condition, command1, command2):
        self.condition = condition
        self.command1 = command1
        self.command2 = command2

    def eval(self):
        if self.condition.eval():
            self.command1.eval()
        else:
            self.command2.eval()


class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class UnOp():
    def __init__(self, tipo, valor):
        self.type = tipo
        self.value = valor

    def eval(self):
        if self.type == "SUM":
            return self.value.eval()
        elif self.type == "SUB":
            return -self.value.eval()
        elif self.type == "NOT":
            return int(not self.value.eval())


class NoOp():
    def eval(self):
        return


class Block():
    def __init__(self, nodeList=[]):
        self.children = nodeList

    def eval(self):
        for child in self.children:
            child.eval()


class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Atribuicao(BinaryOp):
    def eval(self):
        return SymbolTable.setter(self.left, self.right.eval())


class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Mult(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()


class Or(BinaryOp):
    def eval(self):
        return int(bool(self.left.eval() or self.right.eval()))


class And(BinaryOp):
    def eval(self):
        return int(bool(self.left.eval() and self.right.eval()))


class Maior(BinaryOp):
    def eval(self):
        return int(bool(self.left.eval() > self.right.eval()))


class Menor(BinaryOp):
    def eval(self):
        return int(bool(self.left.eval() < self.right.eval()))


class Igual(BinaryOp):
    def eval(self):
        return int(bool(self.left.eval() == self.right.eval()))


class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())
