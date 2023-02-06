


#Rozendox
#sistema de gerenciamento de banco

#importação das bibliotecas

import pickle
import os
import pathlib

class Account:
    accNo = 0
    name = ''
    deposit = 0
    type = ''

    def CreateAccount(self):
        self.accNo = int(input("Entre com o numero da conta"))
        self.name = input("Entre com o nome do usuário da conta")
        self.type = input("Entre com o tipe de conta, conrrente ou salário")
        self.deposit = int(input("entre com o quantia inicial(>=500 para salvar print("\n\n\nConta criada")

    def MostrarConta(self):
        print("Numero da conta:" , self.accNo)
        print("Numero do usuário da conta", self.name)
        print("Tipo de conta:", self.type)
        print("Saldo:", self.deposit)

    def ModificarConta(self):
        print("Nome do usuário da conta", self.name)
        self.name = input("modificar o nome do usuário da conta:")
        self.type = input("Modificar o tipo de conta:")
        self.deposit = int(input("Modificar o saldo"))
    
    
    # Função para depositar dinheiro
    def depositos(self, quantia):
        self.deposit += quantia
    
    
    # Função para retirar dinheiro
    def retirarfundos(self,quantia):
        self.deposit -= quantia
    
    
    # Função para mostrar os dados
    def reportar(self):
        print(self.accNo, "", self.name, "", self.type, "", self.deposit)
    
    
    # Função para mostrar o numero da conta
    def numerodaconta(self):
        return self.accNo


    # Função para mostrar o nome do usuário
    def nomeusu(self):
        return self.name


    # Função para mostrar o tipo de conta
    def tipodeconta(self):
        return self.type


    # Função para mostrar o saldo da conta
    def saldo(self):
        return self.deposit


    # Função de introdução do banco
    def introducao(self):
        print("\t\t\t\t*********************************")
        print("\t\t\t\tSistema de Gerenciamento do Banco")
        print("\t\t\t\t*********************************")

        input("press Enter to continue")



 """
 funções essenciais para o 
 funcionamento do banco
 
 """
    def WriteAccount():
        Conta = Conta()
        conta.CreateAccount()
        writeAccountsFile(conta)

    def displayall():
        file = pathlib.Path("Accounts.data")
        if file.exists():
            infile = open('accounts.data','rb')
            mylist - pickle.load(infile)
            for intem in mylist:
                print(item.accNo, " ",item.name, " ",item.type, " ",item.deposit)
            infile.close()
        else:
            print("Nenhum dado salvo encontrado para esta busca")

    def displaysSp(num)
        file = pathlib.path("accounts.data", 'rb')
        if file.exists():
            infile = open("account.data", 'rb')
            mylist - pickle.load(infile)
            infile.close()
            found = False
            for item in mylist:
                if item.accNo == num:
                    print("o saldo da sua conta é de :" item.deposit)
                    found = True
        else:
            print("Nenhum dado salvo encontrado para esta busca")
        if not found
            print("não existe nenhuma conta com este número")
            print("tente novamente")
