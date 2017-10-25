from PIL import Image

# def interpolacao_bilinear (self, src_image, resolucao):

    # Imagem de entrada
src_image = "out_100_DPI_image_python.tif"
in_img = Image.open(src_image)
in_pixel = in_img.load()

M, N = in_img.size

resolucao_in = in_img.info['dpi'][0]

#inToDo
#essa resolução esta fixa mas deve ser inserida pelo usuario
MM = round(M*1250/resolucao_in)
NN = round(N*1250/resolucao_in)

# Imagem de saida
out_img_MM = []
# out_pixel_MM = out_img_MM.load()

out_img_NN = []
# out_pixel_NN = out_img_NN.load()

out_img_DONE = Image.new("L", (M,N))
out_pixel_DONE = out_img_DONE.load()


for m in range(MM):
    out_img_MM.append(M - (M - 1) * (MM - m) / MM - 1)

for n in range(NN):
    out_img_NN.append(N - (N - 1) * (NN - n) / NN - 1)


for i in range(MM):
    for j in range(NN):
        X = round(out_img_MM[i])
        XP = round(out_img_MM[i] + 0.499)
        Y = round(out_img_NN[j])
        YP = round(out_img_NN[j] + 0.499)

        U = out_img_NN[j] - Y
        A = out_img_MM[i] - XP

        um = in_pixel[XP,YP]
        dois = in_pixel[XP,Y]
        tres = in_pixel[X,YP]
        quatro = in_pixel[X,Y]

        out_pixel_DONE[i,j] = round(A * (U * um) + (1 - U) * dois + (1 - A) * (U * tres) + (1 - U) * quatro)

out_img_DONE.save('out_1250_DPI_image_python.tif', 'tiff')

out_img_DONE.show()