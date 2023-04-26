import pandas as pd
import matplotlib.pyplot as plt #libreria de visualizacion de datos
import seaborn as sns #libreria de graficos estadisticos

df = pd.read_csv("archivos_problemas_graficos\\bigotes.csv")

#creando el grafico
sns.boxplot(x="categoria",y="valor",data=df)

#mostrando el grafico
plt.show()