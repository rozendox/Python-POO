# Rozendox




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
        self.sabado = input("Insira seu Horário de Sábado")
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
        horarios.VerHorarios(self=horarios)
    elif opcao == '2':
        horarios.definirHorarios(self=horarios)
    elif opcao == '3':
        horarios.ModificarHorarios(self=horarios,num=0)
    elif opcao == '4':
        print("\tObrigado por usar o sistema de gerenciamento pessoal de horários.")
        break
    else:
        print("Invalid choice")

    opcao = input("Enter your choice : ")










    """seg = "19:00 as 21:00 - Compiladores, 21:00 às 23:00 - POO "
    terca = "19:00 às 20:00 - Algebra Linear, 20:00 às 23:00 - Sistemas Digitais "
    "quarta = "19:00 às 21:00 - POO, 21:00 às 23:00 - Compiladores"
    quinta = "19:00 às 20:00 - Dev Web, 20:00 às 23:00 - Estatística "
    sexta = "19:00 às 21:00 - Dev web, 21:00 às 23:00 - Algebra Linear"
    sabado = "19:00 às 23:00 - Inglês"""
