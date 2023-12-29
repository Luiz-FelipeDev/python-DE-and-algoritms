matriz = []
def cria_matriz(numero_de_linhas, numero_de_colunas):
    for i in range(numero_de_linhas):
        linha = []
        for j in range(numero_de_colunas):
            valor = int(input(f'Digite o valor do elemento [{i}][{j}]'))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def le_matriz():
    lin = int(input('Digite o número de linhas: '))
    col = int(input('Digite o número de colunas: '))
    m = cria_matriz(lin, col)
    return m

print(le_matriz())

[[0,0,0], 
 [0,0,0],
 [0,0,0]]
        

            