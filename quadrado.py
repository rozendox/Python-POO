class quadrado:
    def __init__(self):
        self.altura = 2
        self.largura = 2

    def set_side(self, new_side):
        self.altura = new_side
        self.largura = new_side

    def get_height(self):
        return self.altura

    def set_height(self, h):
        if h >= 0:
            self.altura = h
        else:
            raise Exception("O valor precisa ser maior que sero ou maior.")


square = Square()
square.altura = 3  # raises AttributeError
