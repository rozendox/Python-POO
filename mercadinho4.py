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
       
if __name__ == '__main__':
    mercado = Mercado()

    # Carrega dados salvos, se existirem
    try:
        with open('dados_mercado.pkl', 'rb') as arquivo:
            dados_salvos = pickle.load(arquivo)
            mercado.produtos = dados_salvos['produtos']
            mercado.clientes = dados_salvos['clientes']
            mercado.vendas = dados_salvos['vendas']
    except FileNotFoundError:
        pass

    # Loop do menu de opções
    while True:
        print('-------- MERCADINHO --------')
        print('1 - Cadastrar produto')
        print('2 - Cadastrar cliente')
        print('3 - Realizar venda')
        print('4 - Verificar estoque')
        print('5 - Verificar clientes')
        print('6 - Verificar vendas')
        print('0 - Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            mercado.cadastrar_produto()
        elif opcao == '2':
            mercado.cadastrar_cliente()
        elif opcao == '3':
            mercado.realizar_venda()
        elif opcao == '4':
            mercado.verificar_estoque()
        elif opcao == '5':
            mercado.verificar_clientes()
        elif opcao == '6':
            mercado.verificar_vendas()
        elif opcao == '0':
            # Salva dados antes de sair
            dados_salvar = {
                'produtos': mercado.produtos,
                'clientes': mercado.clientes,
                'vendas': mercado.vendas
            }
            with open('dados_mercado.pkl', 'wb') as arquivo:
                pickle.dump(dados_salvar, arquivo)
            break
