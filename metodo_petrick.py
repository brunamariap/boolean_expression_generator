import string


def termos_petrick(implicantes_primos_incobertos: dict, implicantes_primos_essenciais: dict):
    termos = {}
    equacao = ''
    alfabeto = list(string.ascii_uppercase[4:])
    chaves = [x for x in implicantes_primos_incobertos]
    valores = [y for y in implicantes_primos_incobertos.values()]
    letras_equacao = []
    print('valores', valores)
    for i in range(len(chaves)):
        termos[(f'{alfabeto[i]}', chaves[i])] = valores[i]
    print('termos',termos)

    # formar a equação de Petrick
    for i in range(len(chaves) - 1): #vai até o penúltimo índice do dicionário 
        for mintermo_1 in implicantes_primos_incobertos[chaves[i]]: #primeiro mintermo a ser analisado
            #print('termo 1',termo_1)
            for j in range(i + 1, len(chaves)): #para checar se tem algum mintermo igual dentro do dicionário
                #print('j', j)
                for mintermo_2 in implicantes_primos_incobertos[chaves[j]]:
                    #print('termo 2',termo_2)
                    if mintermo_1 == mintermo_2:
                        equacao += '(' + alfabeto[i] + "+" + alfabeto[j] + ').'
                        letras_equacao.append([alfabeto[i], alfabeto[j]])
    print(equacao[:-1])
    print(letras_equacao)
    print(distributiva(equacao[:-1], letras_equacao))


def distributiva(equacao, letras_equacao):
    equacao = equacao.split('.')
    print(equacao)
    nova_equacao = []
    nova_equacao2 = ''
    for i in range(len(equacao)):
        nova_equacao.append(list(equacao[i]))
    
    #teste de como seria a nova equação, mas a condição nunca é verdadeira
    for i in range(0,len(letras_equacao) - 1):

        for j in range(i + 1, len(letras_equacao)):
            for letra in letras_equacao[j]:
                print(letra)
                if letras_equacao[i] == letra:
                    nova_equacao2 += '(' + letras_equacao[i] + '+' + letras_equacao[i + 1] + letra + ')'

    print(nova_equacao2)
    print(nova_equacao)