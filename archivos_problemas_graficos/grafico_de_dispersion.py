import pandas as pd
import matplotlib.pyplot as plt #libreria de visualizacion de datos
import seaborn as sns #libreria de graficos estadisticos

df = pd.read_csv("archivos_problemas_graficos\\dispersion.csv")

#creando el grafico
sns.scatterplot(x="tiempo",y="dinero",data=df)

#mostrando el grafico
plt.show()