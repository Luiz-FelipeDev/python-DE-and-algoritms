matriz = []

def cria_matriz(numero_de_linhas, numero_de_colunas):
    result_sum = 0
    for i in range(numero_de_linhas):
        linha = []
        for j in range(numero_de_colunas):
            valor = int(input(f'Digite o valor do elemento [{i}][{j}]'))
            if i == j:
                result_sum += valor
            linha.append(valor)
        matriz.append(linha)
    return matriz, result_sum

def le_matriz():
    lin = int(input('Digite o número de linhas: '))
    col = int(input('Digite o número de colunas: '))
    m = cria_matriz(lin, col)
    return m
                
                
'''                
def soma_diagonal_matriz(i, j, valor):
    result_sum = 0

    if i == j:
        result_sum += valor
    
'''
    

#a posição da linha tem que ser igual a posição da coluna
# a etapa agora é criar uma function e aplicar ao codigo
print(le_matriz())

[[0,0,0], 
 [0,0,0],
 [0,0,0]]
        