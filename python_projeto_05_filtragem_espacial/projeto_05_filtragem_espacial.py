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

    print("aqui")

# Imagem de entrada
in_img = Image.open("../img/teste.tif")

mascara = Image.new("L", (3, 3))
mascara_M, mascara_N = mascara.size
mask = mascara.load()

meu_filtro(in_img, mascara)


#mostra imagem de entrada
in_img.show()