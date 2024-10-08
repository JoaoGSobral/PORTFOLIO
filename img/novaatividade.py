# Aluno: João Gabriel de Sobral Nunes
#MB1

ltchocolate=float(input("quantos litros de chocolate foram vendido: "))
estoq_chocolate=float(input("quanto litros tem no estoque: "))

ltbaunilha=float(input("quantos litros de baunilha foram vendidos: "))
estoq_baunilha=float(input("quanto litros tem no estoque: "))

ltflocos=float(input("quantos litros de flocos foram vendidos: "))
estoq_flocos=float(input("quanto litros tem no estoque: "))

ltcoco=float(input("quantos litros de coco foram vendido: "))
estoq_coco=float(input("quanto litros tem no estoque: "))

lttapioca=float(input("quantos litros de tapioca foram vendidos: "))
estoq_tapioca=float(input("quanto litros tem no estoque: "))

ltmenta=float(input("quantos litros de mentas foram vendidos: "))
estoq_menta=float(input("quanto litros tem no estoque: "))

print ( f" o total de litros vendidos são {ltchocolate+ ltbaunilha+ ltcoco+ ltflocos+ lttapioca+ ltmenta}")
print ( f" o total de litos no estoque é {estoq_baunilha+ estoq_chocolate+ estoq_coco+ estoq_flocos+ estoq_tapioca+ estoq_menta}")
print ( f" a media de litos vendidos foi {ltflocos+ ltbaunilha+ ltchocolate+ ltmenta+ ltcoco+ lttapioca/6}")
print ( f" a media de litros no estoque é {estoq_baunilha+ estoq_chocolate+ estoq_coco+ estoq_flocos+ estoq_menta+ estoq_tapioca/6}")

sabor = ltchocolate, ltbaunilha, ltflocos, ltmenta, lttapioca, ltcoco
maiorvalor = max(sabor)
if ltbaunilha == maiorvalor:
    print (f"O sabor mais vendido foi baunilha, com {maiorvalor} litros vendidos")
elif ltchocolate == maiorvalor:
    print (f"O sabor mais vendido foi o de chocolate, com {maiorvalor} litros vendidos")
elif ltcoco == maiorvalor:
    print (f"O sabor mais vendido foi o de coco, com {maiorvalor} litros vendidos")
elif ltmenta == maiorvalor:
    print (f"O sabor mais vendido foi o de menta, com {maiorvalor} litros vendidos")
elif ltcoco == maiorvalor:
    print (f"O sabor mais vendido foi o de tapioca, com {maiorvalor} litros vendidos")
elif ltmenta == maiorvalor:
    print (f"O sabor mais vendido foi o de menta, com {maiorvalor} litros vendidos")
elif ltflocos == maiorvalor:
    print (f"O sabor mais vendido foi de flocos,comm {maiorvalor} litros vendidos  ")

sabores_estoque = estoq_baunilha, estoq_chocolate, estoq_coco, estoq_flocos, estoq_menta, estoq_tapioca
maiorvalorestoque = max(sabores_estoque)
if estoq_baunilha == maiorvalorestoque:
    print (f"O sabor que tem maior quantidade nos estoque é o de baunilha com {maiorvalorestoque} unidades ")
if estoq_chocolate == maiorvalorestoque:
    print (f"O sabor que tem maior quantidade nos estoque é o de chocolate com {maiorvalorestoque} unidades ")
if estoq_coco == maiorvalorestoque:
    print (f"O sabor que tem maior quantidade nos estoque é o de coco com {maiorvalorestoque} unidades ")
if estoq_flocos == maiorvalorestoque:
    print (f"O sabor que tem maior quantidade nos estoque é o de flocos com {maiorvalorestoque} unidades ")
if estoq_tapioca == maiorvalorestoque:
    print (f"O sabor que tem maior quantidade nos estoque é o de tapioca com {maiorvalorestoque} unidades ")
if estoq_menta == maiorvalorestoque:
    print (f"O sabor que tem maior quantidade nos estoque é o de menta com {maiorvalorestoque} unidades ")
    
total_litro = f"{ltmenta+ ltbaunilha+ ltchocolate+ ltcoco+ ltflocos+ lttapioca}"
total_estoque = f"{estoq_baunilha+ estoq_chocolate+ estoq_coco+ estoq_flocos+ estoq_menta+ estoq_tapioca}"
if total_litro> total_estoque:
    print ("A quantidade de litros vendidos é maior do que tem no estoque ")
else:
    print("A quantidade do que tem no estoque é maior do que tem a quantidade de litros vendidos")
    
    
print (f" o valor que você arrecadou foi de {ltchocolate* 50+ ltbaunilha* 50+ ltcoco* 50+ ltflocos* 50+ ltmenta}")
print (f" o valor que a empresa tem no estoque é {estoq_baunilha* 20+ estoq_chocolate* 20+ estoq_coco* 20+ estoq_flocos* 20+ estoq_menta* 20+estoq_tapioca*20}")
    


