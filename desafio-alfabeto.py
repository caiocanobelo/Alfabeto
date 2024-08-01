# fazer um programa que recebe um número de 1 a 26,
# e printa em série as letras correspondentes a quantidade do número selecionado.


# ATRIBUIÇÃO DE VARIÁVEIS
letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabeto = dict()
aa = 0
# ------------------------------------------------------------ #
for a in range(len(letras)):
    if a == 0:
        aa = a + 1
    alfabeto[aa] = letras[a]
    aa += 1

# print(alfabeto)            # print de teste


def um_a_vinteseis():
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

    '''for b in range(0, valor):'''

    for x in range(1, valor + 1):
        print(f'{alfabeto[x]}', end=', ')
    print()

    resposta = input('Quer tentar novamente? [S/N]:')
    if resposta in 'Nn':
        break

print('Ok! Até breve.')