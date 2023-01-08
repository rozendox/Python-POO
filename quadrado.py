"""
class quadrado:
    def __init__(self):
        self.altura = 2
        self.largura = 2

    def set_lado(self, new_side):
        self.altura = new_side
        self.largura = new_side

    def get_altura(self):
        return self.altura

    def set_altura(self, h):
        if h >= 0:
            self.altura = h
        else:
            raise Exception("O valor precisa ser igual a 0 ou maior.")


square = Square()
square.altura = 3  # gera AttributeError
"""


class quadrado:
    def __init__(self, w, h):
        self.altura = h
        self.largura = w

    def set_side(self, new_side):
        self.altura = new_side
        self.largura = new_side

    @property
    def altura(self):
        return self.altura

    @height.setter
    def altura(self, new_value):
        if new_value >= 0:
            self.altura = new_value
        else:
            raise Exception("O valor precisa ser maior que zero")
