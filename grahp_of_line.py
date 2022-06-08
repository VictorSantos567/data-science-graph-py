# visualização dos dados em python
import matplotlib.pyplot as plt

x = [1, 2, 5]
y = [2, 3, 7]

title = "Gráfico de Linhas"
axisx = "Eixo X"
axisy = "Eixo Y"

# Título
plt.title(title)

# Eixos
plt.xlabel(axisx)
plt.ylabel(axisy)

# grafico de linhas
plt.plot(x, y)
plt.show()
