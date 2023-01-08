class Televisao:
    def __init__(self, polegadas, cor, resolucao, smart, entradahdmi, autofalante):
        self.polegadas = polegadas
        self.cor = cor
        self.resolucao = resolucao
        self.smart = smart
        self.entradahdmi = entradahdmi
        self.autofalante = autofalante

    @staticmethod
    def desligar():
        if Televisao == 'Ligada':
            print('Desligando')

    @staticmethod
    def ligar(televisao):
        if televisao == 'Desligada':
            print('Ligando...')

    @staticmethod
    def volume(volumeatual=0):
        botao1 = input('Pressione um botao: - ou +?')
        if botao1 == ' + ':
            print('Aumetando o Volume')
            volumeatual += 1
            print(volumeatual)
        elif botao1 == ' - ':
            print('Diminuindo o Volume')
            if volumeatual > 0:
                volumeatual = volumeatual - 1
                print(volumeatual)
            else:
                print('O volume está no mínimo')

    class ControleRemoto:
        def __init__(self, cor, tamanho, largura, profundidade):
            self.cor = cor
            self.tamanho = tamanho
            self.largura = largura
            self.profundidade = profundidade

        @staticmethod
        def PassarCanal(botao):
            if botao == ' + ':
                print('Aumentar Canal')
            elif botao == ' - ':
                print('Diminuir Canal')

        @staticmethod
        def AumentarVolume(botaovolume):
            if botaovolume == '+':
                print('aumentar volume')
            elif botaovolume == ' = ':
                print('Diminuir Volume')

        @staticmethod
        def Desligar():
            tv = 'ligada'
            if tv == 'ligada':
                print('Estou Desligando')

    controle1 = ControleRemoto('preto', '10cm', '2cm', '1,5cm')

    print(controle1.cor)
    print(controle1.PassarCanal('+'))

    controle2 = ControleRemoto('cinza', '7cm', '2cm', '1,5cm')
    print(controle2.cor, controle2.profundidade, controle2.largura, controle2.tamanho)
