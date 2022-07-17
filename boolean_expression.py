def canonical_boolean_expression(result_1: list, letras: list):
    """ Analisa o digito dentro da lista que contêm as listas com a entrada de cada linha"""
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