class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

class Cliente(Pessoa):
    def __init__(self, nome, endereco, telefone, cpf):
        super().__init__(nome, endereco, telefone)
        self.cpf = cpf

class Funcionario(Pessoa):
    def __init__(self, nome, endereco, telefone, matricula, salario):
        super().__init__(nome, endereco, telefone)
        self.matricula = matricula
        self.salario = salario

class Produto:
    def __init__(self, nome, descricao, preco, quantidade):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

class Venda:
    def __init__(self, produtos, valor_total):
        self.produtos = produtos
        self.valor_total = valor_total
        
class Loja:
    def __init__(self):
        self.clientes = []
        self.funcionarios = []
        self.produtos = []
        self.vendas = []

    def cadastrar_cliente(self, nome, endereco, telefone, cpf):
        cliente = Cliente(nome, endereco, telefone, cpf)
        self.clientes.append(cliente)

    def cadastrar_funcionario(self, nome, endereco, telefone, matricula, salario):
        funcionario = Funcionario(nome, endereco, telefone, matricula, salario)
        self.funcionarios.append(funcionario)

    def cadastrar_produto(self, nome, descricao, preco, quantidade):
        produto = Produto(nome, descricao, preco, quantidade)
        self.produtos.append(produto)

    def realizar_venda(self, cliente, funcionario, produtos):
        valor_total = sum([produto.preco for produto in produtos])
        venda = Venda(produtos, valor_total)
        self.vendas.append(venda)

        for produto in produtos:
            produto.quantidade -= 1

        return valor_total

    def valor_total_vendas(self):
        return sum([venda.valor_total for venda in self.vendas])
