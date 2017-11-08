'''
    This Example opens an Image and transform the image into grayscale, halftone, dithering, and primary colors.
    You need PILLOW (Python Imaging Library fork) and Python 3.5.
    -Isai B. Cicourel
'''

from PIL import Image

def open_image(path):
  newImage = Image.open(path)
  return newImage

def save_image(image, path):
  image.save(path, 'png')


def create_image(i, j):
  image = Image.new("L", (i, j), "white")
  return image


def meu_filtro(imagem, mascara):
    M, N = imagem.size
    mm, nn = mascara.size

    # nova = create_image(M, N)
    pixels = imagem.load()

    # mascara = create_image(mm, nn)
    pixels_mascara = mascara.load()

    for m in range(1, M - 1):
        for n in range(1, N - 1):
            pixels[m - 1, n - 1] = \
                (pixels_mascara[0, 0] * pixels[m - 1, n - 1]) + \
                 (pixels_mascara[0, 1] * pixels[m - 1, n])     + \
                  (pixels_mascara[0, 2] * pixels[m - 1, n + 1]) + \
                   (pixels_mascara[1, 0] * pixels[m, n - 1])     + \
                    (pixels_mascara[1, 1] * pixels[m, n])         + \
                     (pixels_mascara[1, 2] * pixels[m, n + 1])     + \
                      (pixels_mascara[2, 0] * pixels[m + 1, n-1])   + \
                      (pixels_mascara[2, 1] * pixels[m + 1, n])     + \
                      (pixels_mascara[2, 2] * pixels[m + 1, n+1])
    return imagem