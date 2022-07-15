def separar_minterms(result_1):

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


def primeiros_implicantes_reduzidos(grupos_nums_1, total_variaveis):
    implicantes_primos = []
    mintermos_agrupados = []
    #criar listas com chaves chaves = list(grupos_nums_1.keys())
    chaves = list(grupos_nums_1.keys())
    print(chaves)

    for chave in grupos_nums_1:
        if len(grupos_nums_1[chave]) > 0: # checa se o grupo não está vazio
            
            for minterm_1 in grupos_nums_1[chave]:
                """ print("min 1:", minterm_1) """
                
                if int(chave) + 1 < total_variaveis: #checa se não está num índice que não existe
                    if len(grupos_nums_1[str(int(chave) + 1)]) > 0: # checa se o próximo grupo não está vazio
                        for minterm_2 in grupos_nums_1[str(int(chave) + 1)]: # compara com os minterms do próximo grupo
                            """ print("min 2:", minterm_2) """
                            num_diferencas = 0
                            indice_diferenca = 0
                            for digito in range(total_variaveis):
                                if minterm_1[digito] != minterm_2[digito]:
                                    num_diferencas += 1
                                    indice_diferenca = digito
                            if num_diferencas == 1:
                                temp = list(minterm_1)
                                temp[indice_diferenca] = '-'
                                implicantes_primos.append(''.join(temp))
    
    print(implicantes_primos)
    novos_implicantes = []

    # para formar novos implicantes primos
    for indice, implicante_1 in enumerate(implicantes_primos):
        if indice + 1 < len(implicantes_primos):
            for i in range(indice + 1,len(implicantes_primos)): #para comparar com os próximos implicantes
                pass
