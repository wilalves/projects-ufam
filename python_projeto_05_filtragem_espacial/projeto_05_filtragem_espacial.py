from PIL import Image


def meu_filtro(imagem, mascara):
    M, N = imagem.size

    in_pixel = imagem.load()

    out_img = Image.new("L", (M + 2, N + 2))
    out_pixel = out_img.load()

    for m in range(M):
        for n in range(N):
            out_pixel[m, n] = in_pixel[m, n]

    # Duplica as ultimas linhas e as ultimas colunas
    out_pixel[0, 0:N+1] = int(out_pixel[1, 0:N+1])
    out_pixel[M+1, 0:N+1] = int(out_pixel[M+1, 0:N+1])
    out_pixel[0:M+1, 0] = int(out_pixel[0:M+1, 1])
    out_pixel[0:M+1, N+1] = int(out_pixel[0:M+1, N])

    print("aqui")

# Imagem de entrada
in_img = Image.open("../img/teste.tif")

mascara = Image.new("L", (3, 3))
mascara_M, mascara_N = mascara.size
mask = mascara.load()

meu_filtro(in_img, mascara)


#mostra imagem de entrada
in_img.show()