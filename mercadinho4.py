class Cliente:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

class Funcionario:
    def __init__(self, nome, endereco, telefone, id_funcionario):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.id_funcionario = id_funcionario
        
class Produto:
    def __init__(self, nome, descricao, preco, quantidade):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade
        
class Venda:
    def __init__(self, cliente, funcionario, produtos, valor_total):
        self.cliente = cliente
        self.funcionario = funcionario
        self.produtos = produtos
        self.valor_total = valor_total
        
class Supermercado:
    def __init__(self):
        self.clientes = []
        self.funcionarios = []
        self.produtos = []
        self.vendas = []
        self.valor_total_vendas = 0

    def cadastrar_cliente(self, nome, endereco, telefone):
        cliente = Cliente(nome, endereco, telefone)
        self.clientes.append(cliente)

    def cadastrar_funcionario(self, nome, endereco, telefone, id_funcionario):
        funcionario = Funcionario(nome, endereco, telefone, id_funcionario)
        self.funcionarios.append(funcionario)

    def cadastrar_produto(self, nome, descricao, preco, quantidade):
        produto = Produto(nome, descricao, preco, quantidade)
        self.produtos.append(produto)

    def realizar_venda(self, id_cliente, id_funcionario, id_produtos):
        cliente = next((c for c in self.clientes if c.id_cliente == id_cliente), None)
        funcionario = next((f for f in self.funcionarios if f.id_funcionario == id_funcionario), None)
        produtos = [p for p in self.produtos if p.id_produto in id_produtos]

        valor_total = sum(p.preco for p in produtos)
        venda = Venda(cliente, funcionario, produtos, valor_total)

        self.vendas.append(venda)
        self.valor_total_vendas += valor_total
       
