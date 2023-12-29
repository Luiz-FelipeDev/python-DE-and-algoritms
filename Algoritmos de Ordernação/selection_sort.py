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