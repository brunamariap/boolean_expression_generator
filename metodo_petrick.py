def termos_petrick(implicantes_primos_incobertos: dict, implicantes_primos_essenciais: dict):
    termos = {}
    chaves = [x for x in implicantes_primos_incobertos]
    for i in range(len(chaves)):
        termos[f'P{i}'] = str(chaves[i])
    print(termos)