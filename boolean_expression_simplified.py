from itertools import count


def separar_minterms(result_1: list) -> dict:
    """ Separa os minterms"""

    # Dicionário com os grupos de mintermos
    grupos_nums_1 = {'0': [], '1': [], '2': [], '3': [], '4': []}

    for linha in result_1:
        
        cont_1s = 0

        for digito in linha:
            if digito == '1':
                cont_1s += 1
        grupos_nums_1[str(cont_1s)].append(linha)
    print(grupos_nums_1)

    return grupos_nums_1


def implicantes_reduzidos(grupos_nums_1: dict, total_variaveis: int) -> dict: 
    # Deleta grupos vazios 
    novos_grupos_1 = grupos_nums_1.copy() #dicionário cópia usado para percorrer o outro e apagar as chaves vazias
    implicantes_primos = set() 
    for key in novos_grupos_1: 
        if not novos_grupos_1[key]: # se a chave do dicionário estiver vazia
            grupos_nums_1.pop(key) 

    cont_passagem = 0
    implicantes_primos_mintermos = {} # para armazenar os implicantes e quais mintermos foram usados para criá-lo
    novos_implicantes_mintermos = {} # para armazenar os mintermos usados para formar o implicante primo da segunda passagem

    while True: 
        novos_grupos_1 = {}
        usados = set() # armazena os mintermos que foram usados no agrupamento
        chaves = list(grupos_nums_1.keys()) 
        cont_passagem += 1 #conta quantas vezes o laço de repetição while iniciou
        for i in range(len(chaves) - 1): # para percorrer até a penúltima chave
            if cont_passagem > 2:
                break
            for mintermo_1 in grupos_nums_1[chaves[i]]: # acessa cada mintermo dentro do primeiro grupo que vai ser analisado
                for mintermo_2 in grupos_nums_1[chaves[i+1]]: # acessa cada mintermo do próximo grupo, vai até a última chave
                    qtd_diferencas = 0 
                    pos_diferenca = None 
                    for j, bit in enumerate(zip(mintermo_1, mintermo_2)): #posição do que está sendo acessada dentro de cada mintermo e o que contém em cada indice dos mintermos
                        if bit[0] != bit[1]: #só há 2 índices dentro da tupla do retorno da função
                            qtd_diferencas += 1 
                            pos_diferenca = j 
                            if qtd_diferencas > 1: 
                                break 
                    if qtd_diferencas == 1: 
                        aux = list(mintermo_1) # altera o mintermo
                        aux[pos_diferenca] = '-' 
                        aux = ''.join(aux) # tranforma em string
                        try: 
                            novos_grupos_1[chaves[i]].append(aux) # tenta adicionar o mintermo alterado em um grupo a partir do índice da chave que está no for que percorre as chaves
                        except KeyError: 
                            novos_grupos_1[chaves[i]] = [aux] # se o grupo não estiver criado, vai criar um grupo pra adicionar a chave
        
                        usados.update([mintermo_1, mintermo_2]) #guarda quais mintermos já foram usados
                        try:
                                implicantes_primos_mintermos[aux] = [int(mintermo_1, 2), int(mintermo_2, 2)]
                                novos_implicantes_mintermos[aux] = [int(mintermo_1, 2), int(mintermo_2, 2)]
                        except ValueError:
                            if aux not in novos_implicantes_mintermos:
                                for minter in [implicantes_primos_mintermos[mintermo_1], implicantes_primos_mintermos[mintermo_2]]:
                                    try:
                                        novos_implicantes_mintermos[aux].extend(minter)
                                    except KeyError:
                                        novos_implicantes_mintermos[aux] = [minter[0]]
                                        novos_implicantes_mintermos[aux].append(minter[1])
        
        if usados: 
            for minterm_list in grupos_nums_1.values(): # acessa os valores do dicionário
                for minterm in minterm_list: #acessa os mintermo que está entre os valores do dicionário
                    if minterm not in usados: #vê quais foram os mintermos usado, se o mintermo não foi usado ele vai direto para o set de implicantes primos
                        implicantes_primos.add(minterm)
                        try:
                            implicantes_primos_mintermos[minterm] = [int(minterm, 2)] 
                            novos_implicantes_mintermos[minterm] = [int(minterm, 2)]
                        except:
                            novos_implicantes_mintermos[minterm] = implicantes_primos_mintermos[minterm]
            grupos_nums_1 = novos_grupos_1.copy() #o grupo de números 1 será o grupo que tinha sido alterado anteriormente
            print(f'grupos_nums_1: {grupos_nums_1}') 

        else:    # se o grupo de usador estiver vazio, que é o caso de não haver nenhuma combinação
            """ lista_implicantes_primos = [] 
            for implicantes in grupos_nums_1.values(): # todos os valores que estão nos grupos de qs serão implicantes primos 
                lista_implicantes_primos.extend(implicantes)
            print(f'lista_implicantes_primos: {lista_implicantes_primos}') 
            implicantes_primos.update(lista_implicantes_primos) # retira todas as repetições que podem ter dentro da lista
            print(f'implicantes_primos: {implicantes_primos}')  """
            print(f'implicante e mintermos usados: {implicantes_primos_mintermos}')
            print(f'novos implicantes e mintermos usados: {novos_implicantes_mintermos}')
            break

    return novos_implicantes_mintermos


def primos_essenciais(implicantes_primos: dict) -> list:
    lista_aux = []
    mintermos_essenciais = set()
    implicantes_primos_essenciais = []
    for lista_minterms in implicantes_primos.values():
        lista_aux.extend(lista_minterms) #lista para guardar os mintermos temporariamente
    
    for i in lista_aux:
        cont = lista_aux.count(i)
        if cont == 1:
            implicantes_primos_essenciais.append(i)

    for j in implicantes_primos_essenciais:
        for chave in implicantes_primos:
            for implicante in implicantes_primos[chave]:
                if j == implicante:
                    mintermos_essenciais.add(chave)

    print(mintermos_essenciais)
    print(implicantes_primos_essenciais)
    return mintermos_essenciais


def boolean_expression_minimizer(mintermos_essenciais: set, alphabet: list):
    boolean_expression = ''
    for minterm in mintermos_essenciais:
        for indice, bit in enumerate(minterm):
            if bit == '0':
                boolean_expression += alphabet[indice] + "'"
            elif bit == '1':
                boolean_expression += alphabet[indice]
        boolean_expression += " + "
    
    return boolean_expression[:-3]