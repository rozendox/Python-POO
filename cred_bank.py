"""


Rozendox

card cred
bank

"""

import os
import pickle
import pathlib


class client:
    cod_cli = ''
    name = ''
    income = 0
    type = 0
    cred_cli = 0
    balance = 0

    # Essentials Account Functions

    def createAccount(self):
        self.cod_cli = input("Enter the client code")
        self.name = input("Enter the client holder account")
        self.income = int(input("Enter the income of holder account"))
        self.type = input("Enter the type of the account [C/S]")

        # manter o valor do credito do cliente igual a zero
        # só alterar na função crata crédito
        self.cred_cli = 0
        print("Conta com o nome de :", self.name, "Foi criada com sucesso, o código da conta é:",
              self.cod_cli, "Guarde esse código em um lugar seguro")
        self.balance = int(input("Enter the initial amount... 500 to save and 1000 to current"))

    def ShowClient(self):
        print("Client Code:", self.cod_cli)
        print("Client name:", self.name)
        print("Client Income", self.income)
        print("Cliente type Account", self.type)
        print("The avaible credit", self.cred_cli)

    def modifyClient(self):
        print("Client number:", self.cod_cli)
        self.name = input("Please Enter the holder account name...")
        self.income = int(input("Please enter the income of holder account..."))
        self.type = input("Please enter the type of account.... ([C/S])")

    def CartaCredito(self, cred_disp):

        if self.type == "CC":
            print("Enter the income of holder Account...")
        else:
            print("We have issues, THe entered account do not have needed requeriments.")
        if 0 < self.income < 1000:
            print("o cliente possui renda suficiente para ter a cárta de crédito")
        if 1001 < self.income < 1999:
            cred_disp = 500
            print("o crédito disponível é de R$ 500,00")
        elif 2000 < self.income < 2999:
            cred_disp = 800
        elif 3000 < self.income < 3999:
            cred_disp = 1200
        elif 4000 < self.income < 4999:
            cred_disp = 1600

        if cred_disp == 500:
            self.cred_cli = 500
        elif cred_disp == 800:
            self.cred_cli = 800
        elif cred_disp == 1200:
            self.cred_cli = 1200
        elif cred_disp == 1600:
            self.cred_cli = 1600

    # Função para reportar a conta;
    def report(self):
        print(self.cod_cli, " ", self.name, " ", self.income, " ",self.type, " ", self.cred_cli)

    # Função para pegar o codigo do cliente
    def getCodCli(self):
        print("The numer account:", self.cod_cli)

    def depositAmount(self, amount):
        self.balance += amount

    def withdrawAmount(self, amount):
        self.balance -= amount

    def GetBalance(self):
        print("The balance of the account number:", self.cod_cli)
        print(self.balance)



# funções operacinais

def intro():
    print("\t\t\t\t****************************************************")
    print("\t\t\t\tSistam de gerenciamento de cartão de crédito e banco")
    print("\t\t\t\t****************************************************")

def writeCliente():
    account = client()
    account.createAccount()
    writeAcountsFile()

def displayAll():
    file = pathlib.Path("Accounts.data")
    if file.exists():
        infile = open("Accounts.data", 'rb')
        mylist = pickle.load(infile)
        for item in mylist:
            print(item.cod_cli, " ", item.name, " ", item.type, " ", item.income, " ", item.cred_cli, " ", item.cred_cli,
                  " ", item.balance)
        infile.close()
    else:
        print("No records to display")

def displaySp(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist:
            if item.accNo == num:
                print("Your account Balance is = ", item.balance)
                found = True
    else:
        print("No records to Search")
    if not found:
        print("No existing record with this number")

def depositandWithdraw(num1, num2):
    file = pathlib.Path("Accounts.data")
    if file.exists():
        infile = open("accounts.data",'rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist:
            if item.cod_cli == num1:
                if num2 == 1:
                    amount = int(input("Enter the amount to deposit:"))
                    item.deposit += amount
                    print("Your account is updated")
                elif num2 == 2:
                    amount = int(input("Enter the amount to Withdraw:"))
                    if amount <= item.balance:
                        item.balance -= amount
                    else:
                        print("You cannot withdraw larger amount")
    else:
        print("No records to Search")
    outfile = open("newaccounts.data", 'wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccouts.data','accounts.data')


def modifyAccount():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist:
            if item.cod_cli == num:
                item.name = input("Enter the holder name:")
                item.type = input("Enter the account type")
                item.balance = int(input("Enter the amount:"))
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist,outfile)
        outfile.close()
        os.rename('newaccounts.data','accounts.data')


def writeAcountsFile(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close
        os.remove('accounts.data')
    else:
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist,outfile)
    outfile.close()
    os.rename('newaccounts.data','accounts.data')


#start of the program

ch = ''
num = 0
intro()
