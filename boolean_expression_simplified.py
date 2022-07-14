# contar o núemero de vezes que um digito é igual em mintermos
# lembrar de sempre comparar os min terms com os minterms que estão num grupo com mais 1s


def separar_minterms(result_1, minterms):

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
    for chave in grupos_nums_1:

        for minterm in grupos_nums_1[chave]:
            print(minterm)

            for other_min_control in range(int(chave) + 1, len(minterm)):
                num_diferencas = 0
                print(other_min_control)
                for outro_min in range(len(grupos_nums_1[str(other_min_control)])):
                    print(outro_min)
                    for digito in range(0, len(minterm)):
                        print(digito)
                        print(minterm[digito])
                        print(grupos_nums_1[str(other_min_control)][outro_min][digito])
                        #print(grupos_nums_1[other_min_control][i = len(grupos_nums_1[other_min_control]) for i in range(len(grupos_nums_1[other_min_control]))][digito])
                        if minterm[digito] != grupos_nums_1[str(other_min_control)][outro_min][digito]:
                            num_diferencas += 1
                    print(num_diferencas)



