# fazer um programa que recebe um número de 1 a 26,
# e printa em série as letras correspondentes a quantidade do número selecionado.


# ATRIBUIÇÃO DE VARIÁVEIS
letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabeto = dict()
aa = 0
# ------------------------------------------------------------ #
for a in range(len(letras)):                                   # Adiciona uma chave no dicionário para cada letra da lista 'letras';
    if a == 0:
        aa = a + 1
    alfabeto[aa] = letras[a]                                   # A cada laço, é adicionado uma letra do alfabeto para uma chave int crescente:
    aa += 1


def um_a_vinteseis():                                          # Definição de uma função para retornar uma Booleana;
    return 1 <= valor <= 26

while True:
# ENTRADA DE VALOR
    while True:
        try:
            valor = int(input('Digite um número de 1 a 26 para visualizar o alfabeto: '))
            um_a_vinteseis()
            break
        except:
            print('ERRO. Digite um valor numérico de 1 a 26.')
            
# SAÍDA DE VALOR
    for x in range(1, valor + 1):
        print(f'{alfabeto[x]}', end=', ')
    print()

    resposta = input('Quer tentar novamente? [S/N]:')
    if resposta in 'Nn':
        break

print('Ok! Até breve.')
