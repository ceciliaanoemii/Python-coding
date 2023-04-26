import pandas as pd
import matplotlib.pyplot as plt #libreria de visualizacion de datos
import seaborn as sns #libreria de graficos estadisticos

df = pd.read_csv("archivos_problemas_graficos\\cecilia_ingresos.csv")

#creando el grafico
sns.barplot(x="fuente",y="ingresos",data=df)

#obteniendo el total de ingresos
total_ingresos = df['ingresos'].sum()

#mostrando el total
print(f"El total de ingresos es de: ${total_ingresos} pesos")

#mostrando el grafico
plt.show()