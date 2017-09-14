from PIL import Image

# def interpolacao_bilinear (self, src_image, resolucao):

    # Imagem de entrada
src_image = "../img/Fig0220a.tif"
in_img = Image.open(src_image)

M, N = in_img.size

resolucao_in = in_img.info['dpi']

MM = (M*100/resolucao_in)
NN = (N*100/resolucao_in)

# Imagem de saida
out_img_MM = Image.new("L", (M,N))
out_pixel_MM = out_img_MM.load()

out_img_NN = Image.new("L", (M,N))
out_pixel_NN = out_img_NN.load()


for m in range(MM):
    out_img_MM[m] = M - (M - 1)* (MM - out_img_MM[m]) / MM - 1

for m in range(MM):
    out_img_NN[n] = N - (N - 1)* (NN - out_img_NN[n]) / NN - 1



