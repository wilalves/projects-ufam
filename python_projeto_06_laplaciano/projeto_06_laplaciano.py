from python_projeto_05_filtragem_espacial.filtro import *
import numpy as np

src_image = "../img/Fig0338.tif"

# Carregar a imagem
img_entrada = open_image(src_image)
# img_entrada.show()

# cria uma mascara 3x3
mascara = create_image(3, 3)
pixel_mascara = mascara.load()

# Definir os valores da mascara
for m in range(3):
    for n in range(3):
        print("Linha:", m, "Coluna:", n)
        pixel_mascara[m, n] = int(input("Digite: "))

# Fazer a chamada do filtro
img_filtrada = my_filter(img_entrada, mascara)

img_a = np.add(img_entrada, img_filtrada)
img_b = np.subtract(img_entrada, img_filtrada)

img_max = np.amax(img_filtrada)

img_min = np.amin(img_filtrada)

a = np.subtract(img_filtrada, img_min)
b = np.subtract(img_max, img_min)

img_c = np.divide(a, b)

img_entrada.show()
img_filtrada.show()
img_a.show()
img_b.show()
img_c.show()
