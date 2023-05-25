import numpy as np
import math

# CHALLENGE
# O resultado da função 'customArray' deve produzir um array Bidimensional parecido exemplo abaixo;
# A função também funciona com arrays maiores do que 5x5 sendo possível qualquer tamanho;
# Desde que seja um quadrado
#                   1 1 1 1 1
#                   1 0 0 0 1
#                   1 0 9 0 1
#                   1 0 0 0 1
#                   1 1 1 1 1

# Este foi um desafio proposto no video do freeCodeCamp https://www.youtube.com/watch?v=QUT1VHiLmmI
# e eu extendi ele pra fazer um pouco mais


def customArray(size) -> list:
    # define um array de linhas e colunas iguais (quadrado), composto de números '1' com a função especifica do numpy;

    # atribui mesmo valor para row e col
    row = col = size
    arr = np.ones((row, col), dtype=int)

    # define as bordas subtraindo 1 do tamanho das linhas;
    border = len(arr[1]) - 1

    # Define o centro do array dividindo seu tamanho total pela metade;
    half = math.floor(len(arr[1]) / 2)

    # Itera sobre as linhas a partir do indice 1 atribui o numero '0' até as bordas;
    for r in arr[1:border]:
        r[1:border] = [0]

    # define o meio das Linhas e Colunas
    # define o fim do slice para half + 1 para retornar o centro do array
    # Atribui a seção de slice para o numero '9'
    if not (row % 2 == 0):
        arr[half, half : half + 1] = [9]
        print(*arr, sep="\n")
    else:
        # sorcery, sorry im dead
        arr[half - 1 : half + 1, half - 1 : half + 1] = [9]

        # printa cada elemento do array em uma nova linha usando splat operator e separator
        print(*arr, sep="\n")

    return arr


# customArray(4)
customArray(5)
# customArray(7)
# customArray(10)
# customArray(20)
# customArray(25)
# to infinity
