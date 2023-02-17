class Cliente:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        
class Produto:
    def __init__(self, nome, descricao, preco, quantidade):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade
        
class Loja:
    def __init__(self):
        self.clientes = []
        self.produtos = []

    def cadastrar_cliente(self, nome, endereco, telefone):
        cliente = Cliente(nome, endereco, telefone)
        self.clientes.append(cliente)

    def cadastrar_produto(self, nome, descricao, preco, quantidade):
        produto = Produto(nome, descricao, preco, quantidade)
        self.produtos.append(produto)
        
loja = Loja()

# cadastrar um cliente
loja.cadastrar_cliente("João Silva", "Rua A, 123", "(11) 99999-9999")

# cadastrar um produto
loja.cadastrar_produto("Arroz", "Arroz branco", 10.99, 100)

