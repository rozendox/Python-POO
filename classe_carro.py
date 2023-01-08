class carro():
    def __init__(self , marca, modelo, ano, tanque ):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.tanque = int(tanque)

    def ligar(self):
        print('o carro está ligando')

    def desligar(self):
        print('estou desligando')

    def abrir_port(self):
        print('esto abrindo as portas')

    def fechar_port(self):
        print('estou fechando as portas')


carro1 = carro('chevrolet', 'chevette', '1994', 30)
print(carro1.marca, carro1.modelo, carro1.ano)
carro2 = carro('fiat', 'uno', '1993', 25)
print(carro2.marca, carro2.modelo, carro2.ano)
