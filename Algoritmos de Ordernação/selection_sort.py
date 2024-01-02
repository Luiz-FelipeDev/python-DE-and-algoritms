lista_desordenada = [100, 23, 10, 78, -90]

class Ordernador:
    def section_sort(self, lista):
        fim = len(lista)
        
        for i in range(fim-1):
            # inicialmente, o menor elemento já visto é o i-ésimo
            posicao_do_minimo = i
            
            for j in (i+1 , fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j
                    lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
            return lista
        
o = Ordernador()
lista_ordenada = o.section_sort(lista=lista_desordenada)
print(lista_ordenada)