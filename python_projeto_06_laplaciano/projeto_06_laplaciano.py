from python_projeto_05_filtragem_espacial.filtro import my_filter

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

'''
Imagem_03=Imagem_01+uint8(Imagem_02);
Imagem_04=Imagem_01-uint8(Imagem_02);

Min_Imagem_02 = min(Imagem_02(:));
Max_Imagem_02 = max(Imagem_02(:));
Imagem_05 = (Imagem_02 - Min_Imagem_02) / (Max_Imagem_02 - Min_Imagem_02);

imtool(Imagem_01);
imtool(uint8(Imagem_02));
imtool(Imagem_03);
imtool(Imagem_04);
imtool(Imagem_05);
'''

img_filtrada.show()
