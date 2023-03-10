class Operacoes:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Define os métodos de operações matemáticas
    soma = lambda self: self.a + self.b
    subtracao = lambda self: self.a - self.b
    multiplicacao = lambda self: self.a * self.b
    divisao = lambda self: self.a / self.b if self.b != 0 else "Não é possível dividir por zero"

# Criação do objeto e uso dos métodos
op = Operacoes(10, 5)
print("Soma:", op.soma())
print("Subtração:", op.subtracao())
print("Multiplicação:", op.multiplicacao())
print("Divisão:", op.divisao())

# Alteração dos valores dos atributos
op.a = 20
op.b = 0
print("Divisão:", op.divisao())
