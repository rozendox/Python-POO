# Rozendox

import pathlib
import os
import pickle



class horarios:
    segunda = ''
    terca = ''
    quarta = ''
    quinta = ''
    sexta = ''
    sabado = ''


    def definirHorarios(self):
        print("Bem vindo ao sistema de Definição de Horários")
        self.segunda = input("Insira seu Horário da segunda feira.")
        self.terca = input("Insira seu Horário da Terça feira")
        self.quarta = input("Insira seu Horário da Quarta Feira")
        self.quinta = input("Insira seu Horário da Quinta Feira")
        self.sexta = input("Insira seu Horário da Sexta feira")
        print("Operação Terminada.")

        input("Pressione Enter para sair.")

    def ModificarHorarios(self, num):
        print("Bem-Vindo(a) ao sistema de Modificação de Horários.")
        print("Qual dia da semana deseja Alterar?")
        num = int(input("Digite o dia da semana [1- seg, 2- ter, 3- qua, 4- qui, 5- sex, 6- sab ]"))

        while num != 7:
            if num == 1:
                self.segunda = input("Informe seu novo horário de -SEGUNDA-FEIRA-")
            elif num == 2:
                self.terca = input("Informe seu novo horário de -TERÇA-FEIRA-")
            elif num == 3:
                self.quarta = input("Informe seu novo horário de -QUARTA-FEIRA-")
            elif num == 4:
                self.quinta = input("Informe seu novo horário de -QUARTA-FEIRA-")
            elif num == 5:
                self.sexta = input("Informe seu novo horário de -SEXTA-FEIRA-")
            elif num == 6:
                self.sabado = input("informe seu novo horário de -SÁBADO-")
            elif num == 7:
                print("Obrigado Por usar o Sistema de Modificação de Horários!")
                input("Pressione enter para sair.")
            break
        else:
            print("Invalid choice")

    def VerHorarios(self):
        print(self.segunda)
        print(self.terca)
        print(self.quarta)
        print(self.quinta)
        print(self.sabado)


def introducao():
    print("\t\t\t\t*********************************")
    print("\t\t\t\tSistema de Gerenciamento de Horarios")
    print("\t\t\t\t*********************************")

    input("press Enter to continue")


def EscreverHorario():
    horario = horarios()
    horario.definirHorarios()
    definirHorariosFile(horario)


def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        for item in mylist:
            print(item.segunda, " ", item.terca, " ", item.quarta, " ", item.quinta, " ", item.quinta, " ", item.sexta,
                  " ",item.sabado)
        infile.close()
    else:
        print("No records to display")



introducao()





opcao = ''
while opcao != 4:
    # system("cls");
    print("\t**MAIN MENU**")
    print("\t1. VER HORÁRIOS")
    print("\t2. DEFINIR HORARIOS")
    print("\t3. MODIFICAR HORARIOS")
    print("\t4. EXIT")
    print("\tSelect Your Option (1-4) ")
    opcao = input()
    # system("cls");

    if opcao == '1':
        horarios.VerHorarios()
    elif opcao == '2':
        horarios.definirHorarios(horarios)
    elif opcao == '3':
        horarios.ModificarHorarios()
    elif opcao == '4':
        print("\tObrigado por usar o sistema de gerenciamento pessoal de horários.")
        break
    else:
        print("Invalid choice")

    opcao = input("Enter your choice : ")
