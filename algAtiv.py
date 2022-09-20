# primeiro definimos funções de calculo da porcetagem para facilitar o trabalho.
# dentro das funções definimos os parametros que serão usados.

def finalvalue(prodValue, amount, desc=0):
    value1 = prodValue * amount
    total = value1 - (value1 * desc)
    print(f'Valor SEM desconto foi R$:{value1:.2f} '
          f'\nValor COM desconto foi R$: {total:.2f} '
          f'\n(Valor do desconto: {desc * 100}%).')


# definimos uma função para saber qual desconto sera aplicado utilizando if, elif, else.
def values(prodValue, amount):
    if amount <= 4:
        # sem desconto
        finalvalue(prodValue, amount)
    elif 5 >= amount <= 19:
        # 3% de desconto
        finalvalue(prodValue, amount, 0.03)
    elif 20 >= amount <= 99:
        # 6% de desconto
        finalvalue(prodValue, amount, 0.06)
    else:
        # 10% de desconto
        finalvalue(prodValue, amount, 0.1)


# por último, definimos uma excessão para o caso de erros na digitação
def error():
    print('só são permitidos caracteres numéricos e positivos \n '
           '(utilize ponto ( . ) para separar um valor em real')


# usamos a condição while para chamar as funções que definimos anteriormente.
while True:
    try:
        print(" Feito por Caroline Stefany Bueno Davalos"
              "\n Bem vindo ao nosso atacado!")
        prodValue = float(input('Informe o valor do produto R$: '))
        amount = float(input('Informe a quantidade: '))
        if prodValue >= 0 and amount > 0:
            values(prodValue, amount)
            break
        error()
    # chamamos a função de excecão de erro
    except:
        error()
