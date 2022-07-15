def separar_minterms(result_1: list) -> list:
    """ Separa os minterms"""

    # Dicionário com os grupos de mintermos
    t_nums_1s = {'0': [], '1': [], '2': [], '3': [], '4': []}
    minterms_ordenados = []

    for linha in result_1:
        
        cont_1s = 0

        for digito in linha:
            if digito == '1':
                cont_1s += 1
        t_nums_1s[str(cont_1s)].append(linha)
    print(t_nums_1s)

    # acessando mintermos que estão agrupados
    for chave_grupo in t_nums_1s:
        if len(t_nums_1s[chave_grupo]) != 0: # entra na condição somente se o grupo não for vazio
            #print(chave_grupo)
            for entrada in t_nums_1s[chave_grupo]:
                #print(entrada)
                minterms_ordenados.append(int(entrada, 2)) # Converte número binário (que são as entradas) para decimal

    #print(minterms_ordenados)
    return t_nums_1s


def implicantes_reduzidos(grupos_nums_1: dict, total_variaveis: int):
    implicantes_primos = []
    mintermos_agrupados = []
    #criar listas com chaves chaves = list(grupos_nums_1.keys())
    chaves = list(grupos_nums_1.keys())
    print(chaves)

    for chave in grupos_nums_1:
        if len(grupos_nums_1[chave]) > 0: # checa se o grupo não está vazio
            for minterm_1 in grupos_nums_1[chave]:
                """ print("min 1:", minterm_1) """
                
                if int(chave) + 1 <= total_variaveis: #checa se não está num índice que não existe
                    if len(grupos_nums_1[str(int(chave) + 1)]) > 0: # checa se o próximo grupo não está vazio
                        for minterm_2 in grupos_nums_1[str(int(chave) + 1)]: # compara com os minterms do próximo grupo
                            """ print("min 2:", minterm_2) """
                            minterm_agrupado = []
                            num_diferencas = 0
                            indice_diferenca = 0
                            
                            for digito in range(total_variaveis):
                                if minterm_1[digito] != minterm_2[digito]:
                                    num_diferencas += 1
                                    indice_diferenca = digito
                            
                            if num_diferencas == 1: 
                                temp = list(minterm_1) #variável que armazena o mintermo temporariamente em formato de lista 
                                temp[indice_diferenca] = '-' #modifica o digito que está se alterando nos mintermos
                                implicantes_primos.append(''.join(temp))
                                minterm_agrupado.append(int(minterm_1, 2))
                                minterm_agrupado.append(int(minterm_2, 2))
                                mintermos_agrupados.append(minterm_agrupado)
    
    print(mintermos_agrupados)
    print(implicantes_primos)
    novos_implicantes = []
    novos_mintermos_agrupados = []

    # para formar novos implicantes primos
    for indice, implicante_1 in enumerate(implicantes_primos): # pega o índice e os digitos do implicante primo dentro da lista
        if indice + 1 < len(implicantes_primos): # checa se o próximo índice existe
            for ind_outros_minterms in range(indice + 1,len(implicantes_primos)): #para comparar com os próximos implicantes
                num_diferencas = 0
                indice_diferenca = 0
                novo_minterm_agrupado = [] # guarda os mintermos temporariamente
                for ind_implicante in range(total_variaveis): # iterador que permite percorrer todos os elementos de cada 
                    if implicante_1[ind_implicante] != implicantes_primos[ind_outros_minterms][ind_implicante]: #compara o primeiro implicante com os outros implicantes da lista
                        num_diferencas += 1 
                        indice_diferenca = ind_implicante
                    
                if num_diferencas == 1: # checa se o total de diferenças é apenas 1
                    temp = list(implicante_1)
                    temp[indice_diferenca] = '-'
                    novos_implicantes.append(''.join(temp))
                    """ for x in [mintermos_agrupados[indice], mintermos_agrupados[ind_outros_minterms]]: #pega o mintermo que está numa matriz
                        print(x)
                        print(mintermos_agrupados[indice])
                        novo_minterm_agrupado.append(x) """
                    novo_minterm_agrupado.append(mintermos_agrupados[indice])
                    novo_minterm_agrupado.append(mintermos_agrupados[ind_outros_minterms])
                    print(novo_minterm_agrupado)
                    novos_mintermos_agrupados.append(novo_minterm_agrupado)
    
    print(novos_implicantes)
    print(novos_mintermos_agrupados)
    return novos_implicantes, novos_mintermos_agrupados


def primos_essenciais(implicantes_primos: list, mintermos: list):
    implicantes_primos_essenciais = []
    for i in mintermos:
        for j in i:
            pass