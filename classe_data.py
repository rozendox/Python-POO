#@rozendox

#classe do tipo data
class Data:
    #função que obriga que a saida seja uma string
    #ou seja, acontece uma conversão de tipos
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

#data 1
d1 = Data()
d1.dia = 5
d1.mes = 12
d1.ano = 2019
print(d1)

#data 2
d2 = Data()
d2.dia = 7
d2.mes = 11
d2.ano = 2020
print(d2)

#meu aniversario
aniversario = Data()
aniversario.dia = 21
aniversario.mes = 3
aniversario.ano = 2023
print('meu próximo aniversário será em:', aniversario)

nascimento = Data()
nascimento.dia = 21
nascimento.mes = 3
nascimento.ano = 1999

print('Eu nasci da data de:', nascimento,',Tenho 23 anos!')
