
nome_do_produto = str(input("Qual o nome do produto?:"))
qtde_vendida = int(input("Qual a quantidade vendida?:"))
vr_real = float(input("Qual o valor unitário em real:"))
taxa_euro = float(input("Qual o valor da taxa do euro:"))

vr_real = (qtde_vendida * vr_real)
print("Valor total da venda em reais:", vr_real)
vr_euro = (vr_real / taxa_euro)
print("Valor total da venda em euros", vr_euro)

from time import sleep

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
l.reverse()
for i in l:
        sleep(3)
print ("Fim do programa :)")