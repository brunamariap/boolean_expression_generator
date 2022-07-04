def validacao(numero):  # verifica se o usuário digitou algum número diferente de 0 e 1
    if numero != '0' and numero != '1':
        return True


def boolean_expression_generator():
    variable_value = {'A': [0, 0, 0, 0, 1, 1, 1, 1],
                      'B': [0, 0, 1, 1, 0, 0, 1, 1],
                      'C': [0, 1, 0, 1, 0, 1, 0, 1]}

    output_values = []  # lista para armazenar os valores de saída inseridos pelo usuário
    result_1 = []  # matriz para armazenar a lista de cada linha que resulta em 1

    boolean_enpression = ''

    valid = True

    print("=============================")
    print("   TABELA VERDADE")
    print("  A  |  B  |  C  |  S")
    # estrutura de repetição que vai servir para imprimir a tabela
    for j in range(8):  # serve para controlar os índices da listas dentro do dicionário
        aux = []  # variável usada para armazenar o valor de cada uma das 3 variáveis de entrada
        for i in variable_value:
            print(' ', variable_value[i][j], end='  |')
            aux.append(variable_value[i][j])

        output_values.append(input("  "))

        # verifica se o número de saída foi 0 ou 1
        if validacao(output_values[-1]):
            print("Entrada inválida!")
            valid = False
            break

        if output_values[-1] == '1':
            result_1.append(aux)  # armazena as linhas em que a saída foi 1

    # Analisa o elemento dentro da lista que contêm as listas com a entrada de cada linha
    if len(result_1) == 0 or valid == False:
        print("\nNão foi possível gerar uma expressão booleana")
    else:
        for lista in result_1:
            for elemento in range(3):
                # vê se o elemento é 0, se for ele checa a posição da matriz em que o 0 está
                if lista[elemento] == 0:
                    if elemento == 0:
                        boolean_enpression += "(A'"
                    elif elemento == 1:
                        boolean_enpression += "B'"
                    elif elemento == 2:
                        boolean_enpression += "C')"
                else:  # vê se o elemento é 1, se for ele checa a posição da matriz em que o 1 está
                    if elemento == 0:
                        boolean_enpression += "(A"
                    elif elemento == 1:
                        boolean_enpression += "B"
                    elif elemento == 2:
                        boolean_enpression += "C)"
            boolean_enpression += "+"

        # remove os 2 últimos caracteres da string
        print("\nBoolean expression:", boolean_enpression[:-2])


boolean_expression_generator()
