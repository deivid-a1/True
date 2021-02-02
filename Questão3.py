import pandas as pd
import glob

df = pd.concat(map(pd.read_csv, glob.glob('prevista\*')))
df = df.drop(columns=['subBacia'])
df = df.drop(columns=['lat'])
df = df.drop(columns=['long'])


dfGrande = df.query('bacia == "Grande"')
dfGrande = dfGrande.describe().mean()
print("Bacia Grande: ")
print(dfGrande)

dfIguacu = df.query('bacia == "Iguacu"')
dfIguacu = dfIguacu.describe().mean()
print("Bacia Iguacu: ")
print(dfIguacu)

dfItaipu = df.query('bacia == "Itaipu"')
dfItaipu = dfItaipu.describe().mean()
print("Bacia Itaipu: ")
print(dfItaipu)

dfMadeira = df.query('bacia == "Madeira"')
dfMadeira = dfMadeira.describe().mean()
print("Bacia Madeira: ")
print(dfMadeira)

dfOutrasSul = df.query('bacia == "OutrasSul"')
dfOutrasSul = dfOutrasSul.describe().mean()
print("Bacia OutrasSul: ")
print(dfOutrasSul)

dfParana = df.query('bacia == "Parana"')
dfParana = dfParana.describe().mean()
print("Bacia Parana: ")
print(dfParana)

dfParanaiba = df.query('bacia == "Paranaiba"')
dfParanaiba = dfParanaiba.describe().mean()
print("Bacia Paranaiba: ")
print(dfParanaiba)

dfParanapanema = df.query('bacia == "Paranapanema"')
dfParanapanema = dfParanapanema.describe().mean()
print("Bacia Paranapanema: ")
print(dfParanapanema)

dfSaoFrancisco = df.query('bacia == "SaoFrancisco"')
dfSaoFrancisco = dfSaoFrancisco.describe().mean()
print("Bacia SaoFrancisco: ")
print(dfSaoFrancisco)

dfTiete = df.query('bacia == "Tiete"')
dfTiete = dfTiete.describe().mean()
print("Bacia SaoFrancisco: ")
print(dfTiete)

dfTocantins = df.query('bacia == "Tocantins"')
dfTocantins = dfTocantins.describe().mean()
print("Bacia Tocantins: ")
print(dfTocantins)

dfUruguai = df.query('bacia == "Uruguai"')
dfUruguai = dfUruguai.describe().mean()
print("Bacia Uruguai: ")
print(dfUruguai)