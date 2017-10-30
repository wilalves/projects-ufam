from PIL import Image
import numpy as np
import cv2


def meu_filtro(imagem, mascara):

    M, N = imagem.size

    MM, MN = mascara.size

    in_pixel = imagem.load()

    img_duas_mais= Image.new("L", (M + 2, N + 2))
    out_img_duas_mais = img_duas_mais.load()

    for m in range(M):
        for n in range(N):
            out_img_duas_mais[m + 1, n + 1] = in_pixel[m, n]

    for a in range(0, N+1):
        out_img_duas_mais[0, a] = out_pixel[1, a]

    for a in range(0, N+1):
        out_img_duas_mais[M+1, a] = out_pixel[M+1, a]

    for a in range(0, M+1):
        out_img_duas_mais[a, 0] = out_pixel[a, 1]

    for a in range(0, M+1):
        out_img_duas_mais[a, N+1] = out_pixel[a, N]

    img_filtro = Image.new("L", (M, N))
    out_img_filtro = img_filtro.load()

    # Faz o a varredura da imagem aplicando o filtro
    for m in range(M):
        for n in range(N):
            for k in range(MM):
                for l in range(MN):
                    out_img_filtro[m, n] = out_img_filtro[m, n] + mascara[k, l] * out_img_duas_mais(m + (k - 1), n + (l - 1))
            out_img_filtro[m, n] = round(out_img_filtro[m, n])

def normalize(arr):
    """
    Linear normalization
    http://en.wikipedia.org/wiki/Normalization_%28image_processing%29
    """
    arr = arr.astype('float')
    # Do not touch the alpha channel
    for i in range(3):
        minval = arr[...,i].min()
        maxval = arr[...,i].max()
        if minval != maxval:
            arr[...,i] -= minval
            arr[...,i] *= (255.0/(maxval-minval))
    return arr