# visualização dos dados em python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

title = "Gráfico de Barras"
axisx = "Eixo X"
axisy = "Eixo Y"

# Título
plt.title(title)

# Eixos
plt.xlabel(axisx)
plt.ylabel(axisy)

# grafico de linhas
plt.bar(x, y)
plt.show()
