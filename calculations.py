import numpy as np

def CalcEngine():
    def __init__(self):
        self.mode = "deg"
        self.invert_trig = False
        self.e = np.e
        self.pi = np.pi

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def negate(self, a):
        return a * -1

    def sin(self, a):
        if (self.invert_trig):
            return np.sin(a)
        else:
            return np.arcsin(a)

    def cos(self, a):
        if (self.invert_trig):
            return np.cos(a)
        else:
            return np.arccos(a)
    
    def tan(self, a):
        if (self.invert_trig):
            return np.tan(a)
        else:
            return np.arctan(a)
    
    def exp(self, a, b):
        return a ^ b
    
    def sqrt(self, a):
        return np.sqrt(a)