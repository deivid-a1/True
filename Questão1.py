#é usado as bibliotecas glob e pandas para manipulaçãdo de uma dataframe
import glob
import pandas as pd

#A ideia é pegar de todos os CSVs todos os dados e montar a dataframe.
df = pd.concat(map(pd.read_csv, glob.glob('observada\observada*'))) #aqui eu crio a grande dataframe e a partir dela eu vou retirar todos os dados de cada bacia, como pedido
#na questão 1.

dfGrande = df #Como dito, eu duplico a dataframe original e manipulo o nome objeto "dfGrande" de forma livre, sem se preocupar em perder todos os dados.
dfGrande = dfGrande.query('bacia == "Grande"') #aqui é feito a busca pela coluna bacia que possui os dados "Grande".
dfGrandeOns = dfGrande.query('fonte == "ons"') #aqui é filtrado os dados da ONS em relação a bacia Grande.
dfGrandeTrue = dfGrande.query('fonte == True')#aqui é filtrado os dados da True em relação a bacia Grande.
dfGrande = dfGrande._get_column_array(5)#Criada uma lista que guarda somente os dados da bacia Grande.
dfGrandeTrue = dfGrandeTrue._get_column_array(5) #aqui é retirado do dataframe e colocado em uma lista o sexto índice das colunas, que é o que nos interessa, a média de cada dia da true.
dfGrandeOns = dfGrandeOns._get_column_array(5) #aqui é retirado do dataframe e colocado em uma lista o sexto índice das colunas, que é o que nos interessa, a média de cada dia da ONS.
print("ONS>Grande: {} XXX True>Grande: {}".format(dfGrandeTrue.mean(), dfGrandeOns.mean()))# aqui eu printo a média dos 2 arrays de dados coletados acima

#Daqui em diante, é feito os mesmos passos para cada bacia.
dfIguacu = df
dfIguacu = dfIguacu.query('bacia == "Iguacu"')
dfIguacuOns = dfIguacu.query('fonte == "ons"')
dfIguacuTrue = dfIguacu.query('fonte == True')
dfIguacu = dfIguacu._get_column_array(5)
dfIguacuTrue = dfIguacuTrue._get_column_array(5)
dfIguacuOns = dfIguacuOns._get_column_array(5)
print("ONS>Iguacu: {} XXX True>Iguacu: {}".format(dfIguacuTrue.mean(), dfIguacuOns.mean()))

dfMadeira = df
dfMadeira = dfMadeira.query('bacia == "Madeira"')
dfMadeiraOns = dfMadeira.query('fonte == "ons"')
dfMadeiraTrue = dfMadeira.query('fonte == True')
dfMadeira = dfMadeira._get_column_array(5)
dfMadeiraTrue = dfMadeiraTrue._get_column_array(5)
dfMadeiraOns = dfMadeiraOns._get_column_array(5)
print("ONS>Madeira: {} XXX True>Madeira: {}".format(dfMadeiraTrue.mean(), dfMadeiraOns.mean()))

dfOSul = df
dfOSul = dfOSul.query('bacia == "OSul"')
dfOSulOns = dfOSul.query('fonte == "ons"')
dfOSulTrue = dfOSul.query('fonte == True')
dfOSul = dfOSul._get_column_array(5)
dfOSulTrue = dfOSulTrue._get_column_array(5)
dfOSulOns = dfOSulOns._get_column_array(5)
print("ONS>OSul: {} XXX True>OSul: {}".format(dfOSulTrue.mean(), dfOSulOns.mean()))

dfParana = df
dfParana = dfParana.query('bacia == "Parana"')
dfParanaOns = dfParana.query('fonte == "ons"')
dfParanaTrue = dfParana.query('fonte == True')
dfParana = dfParana._get_column_array(5)
dfParanaTrue = dfParanaTrue._get_column_array(5)
dfParanaOns = dfParanaOns._get_column_array(5)
print("ONS>Parana: {} XXX True>Parana: {}".format(dfParanaTrue.mean(), dfParanaOns.mean()))

dfParanaiba = df
dfParanaiba = dfParanaiba.query('bacia == "Paranaiba"')
dfParanaibaOns = dfParanaiba.query('fonte == "ons"')
dfParanaibaTrue = dfParanaiba.query('fonte == True')
dfParanaiba = dfParanaiba._get_column_array(5)
dfParanaibaTrue = dfParanaibaTrue._get_column_array(5)
dfParanaibaOns = dfParanaibaOns._get_column_array(5)
print("ONS>Paranaiba: {} XXX True>Paranaiba: {}".format(dfParanaibaTrue.mean(), dfParanaibaOns.mean()))

dfParanapanema = df
dfParanapanema = dfParanapanema.query('bacia == "Paranapanema"')
dfParanapanemaOns = dfParanapanema.query('fonte == "ons"')
dfParanapanemaTrue = dfParanapanema.query('fonte == True')
dfParanapanema = dfParanapanema._get_column_array(5)
dfParanapanemaTrue = dfParanapanemaTrue._get_column_array(5)
dfParanapanemaOns = dfParanapanemaOns._get_column_array(5)
print("ONS>Paranapanema: {} XXX True>Paranapanema: {}".format(dfParanapanemaTrue.mean(), dfParanapanemaOns.mean()))

dfSaoFrancisco = df
dfSaoFrancisco = dfSaoFrancisco.query('bacia == "SaoFrancisco"')
dfSaoFranciscoOns = dfSaoFrancisco.query('fonte == "ons"')
dfSaoFranciscoTrue = dfSaoFrancisco.query('fonte == True')
dfSaoFrancisco = dfSaoFrancisco._get_column_array(5)
dfSaoFranciscoTrue = dfSaoFranciscoTrue._get_column_array(5)
dfSaoFranciscoOns = dfSaoFranciscoOns._get_column_array(5)
print("ONS>SaoFrancisco: {} XXX True>SaoFrancisco: {}".format(dfSaoFranciscoTrue.mean(), dfSaoFranciscoOns.mean()))

dfTiete = df
dfTiete = dfTiete.query('bacia == "Tiete"')
dfTieteOns = dfTiete.query('fonte == "ons"')
dfTieteTrue = dfTiete.query('fonte == True')
dfTiete = dfTiete._get_column_array(5)
dfTieteTrue = dfTieteTrue._get_column_array(5)
dfTieteOns = dfTieteOns._get_column_array(5)
print("ONS>Tiete: {} XXX True>Tiete: {}".format(dfTieteTrue.mean(), dfTieteOns.mean()))

dfTocantins = df
dfTocantins = dfTocantins.query('bacia == "Tocantins"')
dfTocantinsOns = dfTocantins.query('fonte == "ons"')
dfTocantinsTrue = dfTocantins.query('fonte == True')
dfTocantinsTrue = dfTocantinsTrue._get_column_array(5)
dfTocantinsOns = dfTocantinsOns._get_column_array(5)
print("ONS>Tocantins: {} XXX True>Tocantins: {}".format(dfTocantinsTrue.mean(), dfTocantinsOns.mean()))

dfUruguai = df
dfUruguai = dfUruguai.query('bacia == "Uruguai"')
dfUruguaiOns = dfUruguai.query('fonte == "ons"')
dfUruguaiTrue = dfUruguai.query('fonte == True')
dfUruguaiTrue = dfUruguaiTrue._get_column_array(5)
dfUruguaiOns = dfUruguaiOns._get_column_array(5)
print("ONS>Uruguai: {} XXX True>Uruguai: {}".format(dfUruguaiTrue.mean(), dfUruguaiOns.mean()))