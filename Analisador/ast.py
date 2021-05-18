class Int():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right


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

class Great(BinaryOp):
    def eval(self):
        return self.left.eval() > self.right.eval()

class Less(BinaryOp):
    def eval(self):
        return self.left.eval() < self.right.eval()

class Equal(BinaryOp):
    def eval(self):
        return self.left.eval() == self.right.eval()


class BinaryOp():
    def __init__(self, left):
        self.left = left

class Not(BinaryOp):
    def eval(self):
        return not(self.left.eval())


class Println():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())