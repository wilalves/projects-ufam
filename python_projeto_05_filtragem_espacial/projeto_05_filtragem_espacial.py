from PIL import Image


def meu_filtro(self, imagem, mascara):
    M, N = imagem.size

    mascara_M, mascara_N = mascara.size

    out_img = Image.new("L", (M + 2, N + 2))
    out_pixel = out_img.load()

    for m in range(M):
        for n in range(N):
            out_pixel[m, n] = in_pixel[m, n]

    # Duplica as ultimas linhas e as ultimas colunas
    out_pixel(1, for a in range(1, N + 2)) = out_pixel(2, for a in range(1, N + 2))
    out_pixel((M + 2), for a in range(1, N + 2)) = out_pixel((M + 1), for a in range(1, N + 2))
    out_pixel(for a in (1, M + 2), 1) = out_pixel(for a in (1, M + 2), 2)
    out_pixel(for a in (1, M + 2), (N + 2)) = out_pixel(for a in (1, M + 2), (N + 1))


    print("aqui")