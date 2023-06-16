""" Exercício 02 - tupla de projetos, com dicionario """

def carregar_dados_projetos (nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        lista = []
        for linha in arquivo:
            dados = linha.split(sep=',')

            dados[0] = int(dados[0])
            
            dicionario = {
                'codigo': dados[0],
                'titulo': dados[1],
                'responsavel': dados[2]
            }
            lista.append(dicionario)
    tupla = (lista)
    return tupla
   
tupla_projetos = carregar_dados_projetos('src/06-arquivos/exercicios/dados_02.txt')

for projeto in tupla_projetos:
    print('{')
    for key, value in projeto.items():
        print(f'    {key} : {value}')
    print('}')