import string


def termos_petrick(implicantes_primos_incobertos: dict, implicantes_primos_essenciais: dict):
    termos = {}
    equacao = ''
    alfabeto = list(string.ascii_uppercase[4:])
    chaves = [x for x in implicantes_primos_incobertos]
    valores = [y for y in implicantes_primos_incobertos.values()]
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
                        equacao += '(' + alfabeto[i] + " + " + alfabeto[j] + ').'
    print(equacao[-1])