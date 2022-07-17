def canonical_boolean_expression(result_1: list, letras: list):
    """ Analisa se o bit é 0 ou 1 para escrever a expressão booleana"""
    boolean_expression = ''
    for linha in result_1:
            for indice, digito in enumerate(linha):
                """ alphabet[indice] """
                if digito == '0':
                    boolean_expression += letras[indice] + "'"
                elif digito == '1':
                    boolean_expression += letras[indice]
            boolean_expression += ' + '
    
    print("\nForma canônica da expressão booleana: ", boolean_expression[:-3], "\n")


def boolean_expression_minimizer(mintermos_essenciais: set, letras: list):
    boolean_expression = ''
    for minterm in mintermos_essenciais:
        for indice, bit in enumerate(minterm):
            if bit == '0':
                boolean_expression += letras[indice] + "'"
            elif bit == '1':
                boolean_expression += letras[indice]
        boolean_expression += " + "
    
    return boolean_expression[:-3]