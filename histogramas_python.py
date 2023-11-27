import pandas as pd #comentario
import matplotlib.pyplot as plt

atletas = pd.read_csv(r'C:\Users\ilse-\PROGA\categorias_de_corredores.csv', sep=';',index_col=0)

atletas.info()

atletas.head()

plt.figure(1)
plt.hist(atletas['Tiempo'], 15, color="yellow", ec="black")
plt.title("Histograma Tiempo")
plt.savefig("Histograma.jpg")

#Para conocer la frecuencia de una variable es categorica
import seaborn as sns
plt.figure(2)
sns.countplot(x=atletas['Velocidad'], palette = 'ocean')
plt.savefig("Velocidades.jpg")

#Si queremos saber las velocidades en hombres y mujeres
plt.figure(3)
grafico3 = sns.countplot(x = 'Genero', hue = 'Velocidad', palette = 'hot_r', data = atletas)
grafico3.set(title = 'Velocidades por Género',
          xlabel = 'Género', ylabel = 'Total')
plt.title("Grafico de Barras Genero")
plt.savefig("Genero.jpg")
plt.show()