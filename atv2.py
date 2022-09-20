
identificador = 'FEITO POR CAROLINE STEFANY BUENO DAVALOS'

# cardapio.
def menu():
    print('+---------------Cardápio------------------+')
    print('| Código | Descrição  | Pizza M | Pizza G |')
    print('| 21     | Napolitana | R$20.00 | R$26.00 |')
    print('| 22     | Margherita | R$20.00 | R$26.00 |')
    print('| 23     | Calabresa  | R$25.00 | R$32.50 |')
    print('| 24     | Toscana    | R$30.00 | R$39.00 |')
    print('| 25     | Portuguesa | R$30.00 | R$39.00 |')
    print('+-----------------------------------------+')


# função validação inteiros
def validaInt(qtd, min, max):
    while (True):
        try:
            x = int(input(qtd))
            while (((x) < (min)) or ((x) > (max))):
                invalidInput()
                x = int(input(qtd))
            return x
        except:
            invalidInput()


# função para calcular os valores
def calculoValor(value):
    # usamos while para chamar a entrada onde o cliente informa o tamanho desejado
    # chamamos também o if para calcularmos os valores das pizzas
    while True:
        tamanho = input('Qual é o tamanho desejado [M/G]? > ')
        if (tamanho == 'M') or (tamanho == 'G'):
            try:
                cod = int(input('Informe o código do sabor desejado; >'))
                if cod == 21:  # Napolitana.
                    res = 'Napolitana'
                    if tamanho == 'M':
                        value = 20
                    else:
                        value = 26
                elif cod == 22:  # Margherita.
                    res = 'Margherita'
                    if tamanho == 'M':
                        value = 20
                    else:
                        value = 26
                elif cod == 23:  # Calabresa.
                    res = 'Calabresa'
                    if tamanho == 'M':
                        value = 25
                    else:
                        value = 32.50
                elif cod == 24:  # Toscana.
                    res = 'Toscana'
                    if tamanho == 'M':
                        value = 30
                    else:
                        value = 39
                elif cod == 25:  # Portuguesa.
                    res = 'Portuguesa'
                    if tamanho == 'M':
                        value = 30
                    else:  # preço do G.
                        value = 39
                else:
                    invalidInput()
                    continue
                print(f'Você pediu uma pizza sabor: {res}, tamanho: {tamanho}')
                return value
            except:
                invalidInput()
                continue
        else:
            invalidInput()
            continue

# função para erro de entrada
def invalidInput():
    print('Opção Inválida.')


# chamaos as funçoes
print(identificador)
menu()
sub = float(0)
while True:
    sub += calculoValor(sub)
    acr = validaInt('Deseja pedir mais alguma coisa?\n1. Sim\n0. Não\n> ', 0, 1)
    if acr == 1:
        continue
    else:
        print(f'O total a ser pago é R${sub:.2f}')
        break
