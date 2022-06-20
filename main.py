def validacao(numero): # verifica se o usuário digitou algum número diferente de 0 e 1
    if numero != '0' and numero != '1':
        return True

def boolean_expression_generator():
    variable_value = {'A': [0, 0, 0, 0, 1, 1, 1, 1],
                      'B': [0, 0, 1, 1, 0, 0, 1, 1],
                      'C': [0, 1, 0, 1, 0, 1, 0, 1]}

    output_values = [] #lista para armazenar os valores de saída inseridos pelo usuário
    linhas = []
    boolean_enpression = ''

    print("=============================")
    print("   TABELA VERDADE")
    print("  A  |  B  |  C  |  S")
    # estrutura de repetição que vai servir para imprimir a tabela
    for j in range(8): #serve para controlar os índices da listas dentro do dicionário
        aux = [] # variável usada para armazenar o valor de cada uma das 3 variáveis de entrada
        for i in variable_value:
            print(' ', variable_value[i][j], end='  |')
            aux.append(variable_value[i][j])
        
        output_values.append(input("  "))
        
        if validacao(output_values[-1]):
            print("Entrada inválido!")
            break
        
        if output_values[-1] == '1':
            linhas.append(aux) #armazena as linhas em que a saída foi 1

    # Analisa o elemento dentro da lista que contem as listas com a entrada de cada linha
    if len(linhas) == 0:
        print("\nNão foi possível gerar uma expressão booleana")
    else:
        for lista in linhas:
            for elemento in range(3):
                if lista[elemento] == 0: # vê se o elemento é 0, se for ele checa a posição da matriz em que o 0 está
                    if elemento == 0: 
                        boolean_enpression += "A'"
                    elif elemento == 1:
                        boolean_enpression += "B'"
                    elif elemento == 2:
                        boolean_enpression += "C'"
                else: # vê se o elemento é 1, se for ele checa a posição da matriz em que o 1 está
                    if elemento == 0:
                        boolean_enpression += "A"
                    elif elemento == 1:
                        boolean_enpression += "B"
                    elif elemento == 2:
                        boolean_enpression += "C"
            boolean_enpression += " + "

        print("\nBoolean expression:", boolean_enpression[:-2]) # remove os 2 últimos caracteres da string

boolean_expression_generator()