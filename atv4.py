
identificador = "Feito por Caroline Stefany Bueno Davalos"

# definimos duas variaveis para receber a lista e guardar os produtos, uma delas serve como contador
produserviList=list()
codCont=int(0)


# definimos uma função para cadastro do produto, como parametro, recebemos a variavel de contador
def cadastrarProduto(codCont):
    print('Cadastro de Produtos:')
    print('Código do Produto: {}'.format(codCont))
    nomeProduto=input('Informe o NOME do produto: ').upper()
    fabricanteProduto=input('Informe a FABRICANTE do produto: ').upper()
    valorProduto=float(input('Informe o VALOR do produto: R$'))
    produservi=dict({
    'Codigo do Produto':codCont,
    'nome do Produto':nomeProduto,
    'fabricante Produto':fabricanteProduto,
    'valor do Produto':valorProduto
    })
    produserviList.append(produservi.copy())


# definimos uma funcão de cconsultar Produtos.
def consultarProduto():
    #utilizamos o while e o if para condicionar as opções do menu
       while(True):
        try:
            print('Consulta de Produtos:')
            opt=validaInt(
            'Informe a opção desejada.\n'
            '1. Consultar todos.\n'
            '2. Consultar por CÓDIGO.\n'
            '3. Consultar por FABRICANTE.\n'
            '4. Retornar.\n> ',1,4
            )
            if((opt)==(int(1))):
                print('Consultando todos.')
                for(produto)in(produserviList):
                    for(key,value)in(produto.items()):
                        print('{}: {}'.format(key,value))
            elif((opt)==(int(2))):
                while(True):
                    try:
                        print('Consultando por Código.')
                        entry=int(input('Informe o Código:\n> '))
                        for(produto)in(produserviList):
                            if(produto['Codigo do Produto']==(entry)):
                                for(key,value)in(produto.items()):
                                    print('{}: {}'.format(key,value))
                                return
                    except:
                        print('Erro desconhecido.')
                        continue
                    print('Código não localizado.')
                    return
            elif((opt)==(int(3))):
                while(True):
                    try:
                        print('Consultando por FABRICANTE.')
                        entry=input('Informe a Fabricante:\n> ').upper()
                        for(produto)in(produserviList):
                            if(produto['fabricante Produto']==(entry)):
                                for(key,value)in(produto.items()):
                                    print('{}: {}'.format(key,value))
                        return
                    except:
                        print('Erro desconhecido.')
                        continue
            else:
                return
        except:
            print('Erro desconhecido.')
            continue

# definimos uma função para remover Produto.
def removerProduto():
    print('Exclusão de Produtos:')
    while(True):
        try:
            print('Excluíndo por CÓDIGO.')
            entry=int(input('Informe o Código:\n> '))
            for(produto)in(produserviList):
                if(produto['Codigo do Produto']==(entry)):
                    produserviList.remove(produto)
                    return
        except:
            print('Erro desconhecido.')
            continue
        print('Código não localizado.')
        return


# validamos os inteiros do menu
def validaInt(q,min,max):
    x=int(input(q))
    while(((x)<(min))or((x)>(max))):
        x=int(input(q))
    return x

# Menu.
print(identificador)
print('Bem vindo a Mercearia da Carol!')
while(True):
    try:
        option=int(validaInt(
        'Informe a opção desejada:\n'
        '1. Cadastro\n'
        '2. Filtro\n'
        '3. Exclusão\n'
        '4. Sair\n> ',1,4
        ))
        if((option)==(int(1))):
            codCont+=1
            cadastrarProduto(codCont)
        elif((option)==(int(2))):
            consultarProduto()
        elif((option)==(int(3))):
            removerProduto()
        else:
            break
    except:
        print('Error')
        continue

