from PIL import Image


def meu_filtro(imagem, mascara):
    M, N = imagem.size

    MM, MN = mascara.size

    in_pixel = imagem.load()

    out_img = Image.new("L", (M + 2, N + 2))
    out_pixel = out_img.load()

    for m in range(M):
        for n in range(N):
            out_pixel[m + 1, n + 1] = in_pixel[m, n]

    for a in range(0, N+1):
        out_pixel[0, a] = out_pixel[1, a]

    for a in range(0, N+1):
        out_pixel[M+1, a] = out_pixel[M+1, a]

    for a in range(0, M+1):
        out_pixel[a, 0] = out_pixel[a, 1]

    for a in range(0, M+1):
        out_pixel[a, N+1] = out_pixel[a, N]

    filt_img = Image.new("L", (M, N))
    filt_img_mask = filt_img.load()

    # Faz o a varredura da imagem aplicando o filtro
    for m in range(M):
        for n in range(N):
            for k in range(MM):
                for l in range(MN):
                    filt_img_mask[m, n] = filt_img_mask[m, n] + mascara[k, l] * out_pixel(m + (k - 1), n + (l - 1))
            filt_img_mask[m, n] = round(filt_img_mask[m, n])




# Imagem de entrada
in_img = Image.open("../img/teste.tif")
in_img.show()

mascara_a = Image.new("L", (3, 3))
mask = mascara_a.load()

teste = meu_filtro(in_img, mascara_a)

#mostra imagem de entrada
teste.show()