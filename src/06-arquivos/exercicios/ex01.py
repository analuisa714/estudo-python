""" Exercício 01 - tupla de alunos, com dicionario """

def carregar_dados_alunos(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        lista = []
        for linha in arquivo:
            dados = linha.split(sep=',')
            dicionario = {
                'prontuario': dados[0],
                'nome': dados[1],
                'email': dados[2]
            }
            lista.append(dicionario)
    tupla = (lista)
    return tupla
   
tupla_alunos = carregar_dados_alunos('src/06-arquivos/exercicios/dados_01.txt')

for aluno in tupla_alunos:
    print('{')
    for key, value in aluno.items():
        print(f'    {key} : {value}')
    print('}')