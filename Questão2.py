import glob
import pandas as pd
#eu busco os dados novamente que são da true e ONS
df1 = pd.concat(map(pd.read_csv, glob.glob('observada\observadaONS*')))
df2 = pd.concat(map(pd.read_csv, glob.glob('observada\observadaTrue*')))

#separo em 2 vetores com os avg da true(df2) e da ons(df1)
df1 = df1._get_column_array(5)
df2 = df2._get_column_array(5)


#aqui eu calculo neste laço a relação de cada dado, já que eles estão organizados se parar pra analizar o csv

soma = 0
listaOns = []
flag = 1
i = 1
for i in range(2268+1):
    soma = soma + df1[i-1]
    if i == 84 * flag:
        flag = flag + 1
        listaOns.append(soma)
        soma = 0

soma = 0
listaTrue = []
flag = 1
i = 1
for i in range(2268+1):#aqui eu crio a lista da True diaria
    soma = soma + df2[i-1]
    if i == 84 * flag:
        flag = flag + 1
        listaTrue.append(soma)
        soma = 0

listaFinal = []
i = 0
for i in range(27):#aqui eu crio a lista da Ons diaria
    a = listaTrue[i]-listaOns[i]
    if a < 0:
        a = a*-1
        listaFinal.append(a)
    else: listaFinal.append(a)

for i in range(27):#como alguns valores estão zerando, eu coloquei um numero proximo a zero para poder dividi-lo.
    if listaFinal[i] == 0:
        listaFinal[i]  = 0.0001

for i in range(len(listaFinal)):#como é pedido o valor relativo a Ons
    print("Valor absoluto dia {}: {} XXX Valor relativo: {}".format(i+1, listaFinal[i], listaFinal[i]/listaOns[i]))
