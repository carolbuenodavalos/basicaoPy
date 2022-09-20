
identificador = "Feito por Caroline Stefany Bueno Davalos"

# validador dos inteiros
def validaInt(qtd, min, max):  # valida se usuário digitou 0 ou 1.
    while (True):
        try:
            x = int(input(qtd))
            while (((x) < (min)) or ((x) > (max))):
                print('Informe um valor válido.')
                x = int(input(qtd))
            return x
        except:
            print('Informe um valor válido.')


# função para definir a quantidade de feijoada.
def volumeFeijoada():
    while (True):
        try:
            qtdEmMl = float(input('Informe a quantidade desejada em Ml''s(ex: 5 Litros = 5000mls):'))
            if (300 <= qtdEmMl <= 5000):
                valorqtd = (qtdEmMl * 0.08)
                return valorqtd
            print('Não aceitamos porções menores que 300ml ou maiores que 5l.')
        except:
            print('Por favor, informe um valor numérico.')


# definimos uma função para o cliente escolher a opção de feijoda
def opcaoFeijoada():
    # usamos o while e o if para definir as opções
    while (True):
        opcaoClient = input(
            'Informe a opção desejada:'
            '\nB - Básica (Feijão + paiol + costelinha)'
            '\nP - Premium (Feijão + paiol + costelinha + partes de porco)'
            '\nS - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)\n> ')
        if opcaoClient == 'B':
            multiplicador = 1
        elif opcaoClient == 'P':
            multiplicador = 1.25
        elif opcaoClient == 'S':
            multiplicador = 1.5
        else:
            print('Por favor, digite uma opção valida do cardápio')
            continue
        return multiplicador


# acompanhamentoFeijoada.
def acompanhamentoFeijoada():
    result = float(0)
    while (True):
        acomp = validaInt('Deseja algum acompanhamento?'
                          '\n0- Não desejo mais acompanhamentos (encerrar pedido)'
                          '\n1- 200g de arroz'
                          '\n2- 150g de farofa especial'
                          '\n3- 100g de couve cozida'
                          '\n4- 1 laranja descascada'
                          '\n> ', 0, 4)
        if acomp == 0:
            result += 0
            return result
        elif acomp == 1:
            result += 5
        elif acomp == 2:
            result += 6
        elif acomp == 3:
            result += 7
        else:
            result += 3


# Menu
print(identificador)
# chamamos as funções com os calculos, opções e um print com o valor final formatado.
print('Bem vindo ao restaurante Feijoada da Carol!'
      '\n Menu:')
print('\nQuantidade desejada de feijoada.')
quantidade = volumeFeijoada()
print('Opção:')
opcaoFeij = opcaoFeijoada()
print('Acompanhamentos:')
ac = acompanhamentoFeijoada()
print('O valor a ser pago é de: R${:.2f}. '
      '(Quantidade: {:.2f} * Opção de feijoada: {:.2f} + Acompanhamentos: {:.2f}).'
      .format(((quantidade * opcaoFeij) + ac), quantidade, opcaoFeij, ac))
