import os
from boolean_expression_simplified import *
from boolean_expression import canonical_boolean_expression, boolean_expression_minimizer


def validacao(bit: str):  # verifica se o usuário digitou algum número diferente de 0 e 1
    if bit != '0' and bit != '1':
        return True


def truth_table_input():
    #os.system("cls")
    num_variable = int(input('Digite o total de variáveis da tabela verdade: '))

    if num_variable < 2 or num_variable > 4:
        print('Não é possível gerar uma tabela verdade')

    else:
        letras = ['A', 'B', 'C', 'D']

        truth_table_lines = []
        output_values = [] # lista para armazenar os valores de saída inseridos pelo usuário
        result_1 = [] # matriz para armazenar a lista de cada linha que resulta em 1
        valid = True
        """ minterms = [] """

        #convertendo valores decimais para binário, pois os valores de entrada da linha correspodem ao número da linha em binário
        for num_linha in range(2 ** num_variable):
            binario = str(bin(num_linha))
            entrada_linha = '' # números de entrada de cada variável na linha

            if len(binario[2:]) < num_variable:
                entrada_linha = '0' * (num_variable - len(binario[2:]))
                entrada_linha += binario[2:]
                binario = entrada_linha
                truth_table_lines.append(binario) # lista para armazenar os valores decimais convertidos para binário
            else:
        
                truth_table_lines.append(binario[2:])
        
        print("=============================")
        print("   TABELA VERDADE")
        for j in range(num_variable):
            print(' ', letras[j], end='  |')
            if j == num_variable - 1:
                print('  S',)

        for linhas in truth_table_lines:
            for digito in linhas:
                print(' ', digito, end='  |')

            output_values.append(input("  "))

            if validacao(output_values[-1]):
                print("Entrada inválida!")
                valid = False
                break

            if output_values[-1] == '1':
                result_1.append(linhas)  # armazena as linhas em que a saída foi 1

        if len(result_1) == 0 or valid == False:
            print("\nNão foi possível gerar uma expressão booleana")
        else:
            canonical_boolean_expression(result_1, letras)
            grupos = separar_minterms(result_1)
            implicantes_primos = implicantes_reduzidos(grupos)
            mintermos_essenciais = primos_essenciais(implicantes_primos)