##################################################
# Cifra de césar.                                #   
# Código para apresentação de FMCC II - 2021.1   #
#                                                # 
# @Authors:                                      #                              
# Jhonnathas Swerley Farias dos Santos           #
# Vimerson Pedro Custodio Silva                  #
# Guilherme Henrique Pereira                     #
# Victor Hugo da Silva Rangel                    #
##################################################

## Know issues:
##  .Index out of range, com a letra t utilizando a chave 7



# Algoritmo trabalha com o alfabeto em maíusculo#
def encriptar (texto, chave):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    texto_limpo = texto.upper() ## mantém o texto em maísculo
    texto_encriptado = ""

    for e in texto_limpo:
        if e == "0" or e == "1" or e == "2" or e == "3" or e == "4" or e == "5" or e == "6" or e == "7" or e == "8" or e == "9": ##visando manter os numeros os mesmos
            texto_encriptado = texto_encriptado + e
        elif e == " ": ## para tratar os espaços no texto
            texto_encriptado = texto_encriptado + e
        else: 
            posicao = alfabeto.find(e)
            posicao += chave ## passo matemático
            if posicao > len(alfabeto):
                posicao = posicao - len(alfabeto)
            
            texto_encriptado = texto_encriptado + alfabeto[posicao]


    return texto_encriptado

def decriptar (texto, chave):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    texto_limpo = texto.upper() ## mantém o texto em maísculo
    texto_decriptado = ""

    for e in texto_limpo:
        if e == "0" or e == "1" or e == "2" or e == "3" or e == "4" or e == "5" or e == "6" or e == "7" or e == "8" or e == "9": ##visando manter os numeros os mesmos
            texto_decriptado = texto_decriptado + e
        elif e == " ": ## para tratar os espaços no texto
            texto_decriptado = texto_decriptado + e
        else:
            posicao = alfabeto.find(e)
            posicao -= chave ## passo matemático

            if posicao < 0:
                posicao = len(alfabeto) - abs(posicao)
            
            texto_decriptado = texto_decriptado + alfabeto[posicao]

    return texto_decriptado
