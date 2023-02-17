class Cliente:
    def __init__(self, nome, cpf, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        
class Funcionario:
    def __init__(self, nome, cpf, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

class Produto:
    def __init__(self, nome, descricao, preco, quantidade):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade
        
class Venda:
    def __init__(self, cliente, funcionario):
        self.cliente = cliente
        self.funcionario = funcionario
        self.produtos = []
        self.valor_total = 0.0

    def adicionar_produto(self, produto, quantidade):
        if produto.quantidade < quantidade:
            raise ValueError(f"Quantidade insuficiente do produto {produto.nome}")
        produto.quantidade -= quantidade
        self.produtos.append((produto, quantidade))
        self.valor_total += produto.preco * quantidade
        
class Loja:
    def __init__(self):
        self.clientes = []
        self.funcionarios = []
        self.produtos = []
        self.vendas = []

    def cadastrar_cliente(self, nome, cpf, endereco, telefone):
        cliente = Cliente(nome, cpf, endereco, telefone)
        self.clientes.append(cliente)

    def cadastrar_funcionario(self, nome, cpf, endereco, telefone):
        funcionario = Funcionario(nome, cpf, endereco, telefone)
        self.funcionarios.append(funcionario)

    def cadastrar_produto(self, nome, descricao, preco, quantidade):
        produto = Produto(nome, descricao, preco, quantidade)
        self.produtos.append(produto)

    def registrar_venda(self, cliente, funcionario, produtos):
        venda = Venda(cliente, funcionario)
        for produto, quantidade in produtos:
            venda
