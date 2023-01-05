"""

multistorage python
@rozendo


O intuito é fixar os conhecimentos de classes em python
realizando uma grande operação onde classes se relacionam
independente da dinstinção de serviços
"""


class FormaDePagamento:
    def __init__(self, bandeira, cartao_deb, cartao_cred, a_vista, pix):
        # bandeira do cartao para registro no caixa
        self.bandeira = bandeira
        # cartão de débito
        self.cartao_deb = cartao_deb
        # cartão de crédito
        self.cartao_cred = cartao_cred
        # a vista
        self.a_vista = a_vista
        # pix
        self.pix = pix


class Cliente:
    def __init__(self, nome, idade, end, telefone):
        # nome do cliente
        self.nome = nome
        # idade do cliente
        self.idade = idade
        # endereço do cliente
        self.end = end
        # telefone do cliente
        self.telefone = telefone

    # função de verificação de nomes duplicados em variáveis

    @staticmethod
    def verifica(x, z):
        if x == z:
            print("Nome está du plicado")


class Carro:
    def __init__(self, marca, modelo, ano, cor):
        # marca do carro
        self.marca = marca
        # modelo do carro
        self.modelo = modelo
        # ano do carro
        self.ano = ano
        # cor do carro
        self.cor = cor


class Produto:
    def __init__(self, nome_produto, validade_prod, data_fab, valor_prod, cod_barras):
        # nome do produto
        self.nome_produto = nome_produto

        # validade
        self.validade_prod = validade_prod

        # data de fabricação
        self.data_fab = data_fab

        # Valor atribuído ao produto
        self.valor_prod = valor_prod

        # Codigo de barras do produto
        self.cod_barras = cod_barras

    # função que retorna o valor do produto para chamar em outras classes
    def valor(self):
        return self.valor_prod

    # função que retorna o codigo de barras do produto para chamar em outras classes
    def cod(self):
        return self.cod_barras


class Mecanica:
    def __init__(self, Cliente, Carro):
        self.Cliente = Cliente
        print(self.Cliente.nome)
        print(self.Cliente.end)
        print(self.Cliente.telfone)
        self.Carro = Carro


class SuperMercado:
    def __init__(self, Cliente, Produto):
        self.Cliente = Cliente
        print(self.Cliente.nome)
        self.Produto = Produto
        print(self.Produto.valor)
        print(self.Produto.cod_barras)

    def compra(self, valor_total):
        valor_total = input("digite o valor dos produtos")


class LojinhaCell:
    def __init__(self, Cliente, tipo_cell, tipo_serv, ):
        # Nome do Cliente

        self.Cliente = Cliente
        print(self.Cliente.nome)

        # #tipo_de_celular
        self.tipo_cell = tipo_cell

        # #tipo_de_serviço
        self.tipo_serv = tipo_serv


@property
def pagamento(FormaDePagamento):
    x = input("informa a forma de pagamento: Cartão Débito, Cartão Crédito, pix, a vista")
    if x == "Cartão Débito":
        return FormaDePagamento.cartao_deb
    elif x == "Cartão Crédito":
        return FormaDePagamento.cartao_cred
    elif x == "pix":
        return FormaDePagamento.pix
    elif x == "a vista":
        return FormaDePagamento.a_vista
    else:
        print('- Opção inválida, Por favor, tente novamente -')
