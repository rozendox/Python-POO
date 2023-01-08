class Calculadora:
    def calcular(self,x,y,z,  operacao = '+'):

    if operacao == '+' : resultado = '%.1f + %1.f = %1.f' % (x ,y, x + z)
    elif operacao == '-': resultado = '%.1f - %1.f = %1.f' % (x, y, x - z)
    elif operacao == '*' : resultado ='%.1f x %1.f = %1.f' % (x, y, x * z)
    elif operacao == '/':
        if y == 0 resultado = 'Erro, divisão por zero!'
        else: resultado = '%.1f / %1.f = %1.f' % (x,y, x / y)
    else:
        resultado = 'nenhuma operação conhecida ( + - * /) foi requisitada.'
    print(resultado)

    calc = Calculadora()
    calc.calcular(123,123)
