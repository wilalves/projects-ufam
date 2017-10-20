from PIL import Image


def meu_filtro(imagem, mascara):
    M, N = imagem.size

    in_pixel = imagem.load()

    out_img = Image.new("L", (M + 2, N + 2))
    out_pixel = out_img.load()

    print(out_img)

    for m in range(M):
        for n in range(N):
            out_pixel[m, n] = in_pixel[m, n]

    # Duplica as ultimas linhas e as ultimas colunas
    for a in range(0, N+1):
        out_pixel[0, a] = out_pixel[1, a]

    for a in range(0, N+1):
        out_pixel[M+1, a] = out_pixel[M+1, a]

    for a in range(0, M+1):
        out_pixel[a, 0] = out_pixel[a, 1]

    for a in range(0, M+1):
        out_pixel[a, N+1] = out_pixel[a, N]

    mask = Image.new("L", (3, 3))
    mask_u = mask.load()

    # Faz o a varredura da imagem aplicando o filtro
    for m in range(1, M):
        for n in range(1, N):
            for k in range(1, mascara_M):
                for l in range(1, mascara_N):
                    mask_u[m, n] = mask_u[m, n] + mascara[k, l] * out_pixel(m + (k - 1), n + (l - 1));
            mask_u[m, n] = round(mask_u[m, n]);

    print("aqui")

# Imagem de entrada
in_img = Image.open("../img/teste.tif")

mascara = Image.new("L", (3, 3))
mascara_M, mascara_N = mascara.size
mask = mascara.load()

meu_filtro(in_img, mascara)



#mostra imagem de entrada
in_img.show()