
matriz = [
    [1, 2, 3],
    [4, 5 ,6],
    [9, 8, 9],  
]

list_diagonal_one = []

contador_linha = 0
contador_coluna = 0
def diagonalDifference(matriz):
    for i, line in matriz:
        for k, element in line:
            element[i][k] == matriz[contador_linha][contador_coluna]
            list_diagonal_one.append(element)
               


print(diagonalDifference(matriz))
print(list_diagonal_one)