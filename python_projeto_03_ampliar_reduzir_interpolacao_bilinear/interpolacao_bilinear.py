from PIL import Image

# def interpolacao_bilinear (self, src_image, resolucao):

    # Imagem de entrada
src_image = "../img/Fig0220a.tif"
in_img = Image.open(src_image)
in_pixel = in_img.load()

M, N = in_img.size

resolucao_in = in_img.info['dpi'][0]

MM = round(M*100/resolucao_in)
NN = round(N*100/resolucao_in)

# Imagem de saida
out_img_MM = []
# out_pixel_MM = out_img_MM.load()

out_img_NN = []
# out_pixel_NN = out_img_NN.load()

out_img_DONE = Image.new("L", (M,N))
out_pixel_DONE = out_img_DONE.load()


for m in range(MM):
    out_img_MM.append(M - (M - 1)* (MM - out_img_MM[m]) / MM - 1)

for n in range(MM):
    out_img_NN[n] = N - (N - 1)* (NN - out_img_NN[n]) / NN - 1


for i in range(MM):
    for j in range(NN):
        X = round(out_img_MM[i])
        XP = round(out_img_MM[i]+0.499)
        Y = round(out_img_NN[j])
        YP = round(out_img_NN[j] + 0.499)

        U = out_img_NN[j] - Y
        A = out_img_MM[i] - XP

        out_img_DONE[i,j] = A * (U * in_pixel(XP,YP)+(1-U)*in_pixel(XP,Y))+ (1 - A) * (U*in_pixel[X,YP]+(1-U)*in_pixel[xy])


out_img_DONE.show()