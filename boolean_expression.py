def canonical_boolean_expression(result_1: list, alphabet: list):
    """ Analisa o digito dentro da lista que contêm as listas com a entrada de cada linha"""
    boolean_expression = ''
    for linha in result_1:
            for indice, digito in enumerate(linha):
                alphabet[indice]
                if digito == '0':
                    boolean_expression += alphabet[indice] + "'"
                elif digito == '1':
                    boolean_expression += alphabet[indice]
            boolean_expression += ' + '
    
    print("Forma canônica da expressão booleana: ", boolean_expression[:-2])