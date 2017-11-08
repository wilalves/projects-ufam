from filtro import *

src_image = "../img/Fig0338.tif"

# Carregar a imagem
img_entrada = open_image(src_image)
img_entrada.show()

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
img_filtrada.show()
