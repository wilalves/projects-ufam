from filtro import *

src_image = "../img/Fig0338.tif"

in_img = open_image(src_image)

# cria uma mascara
mascara = create_image(3, 3)
pixel_mascara = mascara.load()

for m in range(3):
    for n in range(3):
        print("Linha:", m, "Coluna:", n)
        pixel_mascara[m, n] = int(input("Digite: "))


filtrada = meu_filtro(in_img, mascara)

filtrada.show()

