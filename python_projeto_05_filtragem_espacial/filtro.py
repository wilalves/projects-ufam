'''
    This Example opens an Image and filtering.
    You need PILLOW (Python Imaging Library fork) and Python 3.6.
    - Willian Alves @willalves
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


def my_filter(image, mask):
    # Definir quantidade de linhas e colunas, imagem e mascara
    M, N = image.size
    mm, nn = mask.size

    # Ativa o modo processamento para manipular a imagem
    pixels = image.load()
    pixels_mask = mask.load()

    #Aplica o procedimento de convolução
    for m in range(1, M - 1):
        for n in range(1, N - 1):
            pixels[m - 1, n - 1] = \
                (pixels_mask[0, 0] * pixels[m - 1, n - 1]) + \
                 (pixels_mask[0, 1] * pixels[m - 1, n])     + \
                  (pixels_mask[0, 2] * pixels[m - 1, n + 1]) + \
                   (pixels_mask[1, 0] * pixels[m, n - 1])     + \
                    (pixels_mask[1, 1] * pixels[m, n])         + \
                     (pixels_mask[1, 2] * pixels[m, n + 1])     + \
                      (pixels_mask[2, 0] * pixels[m + 1, n-1])   + \
                       (pixels_mask[2, 1] * pixels[m + 1, n])     + \
                        (pixels_mask[2, 2] * pixels[m + 1, n+1])
    return image