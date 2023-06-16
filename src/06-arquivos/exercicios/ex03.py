""" Exercício 03 - dicionário dinâmico """


def buscando_dados(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        lista = []
        lista_chaves = []
        valores = ''

        for linha in arquivo:
            lista.append(linha)
        lista_chaves = lista[1].strip().split(sep=',')
        valores = lista[0]

        return lista_chaves, valores


chaves, dados = buscando_dados('src/06-arquivos/exercicios/dados_03.txt')


def linha_para_dict(chaves, dados):
    dados = dados.strip().split(sep=',')

    dicionario = {}

    for i in range(len(chaves)):
        dicionario[chaves[i]] = dados[i]

    return dicionario


item = linha_para_dict(chaves, dados)

print('{')
for key, value in item.items():
    print(f"    '{key}' : '{value}'")
print('}')
