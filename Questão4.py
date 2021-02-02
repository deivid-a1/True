import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot
import Questão3
import Questão1
#grafico observada
meses = ['Gra','Ig','It','Mad','OSul','Pr', "Paran", "Paranam", "SaoFr", "Tie", "Toc", "Ur"]
valores = [Questão1.dfGrandeTrue.mean(),Questão1.dfIguacuTrue.mean(), 0,Questão1.dfMadeiraTrue.mean(),Questão1.dfOSulTrue.mean(), Questão1.dfParanaTrue.mean(),
Questão1.dfParanaibaTrue.mean(), Questão1.dfParanapanemaTrue.mean(),Questão1.dfSaoFranciscoTrue.mean(),Questão1.dfTieteTrue.mean(),Questão1.dfTocantinsTrue.mean(),Questão1.dfUruguaiTrue.mean()]

matplotlib.pyplot.plot(meses, valores)
matplotlib.pyplot.show()

#gráfico prevista
meses = ['Gra','Ig','It','Mad','OSul','Pr', "Paran", "Paranam", "SaoFr", "Tie", "Toc", "Ur"]
valores = [Questão3.dfGrande.mean(),Questão3.dfIguacu.mean(), Questão3.dfItaipu.mean(), Questão3.dfMadeira.mean(),Questão3.dfOutrasSul.mean(), Questão3.dfParana.mean(),
Questão3.dfParanaiba.mean(), Questão3.dfParanapanema.mean(),Questão3.dfSaoFrancisco.mean(),Questão3.dfTiete.mean(),Questão3.dfTocantins.mean(),Questão3.dfUruguai.mean()]

matplotlib.pyplot.plot(meses, valores)
matplotlib.pyplot.show()