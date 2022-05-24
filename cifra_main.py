##################################################
# Cifra de césar.                                #   
# Código para apresentação de FMCC II - 2021.1   #
#                                                # 
# @Author:                                       #
# Victor Hugo da Silva Rangel                    #
##################################################

from cifra_funcoes import encriptar
from cifra_funcoes import decriptar


print ("\n")
print("==============================")
print("-- Criptografia de cesar -- \n")

texto = input("Digite o texto que deseja encriptar ou descriptar: ")

chave = int(input("Digite a chave privada, para encriptar ou descriptografar (entre 0 e 26): "))

while chave:
    if chave > 26:
        chave = int(input("Digite um valor menor do que 26 "))
    else: 
        break


operacao = int(input("Deseja criptografar? Digite 0 \nDeseja descriptografar? Digite 1  "))

if operacao == 0 :
    print(encriptar(texto,chave))

elif operacao == 1:
    print(decriptar(texto,chave))

