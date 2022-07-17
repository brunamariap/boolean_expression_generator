from metodo_petrick import *
from boolean_expression import boolean_expression_minimizer


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


def mintermos_representados(implicantes_primos_mintermos,implicante: str, cont_passagens: int, usados, mintermo_1, mintermo_2) -> dict:
    if usados:
        if cont_passagens == 1 and '-' not in implicante: #quando mintermo_1 não tem nenhum valor, seria o caso que entra apenas nos usados
            implicantes_primos_mintermos[implicante] = [int(implicante, 2)]
        elif '-' not in mintermo_1 and '-' not in mintermo_2 and mintermo_1:
            implicantes_primos_mintermos[implicante] = [int(mintermo_1, 2), int(mintermo_2, 2)]

    # mintermos que foram combinados para formar o novo implicante
    if implicante not in implicantes_primos_mintermos:
            for minter in [implicantes_primos_mintermos[mintermo_1], implicantes_primos_mintermos[mintermo_2]]:
                try:
                    implicantes_primos_mintermos[implicante].extend(minter)
                except KeyError:
                    implicantes_primos_mintermos[implicante] = [x for x in implicantes_primos_mintermos[mintermo_1]]
    
    return implicantes_primos_mintermos


def implicantes_reduzidos(grupos_nums_1: dict, total_variaveis: int) -> dict: 
    # Deleta grupos vazios 
    novos_grupos_1 = grupos_nums_1.copy() 
    implicantes_primos = set() 
    for key in novos_grupos_1:
        if not novos_grupos_1[key]: 
            grupos_nums_1.pop(key) 

    implicantes_mintermos = {}
    minterm_representado = {}
    cont_passagens = 0
    
    while True: 
        novos_grupos_1 = {} 
        usados = set() # armazena os mintermos que foram usados no agrupamento
        cont_passagens += 1
        chaves = list(grupos_nums_1.keys()) 
        for i in range(len(chaves) - 1): 
            for mintermo_1 in grupos_nums_1[chaves[i]]: 
                for mintermo_2 in grupos_nums_1[chaves[i+1]]: 
                    qtd_diferencas = 0 
                    pos_diferenca = None 
                    for j, digito in enumerate(zip(mintermo_1, mintermo_2)): 
                        if digito[0] != digito[1]: 
                            qtd_diferencas += 1 
                            pos_diferenca = j 
                            if qtd_diferencas > 1: 
                                break 
                    if qtd_diferencas == 1: 
                        aux = list(mintermo_1) 
                        aux[pos_diferenca] = '-' 
                        aux = ''.join(aux) 
                        try: 
                            novos_grupos_1[chaves[i]].append(aux)  
                        except KeyError: 
                            novos_grupos_1[chaves[i]] = [aux] 
                        usados.update([mintermo_1, mintermo_2])
                        minterm_representado.update(mintermos_representados(minterm_representado, aux, cont_passagens, usados, mintermo_1, mintermo_2))
     
        if usados: 
            for minterm_list in grupos_nums_1.values(): 
                for minterm in minterm_list: 
                    if minterm not in usados: 
                        implicantes_primos.add(minterm)
                        minterm_representado.update(mintermos_representados(minterm_representado, minterm, cont_passagens, usados, mintermo_1, mintermo_2)) 
            grupos_nums_1 = novos_grupos_1.copy() 
            print(f'grupos_nums_1: {grupos_nums_1}') 
        else:    
            lista_implicantes_primos = [] 
            for implicantes in grupos_nums_1.values(): 
                lista_implicantes_primos.extend(implicantes) 
            print(f'lista_implicantes_primos: {lista_implicantes_primos}') 
            implicantes_primos.update(lista_implicantes_primos) 
            print(f'implicantes_primos: {implicantes_primos}')

            for minterm in implicantes_primos:
                for chave in minterm_representado:
                    if minterm == chave:
                        implicantes_mintermos[chave] = [x for x in minterm_representado[chave]]

            print(implicantes_mintermos) 
            break
    
    return implicantes_mintermos


def primos_essenciais(implicantes_primos: dict):
    lista_aux = []
    incobertos = {} # para armazenar os implicantes e os minntermos que não foram cobertos pelos implicantes primos essenciais
    implicantes_primos_essenc = {} #lista com o implicante primos essenciais e quais mintermos ele representa
    set_mintermos_cobertos = set()
    lista_implicantes_primos_essenciais = []

    for lista_minterms in implicantes_primos.values():
        lista_aux.extend(lista_minterms) #lista para guardar os mintermos temporariamente
    
    #conta o número de repetições do mintermo
    for i in lista_aux:
        cont = lista_aux.count(i)
        if cont == 1:
            lista_implicantes_primos_essenciais.append(i)

    for j in lista_implicantes_primos_essenciais:
        for chave in implicantes_primos:
            for implicante in implicantes_primos[chave]:
                if j == implicante:
                    implicantes_primos_essenc[chave] = []
                    implicantes_primos_essenc[chave].extend(implicantes_primos[chave])

    #checa se cobre todos os outros implicantes
    for mintermos in implicantes_primos_essenc.values():
        set_mintermos_cobertos.update(mintermos)
    
    for chave in implicantes_primos:
        for valor in implicantes_primos[chave]:
            if valor not in set_mintermos_cobertos:
                incobertos[chave] = implicantes_primos[chave]

    print(set_mintermos_cobertos)
    print(incobertos)
    print(implicantes_primos_essenc)
    #print(lista_implicantes_primos_essenciais)

    if incobertos: #chama o método de Petrick, mandar no mínimo, os implicantes primos essenciais e os incobertos
        termos_petrick(incobertos, implicantes_primos_essenc)
    else:
        print("Expressão booleana na forma reduzida:", boolean_expression_minimizer(implicantes_primos_essenc.keys())) #retorna os implicantes primos essenciais
