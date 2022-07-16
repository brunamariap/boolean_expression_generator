def separar_minterms(result_1: list) -> list:
    """ Separa os minterms"""

    # Dicionário com os grupos de mintermos
    grupos_nums_1 = {'0': [], '1': [], '2': [], '3': [], '4': []}
    minterms_ordenados = []

    for linha in result_1:
        
        cont_1s = 0

        for digito in linha:
            if digito == '1':
                cont_1s += 1
        grupos_nums_1[str(cont_1s)].append(linha)
    print(grupos_nums_1)

    # acessando mintermos que estão agrupados
    for chave_grupo in grupos_nums_1:
        if len(grupos_nums_1[chave_grupo]) != 0: # entra na condição somente se o grupo não for vazio
            for entrada in grupos_nums_1[chave_grupo]:
                minterms_ordenados.append(int(entrada, 2)) # Converte número binário (que são as entradas) para decimal

    #print(minterms_ordenados)
    return grupos_nums_1


def implicantes_reduzidos(grupos_nums_1: dict, total_variaveis: int): 
    # Deleta grupos vazios 
    novos_grupos_1 = grupos_nums_1.copy() #dicionário cópia usado para percorrer o outro e apagar as chaves vazias
    implicantes_primos = set() 
    for key in novos_grupos_1: 
        if not novos_grupos_1[key]: # se a chave do dicionário estiver vazia
            grupos_nums_1.pop(key) 

    
    cont_passagem = 0
    implicantes_primos_mintermos = {} # para armazenar os implicantes e quais mintermos foram usados para criá-lo
    novos_impliantes_mintermos = {}

    while True: 
        novos_grupos_1 = {}
        usados = set() # armazena os mintermos que foram usados no agrupamento
        chaves = list(grupos_nums_1.keys()) 
        cont_passagem += 1 #conta quantas vezes o laço de repetição while iniciou
        for i in range(len(chaves) - 1): # para percorrer até a penúltima chave
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
                            if cont_passagem == 1:
                                implicantes_primos_mintermos[aux] = int(mintermo_1, 2), int(mintermo_2, 2)
                        except KeyError: 
                            novos_grupos_1[chaves[i]] = [aux] # se o grupo não estiver criado, vai criar um grupo pra adicionar a chave
                            if cont_passagem == 1:
                                implicantes_primos_mintermos[aux] = int(mintermo_1, 2), int(mintermo_2, 2)
                        usados.update([mintermo_1, mintermo_2]) #guarda quais mintermos já foram usados
        
        print(f'implicante e mintermos usados: {implicantes_primos_mintermos}')
        if usados: 
            for minterm_list in grupos_nums_1.values(): # acessa os valores do dicionário
                for minterm in minterm_list: #acessa os mintermo que está entre os valores do dicionário
                    if minterm not in usados: #vê quais foram os mintermos usado, se o mintermo não foi usado ele vai direto para o set de implicantes primos
                        implicantes_primos.add(minterm) 
            grupos_nums_1 = novos_grupos_1.copy() #o grupo de números 1 será o grupo que tinha sido alterado anteriormente
            print(f'grupos_nums_1: {grupos_nums_1}') 
        else:    # se o grupo de usador estiver vazio, que é o caso de não haver nenhuma combinação
            lista_implicantes_primos = [] 
            for implicantes in grupos_nums_1.values(): # todos os valores que estão nos grupos de qs serão implicantes primos 
                lista_implicantes_primos.extend(implicantes) 
            print(f'lista_implicantes_primos: {lista_implicantes_primos}') 
            implicantes_primos.update(lista_implicantes_primos) # retira todas as repetições que podem ter dentro da lista
            print(f'implicantes_primos: {implicantes_primos}') 
            break 

    # falta pegar o índice dos implicantes primos para contabilizar
    # fazer um dícionário, com um implicante primo sendo a chave e os valores (que podem ser uma lista) serem os os mintermos que foram agrupados para formar aquela implicante
    # quando for apagar os implicantes repetidos dentro do dicionário, fazer de forma parecida com o que foi feito com as chaves do dicionário de grupos
    # ver se a função counter funciona para contar o número de chaves do dicionário e ver se apaga apenas 1 das chaves duplicadas

    #remove as chaves que estão vazias no dicionário


def primos_essenciais(implicantes_primos: list, mintermos: list):
    implicantes_primos_essenciais = []
    for g4_minterm in mintermos:
        num_repeticoes = 0
        for g2_minterm in g4_minterm:
            for dig_inicial in range(2):
                if g2_minterm[dig_inicial]:
                    pass