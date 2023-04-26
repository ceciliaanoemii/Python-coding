import pandas as pd
import matplotlib.pyplot as plt #libreria de visualizacion de datos
import seaborn as sns #libreria de graficos estadisticos

df = pd.read_csv("archivos_problemas_graficos\\vasos.csv")

#creando el grafico
sns.lineplot(x="fecha",y="vasosQueTome",data=df)

#creando un punto en el momento que mas vasos tome
plt.plot("01-10",17,"o")

#mostrando el grafico
plt.show()