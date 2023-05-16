print('modulo [1] importado')

def calcula_imc(peso, altura):
    print('parametro peso: ', peso.replace(',', '.'))
    print('parametro altura: ', altura.replace(',', '.'))
    imc = float(peso) / float(altura) ** 2
    return imc


def classificacao_imc(indice):
    if indice < 18.5:
        return f'STATUS: Baixo peso'
    elif indice < 25:
        return 'STATUS: Peso adequado'
    elif indice < 30:
        return 'STATUS: SobrePeso'
    else:
        return 'STATUS: Obeso'