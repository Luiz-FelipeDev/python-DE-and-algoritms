from collections import Counter

#Primeiro passarei o texto como argumento 
#iterar o texto e econtrar a frequencia númerica inteira de cada palavra 
# encontrar o valor total para realizar a razão 

texto_1 = """
Para começar a fazer vendas online, uma empresa que fabrica adesivos criou uma página para pré cadastro de cartão de crédito que contém campos como nome, idade, endereço, CPF entre outros.

O problema é que alguns cadastros não possuem um formato de CPF válido, isso porque o campo não possui nenhuma validação. Ou seja, o campo está aceitando não só números como letras e outros tipos de caractere.

O que vamos fazer é encontrar uma maneira de ajudar o usuário de forma mais clara possível a preencher o cadastro e garantir a validação no front-end antes que os dados sejam enviados para o back-end.



Como podemos notar não temos nenhuma validação, então fica confuso se devemos ou não colocar ponto ou traço no CPF e pode acontecer do usuário colocar outros caracteres no campo sem querer.

Para isso evitar que isso ocorra vamos usar o atributo pattern do HTML5 que nos permite fazer uso das famosas expressões regulares que nada mais são que padrões utilizados para selecionar caracteres em uma string.

Na nossa verificação vamos usar a lista [0-9], esse padrão indica que queremos os números de 0 até 9 e o intervalo {11}, indicando que temos que ter um número de 11 dígitos no nosso campo.

Com a adição do pattern nosso campo de CPF ficou da seguinte maneira:



Com a ajuda do pattern e das expressões regulares conseguimos resolver uma parte da tarefa, agora o que precisamos fazer encontrar uma maneira de formatar o CPF no padrão que precisamos enviar ao back-end.

Mais um pouco de Regex
Para começar vamos criar uma função que vai ser responsável por formatar o CPF. Dentro dessa função vamos ter as variáveis :

elementoAlvo: responsável pelo parâmetro que vai ser passado na função
cpfAtual: responsável por capturar os números do CPF digitados
cpfAtualizado: responsável por receber o CPF formatado.
"""

    # Entregando a frequencia de acordo com o caracter em pontos percentuais
    # Entregando os 10 com maior frequencia:

def frequencia_de_letras_no_texto(texto):
    aparicoes = Counter(texto.lower())
    total = 0
    lista_de_caracteres = [(caracter, frequencia) for caracter, frequencia in aparicoes.items()]
    
    mapa_caracteres = Counter(lista_de_caracteres)
    
    for caracter in mapa_caracteres.values():
        total += caracter
    
    caracteres_mais_frequentes  = mapa_caracteres.most_common(10)
    for caracter, valor in caracteres_mais_frequentes:
        percentual = (valor/total) * 100
        
        print("Caracter {} => {:.2f}%".format(caracter, percentual))
        

frequencia_de_letras_no_texto(texto_1)