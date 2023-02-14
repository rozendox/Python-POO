"""

Rozendox

mercado

"""

import pickle
import os
import pathlib


class cliente:
    nome_cli = ''
    cod_cli = 0
    tel_cli = 0
    end_cli = ''
    gasto = 0
    renda = 0
    credito = 0

# Cadastro de clientes

    def cadastrarCliente(self,lk0):
        self.nome_cli = input("Digite o nome do cliente")
        self.cod_cli = int(input("Informe o código a ser designado para o cliente"))
        self.tel_cli = int(input("Informe o numero de celular ou telefone fixo do cliente."))
        self.end_cli = input("Infome o endereço do cliente")
        self.renda = int(input("Informe a renda do Cliente..."))
        try:
            if self.renda != 0 and self.renda > 1000:
                print("Possui renda minima para ter a carta de crédito")
                lk0 = "sim"
            if lk0 == "sim":
                self.credito = int(input("Informe A quantia em crédito que o cliente possuirá"))
            else:
                print("O cliente não possui os requisitos para ter a carta de crédito do super mercado.")
        except:
            raise Exception("""Dados incorretos para inicialização do processo de cadastro do cliente
                            na carta de crédito""")


    # Mostrar Cliente

    def mostrarCliente(self):
        print("Nome cliente: ", self.nome_cli)
        print('Código Cliente:', self.cod_cli)
        print('Telefone do cliente', self.tel_cli)
        print('Endereço do cliente', self.end_cli)
        print('Quantia gasta do cliente', self.gasto)

    # Alterar o Cadastro do Cliente

    def AlterarCadastro(self):
        print("Codigo do cliente: ", self.cod_cli)
        self.nome_cli = input("Altere o nome do cliente")
        self.tel_cli = int(input("Altere o telefone do cliente"))
        self.end_cli = input("Altere o Endereço do cliente")
        self.gasto = int(input("Altere a quantia de dinheiro gasta pelo cliente."))

    def mostrarCred(self):
        if self.credito != 0
            print("A sua em crédito é de:", self.credito)
        else:
            print("O Cliente não possui carta de credito")

    def represt(self):
        print(self.nome_cli, " ", self.cod_cli, " ", self.tel_cli, " ", self.end_cli, " ",self.gasto)


class Mercadoria:
    nome_merc = ''
    valor = 0.0
    cod_merc = 0


    def adicionarMerc(self):
        print("Complete o campo de informações para adicionar a mercadoria")
        self.nome_merc = input("Informe o nome da mercadoria")
        self.valor = float(input("Informe o valor em reais"))
        self.cod_merc = int(input("informe o código da mercadoria"))
        print("Mercadoria adicionada!, Obrigado.")

    def modificarMerc(self):
        print("Código mercadoria:", self.cod_merc)
        self.nome_merc = input("Modifique o nome da mercadoria")
        self.valor = int(input("""Modifique o valor da mercadoria em reais, utilize ponto, 
        Ex: 25.50 """))

    def ShowMerc(self):
        print("Código da mercadoria:", self.cod_merc)
        print("Nome da mercadoria:", self.nome_merc)
        print("Valor da mercadoria: ", self.valor)

    def represmerc(self):
        print()

class SaldoSupermecado:
    deposit = 0

def Saldo(self, venda):
    self.deposit += venda

# guardando o valor da função saldo na variável saldo_1

saldo_1: None = Saldo()

#essa variável é a soma automática da variável que guarda o valor da função saldo()
saldo_final: object = saldo_1 + saldo_1


# função com parametro que entra com o valor de 0 e adiciona o self gasto da classe do cliente
# e soma coma variavel que guarda o valor da soma da função saldo()
def saldocli(self,amount):
    amount = self.gasto + saldo_final


def Intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tSUPERMARKET MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")

    input("Press Enter to continue")


def writeAccount():
     cliente = cliente()
     cliente.cadastrarCliente()
     writeAccountsFile(cliente)

def DisplayAll():
    file = pathlib.Path("Dados.Conta")
    if file.exists():
        infile = open("Dados.Conta", 'rb')
        mylist - pickle.load(infile)
        for item in mylist:
            print(item.nome, " ", item.cod_cli)
        infile.close()
    else:
        print("Sem registros com esses dados.")

def displaySp(num):
    file = pathlib.path("clientes.data")
    if file.exists():
        infile = open('clientes.data', 'rb')
        mylist - pickle.load(infile)
        infile.close()
        found.close()
        found = False
        for item in mylist:
            if item.cod_cli == num:
                print("O possui a quantidade de crédito disponível de:", item.credito,
                      "e Seus gastos foram de:", item.gasto)
                found =  True
    else:
        print("Sem gravações para procurar...")
    if not found:
        print("Não existem dados gravados com esse número.")


















